[ Hugging Face](/)

Transformers 文档

Pipelines

# Transformers

Pipelines

Pipeline 是使用模型进行推理的绝佳且简单的方式。这些 Pipeline 对象抽象了库中大部分复杂代码，提供了一个专用于多种任务的简单 API，包括命名实体识别（Named Entity Recognition）、掩码语言建模（Masked Language Modeling）、情感分析（Sentiment Analysis）、特征提取（Feature Extraction）和问答（Question Answering）。参见[任务总结](../task_summary)了解使用示例。

有两种 Pipeline 抽象类别需要注意：

  * [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) 是最强大的对象，封装了所有其他 Pipeline。
  * 特定任务的 Pipeline 可用于[音频](#audio)、[计算机视觉](#computer-vision)、[自然语言处理](#natural-language-processing)和[多模态](#multimodal)任务。

## [](#transformers.pipeline) Pipeline 抽象

_pipeline_ 抽象是所有其他可用 Pipeline 的包装器。它像任何其他 Pipeline 一样被实例化，但可以提供额外的便利性。

对单个项目的简单调用：

    >>> pipe = pipeline("text-classification")
    >>> pipe("This restaurant is awesome")
    [{'label': 'POSITIVE', 'score': 0.9998743534088135}]

如果你想使用 [Hub](https://huggingface.co) 上的特定模型，如果 Hub 上的模型已经定义了任务，你可以忽略任务：

    >>> pipe = pipeline(model="FacebookAI/roberta-large-mnli")
    >>> pipe("This restaurant is awesome")
    [{'label': 'NEUTRAL', 'score': 0.7313136458396912}]

要在多个项目上调用 Pipeline，可以使用_列表_调用它。

    >>> pipe = pipeline("text-classification")
    >>> pipe(["This restaurant is awesome", "This restaurant is awful"])
    [{'label': 'POSITIVE', 'score': 0.9998743534088135},
     {'label': 'NEGATIVE', 'score': 0.9996669292449951}]

要迭代整个数据集，建议直接使用 `dataset`。这意味着你不需要一次分配整个数据集，也不需要自己进行批处理。

    import datasets
    from transformers import pipeline
    from transformers.pipelines.pt_utils import KeyDataset
    from tqdm.auto import tqdm

    pipe = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-base-960h", device=0)
    dataset = datasets.load_dataset("superb", name="asr", split="test")

    for out in tqdm(pipe(KeyDataset(dataset, "file"))):
        print(out)

为方便使用，也可以使用生成器：

    from transformers import pipeline

    pipe = pipeline("text-classification")

    def data():
        while True:
            yield "This is a test"

    for out in pipe(data()):
        print(out)

## [](#pipeline-parameters) Pipeline 参数

`pipeline()` 函数的主要参数包括：

  * **task** (`str`) — 定义返回哪个 Pipeline 的任务。当前接受的任务有：
    * `"audio-classification"`：返回 [AudioClassificationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.AudioClassificationPipeline)。
    * `"automatic-speech-recognition"`：返回 [AutomaticSpeechRecognitionPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.AutomaticSpeechRecognitionPipeline)。
    * `"depth-estimation"`：返回 [DepthEstimationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.DepthEstimationPipeline)。
    * `"document-question-answering"`：返回 [DocumentQuestionAnsweringPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.DocumentQuestionAnsweringPipeline)。
    * `"feature-extraction"`：返回 [FeatureExtractionPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.FeatureExtractionPipeline)。
    * `"fill-mask"`：返回 [FillMaskPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.FillMaskPipeline)。
    * `"image-classification"`：返回 [ImageClassificationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.ImageClassificationPipeline)。
    * `"image-segmentation"`：返回 [ImageSegmentationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.ImageSegmentationPipeline)。
    * `"image-text-to-text"`：返回 [ImageTextToTextPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.ImageTextToTextPipeline)。
    * `"image-to-image"`：返回 [ImageToImagePipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.ImageToImagePipeline)。
    * `"object-detection"`：返回 [ObjectDetectionPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.ObjectDetectionPipeline)。
    * `"question-answering"`：返回 [QuestionAnsweringPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.QuestionAnsweringPipeline)。
    * `"summarization"`：返回 [SummarizationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.SummarizationPipeline)。
    * `"table-question-answering"`：返回 [TableQuestionAnsweringPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.TableQuestionAnsweringPipeline)。
    * `"text2text-generation"`：返回 [Text2TextGenerationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Text2TextGenerationPipeline)。
    * `"text-classification"`（或 `"sentiment-analysis"`）：返回 [TextClassificationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.TextClassificationPipeline)。
    * `"text-generation"`：返回 [TextGenerationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.TextGenerationPipeline)。
    * `"text-to-audio"`（或 `"text-to-speech"`）：返回 [TextToAudioPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.TextToAudioPipeline)。
    * `"token-classification"`（或 `"ner"`）：返回 [TokenClassificationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.TokenClassificationPipeline)。
    * `"translation"`：返回 [TranslationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.TranslationPipeline)。
    * `"translation_xx_to_yy"`：返回 [TranslationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.TranslationPipeline)。
    * `"video-classification"`：返回 [VideoClassificationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.VideoClassificationPipeline)。
    * `"visual-question-answering"`：返回 [VisualQuestionAnsweringPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.VisualQuestionAnsweringPipeline)。
    * `"zero-shot-audio-classification"`：返回 [ZeroShotAudioClassificationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.ZeroShotAudioClassificationPipeline)。
    * `"zero-shot-classification"`：返回 [ZeroShotClassificationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.ZeroShotClassificationPipeline)。
    * `"zero-shot-image-classification"`：返回 [ZeroShotImageClassificationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.ZeroShotImageClassificationPipeline)。
    * `"zero-shot-object-detection"`：返回 [ZeroShotObjectDetectionPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.ZeroShotObjectDetectionPipeline)。
  * **model** (`PreTrainedModel` 或 `TFPreTrainedModel`，_可选_) — 用于推理的模型。可以是 Hub 上模型的路径标识符。
  * **config** (`str` 或 `PreTrainedConfig`，_可选_) — 用作模型配置的配置。可以是 Hub 上配置的路径标识符。
  * **tokenizer** (`str` 或 `PreTrainedTokenizer`，_可选_) — 用作模型分词器的分词器。可以是 Hub 上分词器的路径标识符。
  * **feature_extractor** (`str` 或 `FeatureExtractionMixin`，_可选_) — 用作模型特征提取器的特征提取器。可以是 Hub 上特征提取器的路径标识符。
  * **image_processor** (`str` 或 `BaseImageProcessor`，_可选_) — 用作模型图像处理器的图像处理器。可以是 Hub 上图像处理器的路径标识符。
  * **processor** (`str` 或 `ProcessorMixin`，_可选_) — 用作模型处理器的处理器。可以是 Hub 上处理器的路径标识符。
  * **revision** (`str`，_可选_，默认为 `"main"`) — 当从 Hub 提供模型的特定版本时，可以是分支名称、标签名称或提交 ID。
  * **use_fast** (`bool`，_可选_，默认为 `True`) — 如果可用，使用基于 Rust 的 [🤗 Tokenizers](https://github.com/huggingface/tokenizers) 分词器。
  * **token** (`str` 或 `bool`，_可选_) — 用作 HTTP 承载令牌的令牌，用于远程文件的身份验证。如果为 `True`，则使用在运行 `huggingface-cli login` 时生成的令牌（存储在 `~/.huggingface` 中）。
  * **device** (`int` 或 `str` 或 `torch.device`，_可选_) — 定义此 Pipeline 将在哪个设备上运行。对于 PyTorch，默认为 CPU，设置为 0 表示使用第一个 GPU。
  * **device_map** (`str` 或 `dict[str, int | str]`，_可选_) — 直接将 `device_map` 传递给模型加载。
  * **dtype** (`str` 或 `torch.dtype`，_可选_) — 直接将 `dtype` 传递给模型加载。
  * **trust_remote_code** (`bool`，_可选_，默认为 `False`) — 如果为 `True`，则允许执行 Hub 上模型定义的自定义代码。
  * **model_kwargs** (`dict[str, Any]`，_可选_) — 传递给模型加载方法的关键字参数字典。

## [](#pipeline-output-format) Pipeline 输出格式

Pipeline 的输出格式取决于任务类型：

  * **文本分类/情感分析**：`[{'label': str, 'score': float}]`
  * **文本生成**：`[{'generated_text': str}]`
  * **命名实体识别**：`[{'entity': str, 'score': float, 'index': int, 'word': str, 'start': int, 'end': int}]`
  * **问答**：`{'score': float, 'start': int, 'end': int, 'answer': str}`
  * **摘要**：`[{'summary_text': str}]`
  * **翻译**：`[{'translation_text': str}]`
  * **特征提取**：`torch.Tensor` 或 `np.ndarray`
  * **图像分类**：`[{'label': str, 'score': float}]`
  * **目标检测**：`[{'score': float, 'label': str, 'box': {'xmin': int, 'ymin': int, 'xmax': int, 'ymax': int}}]`
  * **图像分割**：`[{'score': float, 'label': str, 'mask': str}]`（mask 为 base64 编码的 PNG 图像）

> 完整的 API 参考文档请参阅 [Pipeline API 参考](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline)。

[ 在 GitHub 上更新](https://github.com/huggingface/transformers/blob/main/docs/source/en/main_classes/pipelines.md)

[←处理器](/docs/transformers/main_classes/processors) [文本生成→](/docs/transformers/main_classes/text_generation)

[Pipeline](#pipelines)[Pipeline 抽象](#transformers.pipeline)[Pipeline 参数](#pipeline-parameters)[Pipeline 输出格式](#pipeline-output-format)
