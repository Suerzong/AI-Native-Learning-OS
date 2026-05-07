[ Hugging Face](/)

Transformers 文档

目标检测

# Transformers

目标检测

目标检测（Object detection）是检测图像中实例（如人、建筑物或汽车）的计算机视觉任务。目标检测模型接收图像作为输入，输出检测到对象的边界框坐标和相关标签。一个图像可以包含多个对象，每个对象有自己的边界框和标签（例如，可以有汽车和建筑物），每个对象可以出现在图像的不同部分（例如，图像可以有几辆汽车）。此任务通常用于自动驾驶中检测行人、路标和交通灯等。其他应用包括计数图像中的对象、图像搜索等。

在本指南中，你将学习如何：

  1. 在 [CPPE-5](https://huggingface.co/datasets/cppe-5) 数据集上微调 [DETR](https://huggingface.co/docs/transformers/model_doc/detr)（一种将卷积骨干与编码器-解码器 Transformer 结合的模型）。
  2. 使用微调后的模型进行推理。

## [](#load-the-cppe-5-dataset) 加载 CPPE-5 数据集

[CPPE-5 数据集](https://huggingface.co/datasets/cppe-5)包含带有标注的图像，标注识别了 COVID-19 大流行背景下的医疗个人防护设备（PPE）。

首先加载数据集并从 `train` 创建 `validation` 分割：

    >>> from datasets import load_dataset
    >>> cppe5 = load_dataset("cppe-5")
    >>> if "validation" not in cppe5:
    ...     split = cppe5["train"].train_test_split(0.15, seed=1337)
    ...     cppe5["train"] = split["train"]
    ...     cppe5["validation"] = split["test"]

数据集中的示例有以下字段：

  * `image_id`：示例图像 ID
  * `image`：包含图像的 `PIL.Image.Image` 对象
  * `width`：图像宽度
  * `height`：图像高度
  * `objects`：包含图像中对象边界框元数据的字典：
    * `id`：标注 ID
    * `area`：边界框面积
    * `bbox`：对象的边界框（[COCO 格式](https://albumentations.ai/docs/getting_started/bounding_boxes_augmentation/#coco)）
    * `category`：对象类别，可能的值包括 `Coverall (0)`、`Face_Shield (1)`、`Gloves (2)`、`Goggles (3)` 和 `Mask (4)`

## [](#preprocess-the-data) 数据预处理

要微调模型，必须预处理数据以完全匹配预训练模型使用的方法。[AutoImageProcessor](/docs/transformers/v5.8.0/en/model_doc/auto#transformers.AutoImageProcessor) 负责处理图像数据以创建 DETR 模型可以训练的 `pixel_values`、`pixel_mask` 和 `labels`。

首先，实例化与你想要微调的模型相同检查点的图像处理器：

    >>> from transformers import AutoImageProcessor
    >>> MAX_SIZE = IMAGE_SIZE
    >>> image_processor = AutoImageProcessor.from_pretrained(
    ...     MODEL_NAME,
    ...     do_resize=True,
    ...     size={"max_height": MAX_SIZE, "max_width": MAX_SIZE},
    ...     do_pad=True,
    ...     pad_size={"height": MAX_SIZE, "width": MAX_SIZE},
    ... )

在将图像传递给 `image_processor` 之前，对数据集应用两种预处理变换：

  * 增强图像
  * 重新格式化标注以满足 DETR 要求

使用 [Albumentations](https://albumentations.ai/docs/) 进行图像增强：

    >>> import albumentations as A
    >>> train_augment_and_transform = A.Compose(
    ...     [
    ...         A.Perspective(p=0.1),
    ...         A.HorizontalFlip(p=0.5),
    ...         A.RandomBrightnessContrast(p=0.5),
    ...         A.HueSaturationValue(p=0.1),
    ...     ],
    ...     bbox_params=A.BboxParams(format="coco", label_fields=["category"], clip=True, min_area=25),
    ... )

然后创建自定义 `collate_fn` 来将图像批处理在一起：

    >>> import torch
    >>> def collate_fn(batch):
    ...     data = {}
    ...     data["pixel_values"] = torch.stack([x["pixel_values"] for x in batch])
    ...     data["labels"] = [x["labels"] for x in batch]
    ...     if "pixel_mask" in batch[0]:
    ...         data["pixel_mask"] = torch.stack([x["pixel_mask"] for x in batch])
    ...     return data

## [](#preparing-function-to-compute-map) 准备计算 mAP 的函数

目标检测模型通常使用一组 [COCO 风格指标](https://cocodataset.org/#detection-eval)进行评估。我们将使用 `torchmetrics` 来计算 `mAP`（平均精度均值）和 `mAR`（平均召回率均值）指标。

## [](#training-the-detection-model) 训练检测模型

使用 [AutoModelForObjectDetection](/docs/transformers/v5.8.0/en/model_doc/auto#transformers.AutoModelForObjectDetection) 加载模型：

    >>> from transformers import AutoModelForObjectDetection
    >>> model = AutoModelForObjectDetection.from_pretrained(
    ...     MODEL_NAME,
    ...     id2label=id2label,
    ...     label2id=label2id,
    ...     ignore_mismatched_sizes=True,
    ... )

在 [TrainingArguments](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.TrainingArguments) 中使用 `output_dir` 指定保存模型的位置：

    >>> from transformers import TrainingArguments
    >>> training_args = TrainingArguments(
    ...     output_dir="detr_finetuned_cppe5",
    ...     num_train_epochs=30,
    ...     fp16=False,
    ...     per_device_train_batch_size=8,
    ...     dataloader_num_workers=4,
    ...     learning_rate=5e-5,
    ...     lr_scheduler_type="cosine",
    ...     weight_decay=1e-4,
    ...     max_grad_norm=0.01,
    ...     metric_for_best_model="eval_map",
    ...     greater_is_better=True,
    ...     load_best_model_at_end=True,
    ...     eval_strategy="epoch",
    ...     save_strategy="epoch",
    ...     save_total_limit=2,
    ...     remove_unused_columns=False,
    ...     eval_do_concat_batches=False,
    ...     push_to_hub=True,
    ... )

最后，将所有内容组合在一起并调用 [train()](/docs/transformers/v5.8.0/en/main_classes/trainer#transformers.Trainer.train)：

    >>> from transformers import Trainer
    >>> trainer = Trainer(
    ...     model=model,
    ...     args=training_args,
    ...     train_dataset=cppe5["train"],
    ...     eval_dataset=cppe5["validation"],
    ...     processing_class=image_processor,
    ...     data_collator=collate_fn,
    ...     compute_metrics=eval_compute_metrics_fn,
    ... )
    >>> trainer.train()

## [](#inference) 推理

现在你已经微调了模型、评估了它并上传到 Hugging Face Hub，可以使用它进行推理。

    >>> import torch
    >>> import requests
    >>> from PIL import Image, ImageDraw
    >>> from transformers import AutoImageProcessor, AutoModelForObjectDetection

    >>> url = "https://images.pexels.com/photos/8413299/pexels-photo-8413299.jpeg?auto=compress&cs=tinysrgb&w=630&h=375&dpr=2"
    >>> image = Image.open(requests.get(url, stream=True).raw)

从 Hugging Face Hub 加载模型和图像处理器：

    >>> from accelerate import Accelerator
    >>> device = Accelerator().device
    >>> model_repo = "qubvel-hf/detr_finetuned_cppe5"
    >>> image_processor = AutoImageProcessor.from_pretrained(model_repo)
    >>> model = AutoModelForObjectDetection.from_pretrained(model_repo)
    >>> model = model.to(device)

检测边界框：

    >>> with torch.no_grad():
    ...     inputs = image_processor(images=[image], return_tensors="pt")
    ...     outputs = model(**inputs.to(device))
    ...     target_sizes = torch.tensor([[image.size[1], image.size[0]]])
    ...     results = image_processor.post_process_object_detection(outputs, threshold=0.3, target_sizes=target_sizes)[0]

    >>> for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
    ...     box = [round(i, 2) for i in box.tolist()]
    ...     print(
    ...         f"Detected {model.config.id2label[label.item()]} with confidence "
    ...         f"{round(score.item(), 3)} at location {box}"
    ...     )

绘制结果：

    >>> draw = ImageDraw.Draw(image)
    >>> for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
    ...     box = [round(i, 2) for i in box.tolist()]
    ...     x, y, x2, y2 = tuple(box)
    ...     draw.rectangle((x, y, x2, y2), outline="red", width=1)
    ...     draw.text((x, y), model.config.id2label[label.item()], fill="white")
    >>> image

[ 在 GitHub 上更新](https://github.com/huggingface/transformers/blob/main/docs/source/en/tasks/object_detection.md)

[←视频分类](/docs/transformers/tasks/video_classification) [零样本目标检测→](/docs/transformers/tasks/zero_shot_object_detection)

[目标检测](#object-detection)[加载 CPPE-5 数据集](#load-the-cppe-5-dataset)[数据预处理](#preprocess-the-data)[准备计算 mAP 的函数](#preparing-function-to-compute-map)[训练检测模型](#training-the-detection-model)[评估](#evaluate)[推理](#inference)
