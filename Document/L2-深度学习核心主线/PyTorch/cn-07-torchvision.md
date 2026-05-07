# TorchVision 目标检测微调教程

在本教程中，我们将在 [Penn-Fudan 行人检测与分割数据库](https://www.cis.upenn.edu/~jshi/ped_html/)上微调预训练的 [Mask R-CNN](https://arxiv.org/abs/1703.06870) 模型。它包含 170 张图像和 345 个行人实例，我们将用它来说明如何使用 torchvision 中的新功能来训练自定义数据集上的目标检测和实例分割模型。

> 本教程仅适用于 torchvision 版本 >=0.16 或 nightly。如果你使用的是 torchvision<=0.15，请改用[此教程](https://github.com/pytorch/tutorials/blob/d686b662932a380a58b7683425faa00c06bcf502/intermediate_source/torchvision_tutorial.rst)。

## 定义数据集

用于训练目标检测、实例分割和人体关键点检测的参考脚本允许轻松支持添加新的自定义数据集。数据集应继承标准的 `torch.utils.data.Dataset` 类，并实现 `__len__` 和 `__getitem__`。

我们唯一的要求是数据集的 `__getitem__` 应返回一个元组：

  * image：形状为 `[3, H, W]` 的 `torchvision.tv_tensors.Image`，一个纯张量，或大小为 `(H, W)` 的 PIL 图像
  * target：包含以下字段的字典：
    * `boxes`，形状为 `[N, 4]` 的 `torchvision.tv_tensors.BoundingBoxes`：`N` 个边界框的坐标，格式为 `[x0, y0, x1, y1]`
    * `labels`，形状为 `[N]` 的整数 `torch.Tensor`：每个边界框的标签。`0` 始终表示背景类。
    * `image_id`，int：图像标识符
    * `area`，形状为 `[N]` 的浮点 `torch.Tensor`：边界框的面积
    * `iscrowd`，形状为 `[N]` 的 uint8 `torch.Tensor`：`iscrowd=True` 的实例将在评估时被忽略
    * （可选）`masks`，形状为 `[N, H, W]` 的 `torchvision.tv_tensors.Mask`：每个对象的分割掩码

### 为 PennFudan 编写自定义数据集

让我们为 PennFudan 数据集编写一个数据集类：

    class PennFudanDataset(torch.utils.data.Dataset):
        def __init__(self, root, transforms):
            self.root = root
            self.transforms = transforms
            self.imgs = list(sorted(os.listdir(os.path.join(root, "PNGImages"))))
            self.masks = list(sorted(os.listdir(os.path.join(root, "PedMasks"))))

        def __getitem__(self, idx):
            img_path = os.path.join(self.root, "PNGImages", self.imgs[idx])
            mask_path = os.path.join(self.root, "PedMasks", self.masks[idx])
            img = read_image(img_path)
            mask = read_image(mask_path)
            obj_ids = torch.unique(mask)
            obj_ids = obj_ids[1:]
            num_objs = len(obj_ids)
            masks = (mask == obj_ids[:, None, None]).to(dtype=torch.uint8)
            boxes = masks_to_boxes(masks)
            labels = torch.ones((num_objs,), dtype=torch.int64)
            image_id = idx
            area = (boxes[:, 3] - boxes[:, 1]) * (boxes[:, 2] - boxes[:, 0])
            iscrowd = torch.zeros((num_objs,), dtype=torch.int64)

            img = tv_tensors.Image(img)
            target = {}
            target["boxes"] = tv_tensors.BoundingBoxes(boxes, format="XYXY", canvas_size=F.get_size(img))
            target["masks"] = tv_tensors.Mask(masks)
            target["labels"] = labels
            target["image_id"] = image_id
            target["area"] = area
            target["iscrowd"] = iscrowd

            if self.transforms is not None:
                img, target = self.transforms(img, target)

            return img, target

        def __len__(self):
            return len(self.imgs)

## 定义你的模型

在本教程中，我们将使用 [Mask R-CNN](https://arxiv.org/abs/1703.06870)，它基于 [Faster R-CNN](https://arxiv.org/abs/1506.01497)。Faster R-CNN 是一个预测图像中潜在对象的边界框和类别分数的模型。

Mask R-CNN 在 Faster R-CNN 中添加了一个额外的分支，该分支也为每个实例预测分割掩码。

有两种常见情况可能需要修改 TorchVision 模型库中的可用模型。第一种是我们想从预训练模型开始，只微调最后一层。第二种是我们想用不同的骨干网络替换模型的骨干（例如，为了更快的预测）。

### 1 - 从预训练模型微调

    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(weights="DEFAULT")
    num_classes = 2
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

### 2 - 修改模型以添加不同的骨干

    backbone = torchvision.models.mobilenet_v2(weights="DEFAULT").features
    backbone.out_channels = 1280
    anchor_generator = AnchorGenerator(
        sizes=((32, 64, 128, 256, 512),),
        aspect_ratios=((0.5, 1.0, 2.0),)
    )
    roi_pooler = torchvision.ops.MultiScaleRoIAlign(
        featmap_names=['0'],
        output_size=7,
        sampling_ratio=2
    )
    model = FasterRCNN(
        backbone,
        num_classes=2,
        rpn_anchor_generator=anchor_generator,
        box_roi_pool=roi_pooler
    )

### PennFudan 数据集的目标检测和实例分割模型

在我们的例子中，我们想从预训练模型微调，因为我们的数据集非常小，所以我们将遵循方法 1。

我们还想计算实例分割掩码，所以我们将使用 Mask R-CNN：

    def get_model_instance_segmentation(num_classes):
        model = torchvision.models.detection.maskrcnn_resnet50_fpn(weights="DEFAULT")
        in_features = model.roi_heads.box_predictor.cls_score.in_features
        model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)
        in_features_mask = model.roi_heads.mask_predictor.conv5_mask.in_channels
        hidden_layer = 256
        model.roi_heads.mask_predictor = MaskRCNNPredictor(
            in_features_mask,
            hidden_layer,
            num_classes
        )
        return model

## 整合所有内容

由于 v0.15.0，torchvision 提供了[新的 Transforms API](https://pytorch.org/vision/stable/transforms.html)，可以轻松编写目标检测和分割任务的数据增强管道。

让我们编写一些用于数据增强/转换的辅助函数：

    def get_transform(train):
        transforms = []
        if train:
            transforms.append(T.RandomHorizontalFlip(0.5))
        transforms.append(T.ToDtype(torch.float, scale=True))
        transforms.append(T.ToPureTensor())
        return T.Compose(transforms)

## 测试 `forward()` 方法（可选）

在遍历数据集之前，最好看看模型在训练和推理时对样本数据的期望。

## 放在一起训练

    device = torch.accelerator.current_accelerator() if torch.accelerator.is_available() else torch.device('cpu')
    num_classes = 2
    dataset = PennFudanDataset('data/PennFudanPed', get_transform(train=True))
    dataset_test = PennFudanDataset('data/PennFudanPed', get_transform(train=False))

    indices = torch.randperm(len(dataset)).tolist()
    dataset = torch.utils.data.Subset(dataset, indices[:-50])
    dataset_test = torch.utils.data.Subset(dataset_test, indices[-50:])

    data_loader = torch.utils.data.DataLoader(
        dataset, batch_size=2, shuffle=True, collate_fn=utils.collate_fn)
    data_loader_test = torch.utils.data.DataLoader(
        dataset_test, batch_size=1, shuffle=False, collate_fn=utils.collate_fn)

    model = get_model_instance_segmentation(num_classes)
    model.to(device)

    params = [p for p in model.parameters() if p.requires_grad]
    optimizer = torch.optim.SGD(params, lr=0.005, momentum=0.9, weight_decay=0.0005)
    lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=3, gamma=0.1)

    num_epochs = 2
    for epoch in range(num_epochs):
        train_one_epoch(model, optimizer, data_loader, device, epoch, print_freq=10)
        lr_scheduler.step()
        evaluate(model, data_loader_test, device=device)

    print("完成了！")

## 总结

在本教程中，你学习了如何为自定义数据集上的目标检测模型创建自己的训练管道。为此，你编写了一个返回图像和真实边界框及分割掩码的 `torch.utils.data.Dataset` 类。你还利用了在 COCO train2017 上预训练的 Mask R-CNN 模型来对这个新数据集执行迁移学习。

有关更完整的示例（包括多机/多 GPU 讑练），请查看 torchvision 仓库中的 `references/detection/train.py`。
