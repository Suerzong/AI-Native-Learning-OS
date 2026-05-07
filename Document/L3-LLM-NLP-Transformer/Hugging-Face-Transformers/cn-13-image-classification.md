[ Hugging Face](/)

Transformers 文档

图像分类

# Transformers

图像分类

图像分类（Image classification）为图像分配标签或类别。与文本或音频分类不同，输入是组成图像的像素值。图像分类有许多应用，如自然灾害后检测损害、监测作物健康或帮助筛查医学图像中的疾病迹象。

本指南说明如何：

  1. 在 [Food-101](https://huggingface.co/datasets/ethz/food101) 数据集上微调 [ViT](../model_doc/vit) 以分类图像中的食物项目。
  2. 使用微调后的模型进行推理。

## [](#load-food-101-dataset) 加载 Food-101 数据集

首先从 🤗 Datasets 库加载 Food-101 数据集的较小子集：

    >>> from datasets import load_dataset
    >>> food = load_dataset("ethz/food101", split="train[:5000]")

使用 `train_test_split` 方法将数据集的 `train` 分割为训练集和测试集：

    >>> food = food.train_test_split(test_size=0.2)

数据集中的每个示例有两个字段：

  * `image`：食物项目的 PIL 图像
  * `label`：食物项目的标签类别

为使模型更容易从标签 ID 获取标签名称，创建一个将标签名称映射到整数的字典，反之亦然：

    >>> labels = food["train"].features["label"].names
    >>> label2id, id2label = dict(), dict()
    >>> for i, label in enumerate(labels):
    ...     label2id[label] = str(i)
    ...     id2label[str(i)] = label

现在你可以将标签 ID 转换为标签名称：

    >>> id2label[str(79)]
    'prime_rib'

## [](#preprocess) 预处理

加载 ViT 图像处理器以将图像处理为张量：

    >>> from transformers import AutoImageProcessor
    >>> checkpoint = "google/vit-base-patch16-224-in21k"
    >>> image_processor = AutoImageProcessor.from_pretrained(checkpoint)

对图像应用一些图像变换以使模型更鲁棒，防止过拟合。这里你将使用 torchvision 的 [`transforms`](https://pytorch.org/vision/stable/transforms.html) 模块：

    >>> from torchvision.transforms import RandomResizedCrop, Compose, Normalize, ToTensor
    >>> normalize = Normalize(mean=image_processor.image_mean, std=image_processor.image_std)
    >>> size = (
    ...     image_processor.size["shortest_edge"]
    ...     if "shortest_edge" in image_processor.size
    ...     else (image_processor.size["height"], image_processor.size["width"])
    ... )
    >>> _transforms = Compose([RandomResizedCrop(size), ToTensor(), normalize])

然后创建一个预处理函数来应用变换并返回 `pixel_values`（模型的输入）：

    >>> def transforms(examples):
    ...     examples["pixel_values"] = [_transforms(img.convert("RGB")) for img in examples["image"]]
    ...     del examples["image"]
    ...     return examples

使用 🤗 Datasets 的 `with_transform` 方法将预处理函数应用于整个数据集：

    >>> food = food.with_transform(transforms)

使用 [DefaultDataCollator](/docs/transformers/v5.8.0/en/main_classes/data_collator#transformers.DefaultDataCollator) 创建一批示例：

    >>> from transformers import DefaultDataCollator
    >>> data_collator = DefaultDataCollator()

## [](#evaluate) 评估

对于此任务，加载 [accuracy](https://huggingface.co/spaces/evaluate-metric/accuracy) 指标：

    >>> import evaluate
    >>> accuracy = evaluate.load("accuracy")

    >>> import numpy as np

    >>> def compute_metrics(eval_pred):
    ...     predictions, labels = eval_pred
    ...     predictions = np.argmax(predictions, axis=1)
    ...     return accuracy.compute(predictions=predictions, references=labels)

## [](#train) 训练

使用 [AutoModelForImageClassification](/docs/transformers/v5.8.0/en/model_doc/auto#transformers.AutoModelForImageClassification) 加载 ViT。指定标签数量以及预期的标签映射：

    >>> from transformers import AutoModelForImageClassification, TrainingArguments, Trainer
    >>> model = AutoModelForImageClassification.from_pretrained(
    ...     checkpoint,
    ...     num_labels=len(labels),
    ...     id2label=id2label,
    ...     label2id=label2id,
    ... )

定义训练参数并开始训练：

    >>> training_args = TrainingArguments(
    ...     output_dir="my_awesome_food_model",
    ...     remove_unused_columns=False,
    ...     eval_strategy="epoch",
    ...     save_strategy="epoch",
    ...     learning_rate=5e-5,
    ...     per_device_train_batch_size=16,
    ...     gradient_accumulation_steps=4,
    ...     per_device_eval_batch_size=16,
    ...     num_train_epochs=3,
    ...     warmup_steps=0.1,
    ...     logging_steps=10,
    ...     load_best_model_at_end=True,
    ...     metric_for_best_model="accuracy",
    ...     push_to_hub=True,
    ... )

    >>> trainer = Trainer(
    ...     model=model,
    ...     args=training_args,
    ...     data_collator=data_collator,
    ...     train_dataset=food["train"],
    ...     eval_dataset=food["test"],
    ...     processing_class=image_processor,
    ...     compute_metrics=compute_metrics,
    ... )

    >>> trainer.train()

## [](#inference) 推理

很好，现在你已经微调了模型，可以使用它进行推理！

加载你想运行推理的图像：

    >>> ds = load_dataset("ethz/food101", split="validation[:10]")
    >>> image = ds["image"][0]

使用 [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) 进行推理：

    >>> from transformers import pipeline
    >>> classifier = pipeline("image-classification", model="my_awesome_food_model")
    >>> classifier(image)

或手动进行推理。加载图像处理器以预处理图像并将输入作为 PyTorch 张量返回：

    >>> from transformers import AutoImageProcessor
    >>> import torch
    >>> image_processor = AutoImageProcessor.from_pretrained("my_awesome_food_model")
    >>> inputs = image_processor(image, return_tensors="pt")

将输入传递给模型并返回 logits：

    >>> from transformers import AutoModelForImageClassification
    >>> model = AutoModelForImageClassification.from_pretrained("my_awesome_food_model")
    >>> with torch.no_grad():
    ...     logits = model(**inputs).logits

获取概率最高的预测标签：

    >>> predicted_label = logits.argmax(-1).item()
    >>> model.config.id2label[predicted_label]
    'beignets'

[ 在 GitHub 上更新](https://github.com/huggingface/transformers/blob/main/docs/source/en/tasks/image_classification.md)

[←文本转语音](/docs/transformers/tasks/text-to-speech) [图像分割→](/docs/transformers/tasks/semantic_segmentation)

[图像分类](#image-classification)[加载 Food-101 数据集](#load-food-101-dataset)[预处理](#preprocess)[评估](#evaluate)[训练](#train)[推理](#inference)
