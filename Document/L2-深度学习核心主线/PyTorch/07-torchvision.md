[Skip to main content](#main-content)

__Back to top

__ `Ctrl`+`K`

Rate this Page

★ ★ ★ ★ ★

intermediate/torchvision_tutorial

![](../_static/img/pytorch-colab.svg) Run in Google Colab Colab ![](../_static/img/pytorch-download.svg) Download Notebook Notebook ![](../_static/img/pytorch-github.svg) View on GitHub GitHub

Note

[Go to the end](#sphx-glr-download-intermediate-torchvision-tutorial-py) to download the full example code.

# TorchVision Object Detection Finetuning Tutorial[#](#torchvision-object-detection-finetuning-tutorial "Link to this heading")

Created On: Dec 14, 2023 | Last Updated: Sep 05, 2025 | Last Verified: Nov 05, 2024

For this tutorial, we will be finetuning a pre-trained [Mask R-CNN](https://arxiv.org/abs/1703.06870) model on the [Penn-Fudan Database for Pedestrian Detection and Segmentation](https://www.cis.upenn.edu/~jshi/ped_html/). It contains 170 images with 345 instances of pedestrians, and we will use it to illustrate how to use the new features in torchvision in order to train an object detection and instance segmentation model on a custom dataset.

Note

This tutorial works only with torchvision version >=0.16 or nightly. If you’re using torchvision<=0.15, please follow [this tutorial instead](https://github.com/pytorch/tutorials/blob/d686b662932a380a58b7683425faa00c06bcf502/intermediate_source/torchvision_tutorial.rst).

## Defining the Dataset[#](#defining-the-dataset "Link to this heading")

The reference scripts for training object detection, instance segmentation and person keypoint detection allows for easily supporting adding new custom datasets. The dataset should inherit from the standard `torch.utils.data.Dataset` class, and implement `__len__` and `__getitem__`.

The only specificity that we require is that the dataset `__getitem__` should return a tuple:

  * image: [`torchvision.tv_tensors.Image`](https://docs.pytorch.org/vision/stable/generated/torchvision.tv_tensors.Image.html#torchvision.tv_tensors.Image "\(in Torchvision vmain \(0.26.0+4ab3324\)\)") of shape `[3, H, W]`, a pure tensor, or a PIL Image of size `(H, W)`

  * target: a dict containing the following fields

    * `boxes`, [`torchvision.tv_tensors.BoundingBoxes`](https://docs.pytorch.org/vision/stable/generated/torchvision.tv_tensors.BoundingBoxes.html#torchvision.tv_tensors.BoundingBoxes "\(in Torchvision vmain \(0.26.0+4ab3324\)\)") of shape `[N, 4]`: the coordinates of the `N` bounding boxes in `[x0, y0, x1, y1]` format, ranging from `0` to `W` and `0` to `H`

    * `labels`, integer `torch.Tensor` of shape `[N]`: the label for each bounding box. `0` represents always the background class.

    * `image_id`, int: an image identifier. It should be unique between all the images in the dataset, and is used during evaluation

    * `area`, float `torch.Tensor` of shape `[N]`: the area of the bounding box. This is used during evaluation with the COCO metric, to separate the metric scores between small, medium and large boxes.

    * `iscrowd`, uint8 `torch.Tensor` of shape `[N]`: instances with `iscrowd=True` will be ignored during evaluation.

    * (optionally) `masks`, [`torchvision.tv_tensors.Mask`](https://docs.pytorch.org/vision/stable/generated/torchvision.tv_tensors.Mask.html#torchvision.tv_tensors.Mask "\(in Torchvision vmain \(0.26.0+4ab3324\)\)") of shape `[N, H, W]`: the segmentation masks for each one of the objects

If your dataset is compliant with above requirements then it will work for both training and evaluation codes from the reference script. Evaluation code will use scripts from `pycocotools` which can be installed with `pip install pycocotools`.

Note

For Windows, please install `pycocotools` from [gautamchitnis](https://github.com/gautamchitnis/cocoapi) with command

`pip install git+https://github.com/gautamchitnis/cocoapi.git@cocodataset-master#subdirectory=PythonAPI`

One note on the `labels`. The model considers class `0` as background. If your dataset does not contain the background class, you should not have `0` in your `labels`. For example, assuming you have just two classes, _cat_ and _dog_ , you can define `1` (not `0`) to represent _cats_ and `2` to represent _dogs_. So, for instance, if one of the images has both classes, your `labels` tensor should look like `[1, 2]`.

Additionally, if you want to use aspect ratio grouping during training (so that each batch only contains images with similar aspect ratios), then it is recommended to also implement a `get_height_and_width` method, which returns the height and the width of the image. If this method is not provided, we query all elements of the dataset via `__getitem__` , which loads the image in memory and is slower than if a custom method is provided.

### Writing a custom dataset for PennFudan[#](#writing-a-custom-dataset-for-pennfudan "Link to this heading")

Let’s write a dataset for the PennFudan dataset. First, let’s download the dataset and extract the [zip file](https://www.cis.upenn.edu/~jshi/ped_html/PennFudanPed.zip):


    wget https://www.cis.upenn.edu/~jshi/ped_html/PennFudanPed.zip -P data
    cd data && unzip PennFudanPed.zip


We have the following folder structure:


    PennFudanPed/
      PedMasks/
        FudanPed00001_mask.png
        FudanPed00002_mask.png
        FudanPed00003_mask.png
        FudanPed00004_mask.png
        ...
      PNGImages/
        FudanPed00001.png
        FudanPed00002.png
        FudanPed00003.png
        FudanPed00004.png


Here is one example of a pair of images and segmentation masks


    import matplotlib.pyplot as plt
    from torchvision.io import [read_image](https://docs.pytorch.org/vision/stable/generated/torchvision.io.read_image.html#torchvision.io.read_image "torchvision.io.read_image")


    image = [read_image](https://docs.pytorch.org/vision/stable/generated/torchvision.io.read_image.html#torchvision.io.read_image "torchvision.io.read_image")("data/PennFudanPed/PNGImages/FudanPed00046.png")
    mask = [read_image](https://docs.pytorch.org/vision/stable/generated/torchvision.io.read_image.html#torchvision.io.read_image "torchvision.io.read_image")("data/PennFudanPed/PedMasks/FudanPed00046_mask.png")

    plt.figure(figsize=(16, 8))
    plt.subplot(121)
    plt.title("Image")
    plt.imshow(image.permute(1, 2, 0))
    plt.subplot(122)
    plt.title("Mask")
    plt.imshow(mask.permute(1, 2, 0))


![Image, Mask](../_images/sphx_glr_torchvision_tutorial_001.png)


    <matplotlib.image.AxesImage object at 0x7f1ea4f98730>


So each image has a corresponding segmentation mask, where each color correspond to a different instance. Let’s write a `torch.utils.data.Dataset` class for this dataset. In the code below, we are wrapping images, bounding boxes and masks into [`torchvision.tv_tensors.TVTensor`](https://docs.pytorch.org/vision/stable/generated/torchvision.tv_tensors.TVTensor.html#torchvision.tv_tensors.TVTensor "\(in Torchvision vmain \(0.26.0+4ab3324\)\)") classes so that we will be able to apply torchvision built-in transformations ([new Transforms API](https://pytorch.org/vision/stable/transforms.html)) for the given object detection and segmentation task. Namely, image tensors will be wrapped by [`torchvision.tv_tensors.Image`](https://docs.pytorch.org/vision/stable/generated/torchvision.tv_tensors.Image.html#torchvision.tv_tensors.Image "\(in Torchvision vmain \(0.26.0+4ab3324\)\)"), bounding boxes into [`torchvision.tv_tensors.BoundingBoxes`](https://docs.pytorch.org/vision/stable/generated/torchvision.tv_tensors.BoundingBoxes.html#torchvision.tv_tensors.BoundingBoxes "\(in Torchvision vmain \(0.26.0+4ab3324\)\)") and masks into [`torchvision.tv_tensors.Mask`](https://docs.pytorch.org/vision/stable/generated/torchvision.tv_tensors.Mask.html#torchvision.tv_tensors.Mask "\(in Torchvision vmain \(0.26.0+4ab3324\)\)"). As [`torchvision.tv_tensors.TVTensor`](https://docs.pytorch.org/vision/stable/generated/torchvision.tv_tensors.TVTensor.html#torchvision.tv_tensors.TVTensor "\(in Torchvision vmain \(0.26.0+4ab3324\)\)") are `torch.Tensor` subclasses, wrapped objects are also tensors and inherit the plain `torch.Tensor` API. For more information about torchvision `tv_tensors` see [this documentation](https://pytorch.org/vision/main/auto_examples/transforms/plot_transforms_getting_started.html#what-are-tvtensors).


    import os
    import torch

    from torchvision.io import [read_image](https://docs.pytorch.org/vision/stable/generated/torchvision.io.read_image.html#torchvision.io.read_image "torchvision.io.read_image")
    from torchvision.ops.boxes import [masks_to_boxes](https://docs.pytorch.org/vision/stable/generated/torchvision.ops.masks_to_boxes.html#torchvision.ops.masks_to_boxes "torchvision.ops.masks_to_boxes")
    from torchvision import tv_tensors
    from torchvision.transforms.v2 import functional as F


    class PennFudanDataset(torch.utils.data.Dataset):
        def __init__(self, root, transforms):
            self.root = root
            self.transforms = transforms
            # load all image files, sorting them to
            # ensure that they are aligned
            self.imgs = list(sorted(os.listdir(os.path.join(root, "PNGImages"))))
            self.masks = list(sorted(os.listdir(os.path.join(root, "PedMasks"))))

        def __getitem__(self, idx):
            # load images and masks
            img_path = os.path.join(self.root, "PNGImages", self.imgs[idx])
            mask_path = os.path.join(self.root, "PedMasks", self.masks[idx])
            img = [read_image](https://docs.pytorch.org/vision/stable/generated/torchvision.io.read_image.html#torchvision.io.read_image "torchvision.io.read_image")(img_path)
            mask = [read_image](https://docs.pytorch.org/vision/stable/generated/torchvision.io.read_image.html#torchvision.io.read_image "torchvision.io.read_image")(mask_path)
            # instances are encoded as different colors
            obj_ids = torch.unique(mask)
            # first id is the background, so remove it
            obj_ids = obj_ids[1:]
            num_objs = len(obj_ids)

            # split the color-encoded mask into a set
            # of binary masks
            masks = (mask == obj_ids[:, None, None]).to(dtype=torch.uint8)

            # get bounding box coordinates for each mask
            boxes = [masks_to_boxes](https://docs.pytorch.org/vision/stable/generated/torchvision.ops.masks_to_boxes.html#torchvision.ops.masks_to_boxes "torchvision.ops.masks_to_boxes")(masks)

            # there is only one class
            labels = torch.ones((num_objs,), dtype=torch.int64)

            image_id = idx
            area = (boxes[:, 3] - boxes[:, 1]) * (boxes[:, 2] - boxes[:, 0])
            # suppose all instances are not crowd
            iscrowd = torch.zeros((num_objs,), dtype=torch.int64)

            # Wrap sample and targets into torchvision tv_tensors:
            img = [tv_tensors.Image](https://docs.pytorch.org/vision/stable/generated/torchvision.tv_tensors.Image.html#torchvision.tv_tensors.Image "torchvision.tv_tensors.Image")(img)

            target = {}
            target["boxes"] = [tv_tensors.BoundingBoxes](https://docs.pytorch.org/vision/stable/generated/torchvision.tv_tensors.BoundingBoxes.html#torchvision.tv_tensors.BoundingBoxes "torchvision.tv_tensors.BoundingBoxes")(boxes, format="XYXY", canvas_size=F.get_size(img))
            target["masks"] = [tv_tensors.Mask](https://docs.pytorch.org/vision/stable/generated/torchvision.tv_tensors.Mask.html#torchvision.tv_tensors.Mask "torchvision.tv_tensors.Mask")(masks)
            target["labels"] = labels
            target["image_id"] = image_id
            target["area"] = area
            target["iscrowd"] = iscrowd

            if self.transforms is not None:
                img, target = self.transforms(img, target)

            return img, target

        def __len__(self):
            return len(self.imgs)


That’s all for the dataset. Now let’s define a model that can perform predictions on this dataset.

## Defining your model[#](#defining-your-model "Link to this heading")

In this tutorial, we will be using [Mask R-CNN](https://arxiv.org/abs/1703.06870), which is based on top of [Faster R-CNN](https://arxiv.org/abs/1506.01497). Faster R-CNN is a model that predicts both bounding boxes and class scores for potential objects in the image.

![../_static/img/tv_tutorial/tv_image03.png](../_static/img/tv_tutorial/tv_image03.png)

Mask R-CNN adds an extra branch into Faster R-CNN, which also predicts segmentation masks for each instance.

![../_static/img/tv_tutorial/tv_image04.png](../_static/img/tv_tutorial/tv_image04.png)

There are two common situations where one might want to modify one of the available models in TorchVision Model Zoo. The first is when we want to start from a pre-trained model, and just finetune the last layer. The other is when we want to replace the backbone of the model with a different one (for faster predictions, for example).

Let’s go see how we would do one or another in the following sections.

### 1 - Finetuning from a pretrained model[#](#finetuning-from-a-pretrained-model "Link to this heading")

Let’s suppose that you want to start from a model pre-trained on COCO and want to finetune it for your particular classes. Here is a possible way of doing it:


    import torchvision
    from torchvision.models.detection.faster_rcnn import FastRCNNPredictor

    # load a model pre-trained on COCO
    model = [torchvision.models.detection.fasterrcnn_resnet50_fpn](https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.detection.fasterrcnn_resnet50_fpn.html#torchvision.models.detection.fasterrcnn_resnet50_fpn "torchvision.models.detection.fasterrcnn_resnet50_fpn")(weights="DEFAULT")

    # replace the classifier with a new one, that has
    # num_classes which is user-defined
    num_classes = 2  # 1 class (person) + background
    # get number of input features for the classifier
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    # replace the pre-trained head with a new one
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)



    Downloading: "https://download.pytorch.org/models/fasterrcnn_resnet50_fpn_coco-258fb6c6.pth" to /var/lib/ci-user/.cache/torch/hub/checkpoints/fasterrcnn_resnet50_fpn_coco-258fb6c6.pth

      0%|          | 0.00/160M [00:00<?, ?B/s]
     25%|██▌       | 40.2M/160M [00:00<00:00, 422MB/s]
     51%|█████▏    | 82.0M/160M [00:00<00:00, 431MB/s]
     79%|███████▊  | 126M/160M [00:00<00:00, 443MB/s]
    100%|██████████| 160M/160M [00:00<00:00, 442MB/s]


### 2 - Modifying the model to add a different backbone[#](#modifying-the-model-to-add-a-different-backbone "Link to this heading")


    import torchvision
    from torchvision.models.detection import FasterRCNN
    from torchvision.models.detection.rpn import AnchorGenerator

    # load a pre-trained model for classification and return
    # only the features
    backbone = [torchvision.models.mobilenet_v2](https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.mobilenet_v2.html#torchvision.models.mobilenet_v2 "torchvision.models.mobilenet_v2")(weights="DEFAULT").features
    # ``FasterRCNN`` needs to know the number of
    # output channels in a backbone. For mobilenet_v2, it's 1280
    # so we need to add it here
    backbone.out_channels = 1280

    # let's make the RPN generate 5 x 3 anchors per spatial
    # location, with 5 different sizes and 3 different aspect
    # ratios. We have a Tuple[Tuple[int]] because each feature
    # map could potentially have different sizes and
    # aspect ratios
    anchor_generator = AnchorGenerator(
        sizes=((32, 64, 128, 256, 512),),
        aspect_ratios=((0.5, 1.0, 2.0),)
    )

    # let's define what are the feature maps that we will
    # use to perform the region of interest cropping, as well as
    # the size of the crop after rescaling.
    # if your backbone returns a Tensor, featmap_names is expected to
    # be [0]. More generally, the backbone should return an
    # ``OrderedDict[Tensor]``, and in ``featmap_names`` you can choose which
    # feature maps to use.
    [roi_pooler](https://docs.pytorch.org/vision/stable/generated/torchvision.ops.MultiScaleRoIAlign.html#torchvision.ops.MultiScaleRoIAlign "torchvision.ops.MultiScaleRoIAlign") = [torchvision.ops.MultiScaleRoIAlign](https://docs.pytorch.org/vision/stable/generated/torchvision.ops.MultiScaleRoIAlign.html#torchvision.ops.MultiScaleRoIAlign "torchvision.ops.MultiScaleRoIAlign")(
        featmap_names=['0'],
        output_size=7,
        sampling_ratio=2
    )

    # put the pieces together inside a Faster-RCNN model
    model = FasterRCNN(
        backbone,
        num_classes=2,
        rpn_anchor_generator=anchor_generator,
        box_roi_pool=[roi_pooler](https://docs.pytorch.org/vision/stable/generated/torchvision.ops.MultiScaleRoIAlign.html#torchvision.ops.MultiScaleRoIAlign "torchvision.ops.MultiScaleRoIAlign")
    )



    Downloading: "https://download.pytorch.org/models/mobilenet_v2-7ebf99e0.pth" to /var/lib/ci-user/.cache/torch/hub/checkpoints/mobilenet_v2-7ebf99e0.pth

      0%|          | 0.00/13.6M [00:00<?, ?B/s]
    100%|██████████| 13.6M/13.6M [00:00<00:00, 410MB/s]


### Object detection and instance segmentation model for PennFudan Dataset[#](#object-detection-and-instance-segmentation-model-for-pennfudan-dataset "Link to this heading")

In our case, we want to finetune from a pre-trained model, given that our dataset is very small, so we will be following approach number 1.

Here we want to also compute the instance segmentation masks, so we will be using Mask R-CNN:


    import torchvision
    from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
    from torchvision.models.detection.mask_rcnn import MaskRCNNPredictor


    def get_model_instance_segmentation(num_classes):
        # load an instance segmentation model pre-trained on COCO
        model = [torchvision.models.detection.maskrcnn_resnet50_fpn](https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.detection.maskrcnn_resnet50_fpn.html#torchvision.models.detection.maskrcnn_resnet50_fpn "torchvision.models.detection.maskrcnn_resnet50_fpn")(weights="DEFAULT")

        # get number of input features for the classifier
        in_features = model.roi_heads.box_predictor.cls_score.in_features
        # replace the pre-trained head with a new one
        model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

        # now get the number of input features for the mask classifier
        in_features_mask = model.roi_heads.mask_predictor.conv5_mask.in_channels
        hidden_layer = 256
        # and replace the mask predictor with a new one
        model.roi_heads.mask_predictor = MaskRCNNPredictor(
            in_features_mask,
            hidden_layer,
            num_classes
        )

        return model


That’s it, this will make `model` be ready to be trained and evaluated on your custom dataset.

## Putting everything together[#](#putting-everything-together "Link to this heading")

In `references/detection/`, we have a number of helper functions to simplify training and evaluating detection models. Here, we will use `references/detection/engine.py` and `references/detection/utils.py`. Just download everything under `references/detection` to your folder and use them here. On Linux if you have `wget`, you can download them using below commands:


    os.system("wget https://raw.githubusercontent.com/pytorch/vision/main/references/detection/engine.py")
    os.system("wget https://raw.githubusercontent.com/pytorch/vision/main/references/detection/utils.py")
    os.system("wget https://raw.githubusercontent.com/pytorch/vision/main/references/detection/coco_utils.py")
    os.system("wget https://raw.githubusercontent.com/pytorch/vision/main/references/detection/coco_eval.py")
    os.system("wget https://raw.githubusercontent.com/pytorch/vision/main/references/detection/transforms.py")



    0


Since v0.15.0 torchvision provides [new Transforms API](https://pytorch.org/vision/stable/transforms.html) to easily write data augmentation pipelines for Object Detection and Segmentation tasks.

Let’s write some helper functions for data augmentation / transformation:


    from torchvision.transforms import v2 as T


    def get_transform(train):
        transforms = []
        if train:
            transforms.append([T.RandomHorizontalFlip](https://docs.pytorch.org/vision/stable/generated/torchvision.transforms.v2.RandomHorizontalFlip.html#torchvision.transforms.v2.RandomHorizontalFlip "torchvision.transforms.v2.RandomHorizontalFlip")(0.5))
        transforms.append([T.ToDtype](https://docs.pytorch.org/vision/stable/generated/torchvision.transforms.v2.ToDtype.html#torchvision.transforms.v2.ToDtype "torchvision.transforms.v2.ToDtype")(torch.float, scale=True))
        transforms.append([T.ToPureTensor](https://docs.pytorch.org/vision/stable/generated/torchvision.transforms.v2.ToPureTensor.html#torchvision.transforms.v2.ToPureTensor "torchvision.transforms.v2.ToPureTensor")())
        return [T.Compose](https://docs.pytorch.org/vision/stable/generated/torchvision.transforms.v2.Compose.html#torchvision.transforms.v2.Compose "torchvision.transforms.v2.Compose")(transforms)


## Testing `forward()` method (Optional)[#](#testing-forward-method-optional "Link to this heading")

Before iterating over the dataset, it’s good to see what the model expects during training and inference time on sample data.


    import utils

    model = [torchvision.models.detection.fasterrcnn_resnet50_fpn](https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.detection.fasterrcnn_resnet50_fpn.html#torchvision.models.detection.fasterrcnn_resnet50_fpn "torchvision.models.detection.fasterrcnn_resnet50_fpn")(weights="DEFAULT")
    dataset = PennFudanDataset('data/PennFudanPed', get_transform(train=True))
    data_loader = torch.utils.data.DataLoader(
        dataset,
        batch_size=2,
        shuffle=True,
        collate_fn=utils.collate_fn
    )

    # For Training
    images, targets = next(iter(data_loader))
    images = list(image for image in images)
    targets = [{k: v for k, v in t.items()} for t in targets]
    output = model(images, targets)  # Returns losses and detections
    print(output)

    # For inference
    model.eval()
    x = [torch.rand(3, 300, 400), torch.rand(3, 500, 400)]
    predictions = model(x)  # Returns predictions
    print(predictions[0])



    {'loss_classifier': tensor(0.0904, grad_fn=<NllLossBackward0>), 'loss_box_reg': tensor(0.0277, grad_fn=<DivBackward0>), 'loss_objectness': tensor(0.0027, grad_fn=<BinaryCrossEntropyWithLogitsBackward0>), 'loss_rpn_box_reg': tensor(0.0029, grad_fn=<DivBackward0>)}
    {'boxes': tensor([], size=(0, 4), grad_fn=<StackBackward0>), 'labels': tensor([], dtype=torch.int64), 'scores': tensor([], grad_fn=<IndexBackward0>)}


We want to be able to train our model on an [accelerator](https://pytorch.org/docs/stable/torch.html#accelerators) such as CUDA, MPS, MTIA, or XPU. Let’s now write the main function which performs the training and the validation:


    from engine import train_one_epoch, evaluate

    # train on the accelerator or on the CPU, if an accelerator is not available
    device = torch.accelerator.current_accelerator() if torch.accelerator.is_available() else torch.device('cpu')

    # our dataset has two classes only - background and person
    num_classes = 2
    # use our dataset and defined transformations
    dataset = PennFudanDataset('data/PennFudanPed', get_transform(train=True))
    dataset_test = PennFudanDataset('data/PennFudanPed', get_transform(train=False))

    # split the dataset in train and test set
    indices = torch.randperm(len(dataset)).tolist()
    dataset = torch.utils.data.Subset(dataset, indices[:-50])
    dataset_test = torch.utils.data.Subset(dataset_test, indices[-50:])

    # define training and validation data loaders
    data_loader = torch.utils.data.DataLoader(
        dataset,
        batch_size=2,
        shuffle=True,
        collate_fn=utils.collate_fn
    )

    data_loader_test = torch.utils.data.DataLoader(
        dataset_test,
        batch_size=1,
        shuffle=False,
        collate_fn=utils.collate_fn
    )

    # get the model using our helper function
    model = get_model_instance_segmentation(num_classes)

    # move model to the right device
    model.to(device)

    # construct an optimizer
    params = [p for p in model.parameters() if p.requires_grad]
    optimizer = torch.optim.SGD(
        params,
        lr=0.005,
        momentum=0.9,
        weight_decay=0.0005
    )

    # and a learning rate scheduler
    lr_scheduler = torch.optim.lr_scheduler.StepLR(
        optimizer,
        step_size=3,
        gamma=0.1
    )

    # let's train it just for 2 epochs
    num_epochs = 2

    for epoch in range(num_epochs):
        # train for one epoch, printing every 10 iterations
        train_one_epoch(model, optimizer, data_loader, device, epoch, print_freq=10)
        # update the learning rate
        lr_scheduler.step()
        # evaluate on the test dataset
        evaluate(model, data_loader_test, device=device)

    print("That's it!")



    Downloading: "https://download.pytorch.org/models/maskrcnn_resnet50_fpn_coco-bf2d0c1e.pth" to /var/lib/ci-user/.cache/torch/hub/checkpoints/maskrcnn_resnet50_fpn_coco-bf2d0c1e.pth

      0%|          | 0.00/170M [00:00<?, ?B/s]
     24%|██▍       | 40.8M/170M [00:00<00:00, 427MB/s]
     49%|████▊     | 82.4M/170M [00:00<00:00, 432MB/s]
     73%|███████▎  | 125M/170M [00:00<00:00, 437MB/s]
     98%|█████████▊| 167M/170M [00:00<00:00, 438MB/s]
    100%|██████████| 170M/170M [00:00<00:00, 436MB/s]
    /var/lib/workspace/intermediate_source/engine.py:30: FutureWarning: `torch.cuda.amp.autocast(args...)` is deprecated. Please use `torch.amp.autocast('cuda', args...)` instead.
      with torch.cuda.amp.autocast(enabled=scaler is not None):
    Epoch: [0]  [ 0/60]  eta: 0:00:47  lr: 0.000090  loss: 3.0393 (3.0393)  loss_classifier: 0.6642 (0.6642)  loss_box_reg: 0.4568 (0.4568)  loss_mask: 1.8924 (1.8924)  loss_objectness: 0.0133 (0.0133)  loss_rpn_box_reg: 0.0126 (0.0126)  time: 0.7851  data: 0.0139  max mem: 1876
    Epoch: [0]  [10/60]  eta: 0:00:13  lr: 0.000936  loss: 1.2444 (1.6999)  loss_classifier: 0.4378 (0.4673)  loss_box_reg: 0.2742 (0.3033)  loss_mask: 0.5838 (0.9043)  loss_objectness: 0.0133 (0.0202)  loss_rpn_box_reg: 0.0032 (0.0047)  time: 0.2704  data: 0.0153  max mem: 2396
    Epoch: [0]  [20/60]  eta: 0:00:09  lr: 0.001783  loss: 1.0126 (1.2566)  loss_classifier: 0.2819 (0.3503)  loss_box_reg: 0.2549 (0.2854)  loss_mask: 0.3257 (0.5976)  loss_objectness: 0.0128 (0.0171)  loss_rpn_box_reg: 0.0032 (0.0063)  time: 0.2167  data: 0.0157  max mem: 2425
    Epoch: [0]  [30/60]  eta: 0:00:07  lr: 0.002629  loss: 0.6141 (1.0499)  loss_classifier: 0.1226 (0.2704)  loss_box_reg: 0.2586 (0.2821)  loss_mask: 0.2422 (0.4766)  loss_objectness: 0.0081 (0.0139)  loss_rpn_box_reg: 0.0064 (0.0069)  time: 0.2157  data: 0.0156  max mem: 2710
    Epoch: [0]  [40/60]  eta: 0:00:04  lr: 0.003476  loss: 0.5555 (0.9109)  loss_classifier: 0.0770 (0.2199)  loss_box_reg: 0.2412 (0.2624)  loss_mask: 0.1998 (0.4105)  loss_objectness: 0.0036 (0.0112)  loss_rpn_box_reg: 0.0061 (0.0069)  time: 0.2179  data: 0.0161  max mem: 2710
    Epoch: [0]  [50/60]  eta: 0:00:02  lr: 0.004323  loss: 0.4124 (0.8076)  loss_classifier: 0.0518 (0.1855)  loss_box_reg: 0.1586 (0.2384)  loss_mask: 0.1830 (0.3673)  loss_objectness: 0.0013 (0.0095)  loss_rpn_box_reg: 0.0057 (0.0069)  time: 0.2165  data: 0.0164  max mem: 2710
    Epoch: [0]  [59/60]  eta: 0:00:00  lr: 0.005000  loss: 0.3360 (0.7363)  loss_classifier: 0.0455 (0.1646)  loss_box_reg: 0.1154 (0.2187)  loss_mask: 0.1782 (0.3377)  loss_objectness: 0.0013 (0.0082)  loss_rpn_box_reg: 0.0057 (0.0071)  time: 0.2162  data: 0.0162  max mem: 2710
    Epoch: [0] Total time: 0:00:13 (0.2261 s / it)
    creating index...
    index created!
    Test:  [ 0/50]  eta: 0:00:04  model_time: 0.0828 (0.0828)  evaluator_time: 0.0029 (0.0029)  time: 0.0945  data: 0.0083  max mem: 2710
    Test:  [49/50]  eta: 0:00:00  model_time: 0.0392 (0.0552)  evaluator_time: 0.0029 (0.0046)  time: 0.0591  data: 0.0093  max mem: 2710
    Test: Total time: 0:00:03 (0.0691 s / it)
    Averaged stats: model_time: 0.0392 (0.0552)  evaluator_time: 0.0029 (0.0046)
    Accumulating evaluation results...
    DONE (t=0.01s).
    Accumulating evaluation results...
    DONE (t=0.01s).
    IoU metric: bbox
     Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.765
     Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.981
     Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.945
     Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
     Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.620
     Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.771
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.395
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.822
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.822
     Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.817
     Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.822
    IoU metric: segm
     Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.764
     Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.981
     Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.950
     Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
     Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.523
     Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.773
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.385
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.807
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.807
     Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.783
     Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.808
    Epoch: [1]  [ 0/60]  eta: 0:00:14  lr: 0.005000  loss: 0.2948 (0.2948)  loss_classifier: 0.0439 (0.0439)  loss_box_reg: 0.1134 (0.1134)  loss_mask: 0.1273 (0.1273)  loss_objectness: 0.0006 (0.0006)  loss_rpn_box_reg: 0.0096 (0.0096)  time: 0.2472  data: 0.0179  max mem: 2710
    Epoch: [1]  [10/60]  eta: 0:00:10  lr: 0.005000  loss: 0.3052 (0.2969)  loss_classifier: 0.0443 (0.0480)  loss_box_reg: 0.1266 (0.1077)  loss_mask: 0.1279 (0.1341)  loss_objectness: 0.0006 (0.0014)  loss_rpn_box_reg: 0.0058 (0.0057)  time: 0.2190  data: 0.0168  max mem: 2710
    Epoch: [1]  [20/60]  eta: 0:00:08  lr: 0.005000  loss: 0.2976 (0.2897)  loss_classifier: 0.0420 (0.0424)  loss_box_reg: 0.0745 (0.0934)  loss_mask: 0.1460 (0.1472)  loss_objectness: 0.0005 (0.0013)  loss_rpn_box_reg: 0.0039 (0.0054)  time: 0.2118  data: 0.0157  max mem: 2710
    Epoch: [1]  [30/60]  eta: 0:00:06  lr: 0.005000  loss: 0.2711 (0.2861)  loss_classifier: 0.0325 (0.0405)  loss_box_reg: 0.0727 (0.0878)  loss_mask: 0.1550 (0.1508)  loss_objectness: 0.0009 (0.0016)  loss_rpn_box_reg: 0.0039 (0.0054)  time: 0.2082  data: 0.0150  max mem: 2710
    Epoch: [1]  [40/60]  eta: 0:00:04  lr: 0.005000  loss: 0.2579 (0.2776)  loss_classifier: 0.0339 (0.0400)  loss_box_reg: 0.0727 (0.0866)  loss_mask: 0.1339 (0.1443)  loss_objectness: 0.0009 (0.0014)  loss_rpn_box_reg: 0.0047 (0.0053)  time: 0.2142  data: 0.0157  max mem: 2710
    Epoch: [1]  [50/60]  eta: 0:00:02  lr: 0.005000  loss: 0.2602 (0.2765)  loss_classifier: 0.0360 (0.0391)  loss_box_reg: 0.0784 (0.0856)  loss_mask: 0.1246 (0.1448)  loss_objectness: 0.0006 (0.0014)  loss_rpn_box_reg: 0.0044 (0.0056)  time: 0.2180  data: 0.0159  max mem: 2768
    Epoch: [1]  [59/60]  eta: 0:00:00  lr: 0.005000  loss: 0.2667 (0.2792)  loss_classifier: 0.0367 (0.0411)  loss_box_reg: 0.0813 (0.0848)  loss_mask: 0.1398 (0.1458)  loss_objectness: 0.0008 (0.0016)  loss_rpn_box_reg: 0.0046 (0.0059)  time: 0.2125  data: 0.0156  max mem: 2768
    Epoch: [1] Total time: 0:00:12 (0.2130 s / it)
    creating index...
    index created!
    Test:  [ 0/50]  eta: 0:00:02  model_time: 0.0406 (0.0406)  evaluator_time: 0.0024 (0.0024)  time: 0.0516  data: 0.0082  max mem: 2768
    Test:  [49/50]  eta: 0:00:00  model_time: 0.0387 (0.0395)  evaluator_time: 0.0025 (0.0035)  time: 0.0518  data: 0.0093  max mem: 2768
    Test: Total time: 0:00:02 (0.0523 s / it)
    Averaged stats: model_time: 0.0387 (0.0395)  evaluator_time: 0.0025 (0.0035)
    Accumulating evaluation results...
    DONE (t=0.01s).
    Accumulating evaluation results...
    DONE (t=0.01s).
    IoU metric: bbox
     Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.809
     Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.990
     Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.931
     Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
     Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.609
     Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.812
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.406
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.846
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.846
     Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.867
     Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.845
    IoU metric: segm
     Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.778
     Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.990
     Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.968
     Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
     Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.475
     Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.790
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.383
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.809
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.809
     Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
     Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.717
     Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.815
    That's it!


So after one epoch of training, we obtain a COCO-style mAP > 50, and a mask mAP of 65.

But what do the predictions look like? Let’s take one image in the dataset and verify


    import matplotlib.pyplot as plt

    from torchvision.utils import [draw_bounding_boxes](https://docs.pytorch.org/vision/stable/generated/torchvision.utils.draw_bounding_boxes.html#torchvision.utils.draw_bounding_boxes "torchvision.utils.draw_bounding_boxes"), [draw_segmentation_masks](https://docs.pytorch.org/vision/stable/generated/torchvision.utils.draw_segmentation_masks.html#torchvision.utils.draw_segmentation_masks "torchvision.utils.draw_segmentation_masks")


    image = [read_image](https://docs.pytorch.org/vision/stable/generated/torchvision.io.read_image.html#torchvision.io.read_image "torchvision.io.read_image")("data/PennFudanPed/PNGImages/FudanPed00046.png")
    [eval_transform](https://docs.pytorch.org/vision/stable/generated/torchvision.transforms.v2.Compose.html#torchvision.transforms.v2.Compose "torchvision.transforms.v2.Compose") = get_transform(train=False)

    model.eval()
    with torch.no_grad():
        x = [eval_transform](https://docs.pytorch.org/vision/stable/generated/torchvision.transforms.v2.Compose.html#torchvision.transforms.v2.Compose "torchvision.transforms.v2.Compose")(image)
        # convert RGBA -> RGB and move to device
        x = x[:3, ...].to(device)
        predictions = model([x, ])
        pred = predictions[0]


    image = (255.0 * (image - image.min()) / (image.max() - image.min())).to(torch.uint8)
    image = image[:3, ...]
    pred_labels = [f"pedestrian: {score:.3f}" for label, score in zip(pred["labels"], pred["scores"])]
    pred_boxes = pred["boxes"].long()
    output_image = [draw_bounding_boxes](https://docs.pytorch.org/vision/stable/generated/torchvision.utils.draw_bounding_boxes.html#torchvision.utils.draw_bounding_boxes "torchvision.utils.draw_bounding_boxes")(image, pred_boxes, pred_labels, colors="red")

    masks = (pred["masks"] > 0.7).squeeze(1)
    output_image = [draw_segmentation_masks](https://docs.pytorch.org/vision/stable/generated/torchvision.utils.draw_segmentation_masks.html#torchvision.utils.draw_segmentation_masks "torchvision.utils.draw_segmentation_masks")(output_image, masks, alpha=0.5, colors="blue")


    plt.figure(figsize=(12, 12))
    plt.imshow(output_image.permute(1, 2, 0))


![torchvision tutorial](../_images/sphx_glr_torchvision_tutorial_002.png)


    <matplotlib.image.AxesImage object at 0x7f1ea33dac80>


The results look good!

## Wrapping up[#](#wrapping-up "Link to this heading")

In this tutorial, you have learned how to create your own training pipeline for object detection models on a custom dataset. For that, you wrote a `torch.utils.data.Dataset` class that returns the images and the ground truth boxes and segmentation masks. You also leveraged a Mask R-CNN model pre-trained on COCO train2017 in order to perform transfer learning on this new dataset.

For a more complete example, which includes multi-machine / multi-GPU training, check `references/detection/train.py`, which is present in the torchvision repository.

**Total running time of the script:** (0 minutes 46.510 seconds)

## Docs

Access comprehensive developer documentation for PyTorch

[View Docs](https://docs.pytorch.org/docs/stable/index.html)

## Tutorials

Get in-depth tutorials for beginners and advanced developers

[View Tutorials](https://docs.pytorch.org/tutorials)

## Resources

Find development resources and get your questions answered

[View Resources](https://pytorch.org/resources)

To analyze traffic and optimize your experience, we serve cookies on this site. By clicking or navigating, you agree to allow our usage of cookies. As the current maintainers of this site, Facebook’s Cookies Policy applies. Learn more, including about available controls: [Cookies Policy](https://opensource.fb.com/legal/cookie-policy).
