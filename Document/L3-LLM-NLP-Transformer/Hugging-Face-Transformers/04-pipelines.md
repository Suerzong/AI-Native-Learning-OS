[ Hugging Face](/)

  * [ Models ](/models)
  * [ Datasets ](/datasets)
  * [ Spaces ](/spaces)
  * [ Buckets new](/storage)
  * [ Docs ](/docs)
  * [ Enterprise ](/enterprise)
  * [Pricing](/pricing)
  *   * * * *

  * [Log In](/login)
  * [Sign Up](/join)

Transformers documentation

Pipelines

# Transformers

🏡 View all docsAWS Trainium & InferentiaAccelerateArgillaAutoTrainBitsandbytesCLIChat UIDataset viewerDatasetsDeploying on AWSDiffusersDistilabelEvaluateGoogle CloudGoogle TPUsGradioHubHub Python LibraryHuggingface.jsInference Endpoints (dedicated)Inference ProvidersKernelsLeRobotLeaderboardsLightevalMicrosoft AzureOptimumPEFTReachy MiniSafetensorsSentence TransformersTRLTasksText Embeddings InferenceText Generation InferenceTokenizersTrackioTransformersTransformers.jsXetsmolagentstimm

Search documentation

mainv5.8.0v5.7.0v5.6.2v5.5.4v5.4.0v5.3.0v5.2.0v5.1.0v5.0.0v4.57.6v4.56.2v4.55.4v4.53.3v4.52.3v4.51.3v4.50.0v4.49.0v4.48.2v4.47.1v4.46.3v4.45.2v4.44.2v4.43.4v4.42.4v4.41.2v4.40.2v4.39.3v4.38.2v4.37.2v4.36.1v4.35.2v4.34.1v4.33.3v4.32.1v4.31.0v4.30.0v4.29.1v4.28.1v4.27.2v4.26.1v4.25.1v4.24.0v4.23.1v4.22.2v4.21.3v4.20.1v4.19.4v4.18.0v4.17.0v4.16.2v4.15.0v4.14.1v4.13.0v4.12.5v4.11.3v4.10.1v4.9.2v4.8.2v4.7.0v4.6.0v4.5.1v4.4.2v4.3.3v4.2.2v4.1.1v4.0.1v3.5.1v3.4.0v3.3.1v3.2.0v3.1.0v3.0.2v2.11.0v2.10.0v2.9.1v2.8.0v2.7.0v2.6.0v2.5.1v2.4.1v2.3.0v2.2.2v2.1.1v2.0.0v1.2.0v1.1.0v1.0.0doc-builder-html ARDEENESFRHIITJAKOPTTRZH

[ ](https://github.com/huggingface/transformers)

Get started

[Transformers](/docs/transformers/index)[Installation](/docs/transformers/installation)[Quickstart](/docs/transformers/quicktour)

Base classes

Models

Preprocessors

Inference

Pipeline API

Generate API

Optimization

Chat with models

Serving

Training

Get started

Customization

[Parameter-efficient fine-tuning](/docs/transformers/peft)

Performance

Distributed training

Hardware

Quantization

Ecosystem integrations

Resources

API

Main Classes

[Auto Classes](/docs/transformers/model_doc/auto)[Backbones](/docs/transformers/main_classes/backbones)[Callbacks](/docs/transformers/main_classes/callback)[Configuration](/docs/transformers/main_classes/configuration)[Continuous batching](/docs/transformers/main_classes/continuous_batching)[Data Collator](/docs/transformers/main_classes/data_collator)[Logging](/docs/transformers/main_classes/logging)[Models](/docs/transformers/main_classes/model)[Text Generation](/docs/transformers/main_classes/text_generation)[Optimization](/docs/transformers/main_classes/optimizer_schedules)[Model outputs](/docs/transformers/main_classes/output)[PEFT](/docs/transformers/main_classes/peft)[Pipelines](/docs/transformers/main_classes/pipelines)[Processors](/docs/transformers/main_classes/processors)[Quantization](/docs/transformers/main_classes/quantization)[Tokenizer](/docs/transformers/main_classes/tokenizer)[Trainer](/docs/transformers/main_classes/trainer)[DeepSpeed](/docs/transformers/main_classes/deepspeed)[ExecuTorch](/docs/transformers/main_classes/executorch)[Feature Extractor](/docs/transformers/main_classes/feature_extractor)[Image Processor](/docs/transformers/main_classes/image_processor)[Video Processor](/docs/transformers/main_classes/video_processor)[Kernels](/docs/transformers/main_classes/kernels)

Models

Internal helpers

Reference

Join the Hugging Face community

and get access to the augmented documentation experience

Collaborate on models, datasets and Spaces

Faster examples with accelerated inference

Switch between documentation themes

[Sign Up](/join)

to get started

Copy page

# [](#pipelines) Pipelines

The pipelines are a great and easy way to use models for inference. These pipelines are objects that abstract most of the complex code from the library, offering a simple API dedicated to several tasks, including Named Entity Recognition, Masked Language Modeling, Sentiment Analysis, Feature Extraction and Question Answering. See the [task summary](../task_summary) for examples of use.

There are two categories of pipeline abstractions to be aware about:

  * The [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) which is the most powerful object encapsulating all other pipelines.
  * Task-specific pipelines are available for [audio](#audio), [computer vision](#computer-vision), [natural language processing](#natural-language-processing), and [multimodal](#multimodal) tasks.

## [](#transformers.pipeline) The pipeline abstraction

The _pipeline_ abstraction is a wrapper around all the other available pipelines. It is instantiated as any other pipeline but can provide additional quality of life.

Simple call on one item:

Copied


    >>> pipe = pipeline("text-classification")
    >>> pipe("This restaurant is awesome")
    [{'label': 'POSITIVE', 'score': 0.9998743534088135}]

If you want to use a specific model from the [hub](https://huggingface.co) you can ignore the task if the model on the hub already defines it:

Copied


    >>> pipe = pipeline(model="FacebookAI/roberta-large-mnli")
    >>> pipe("This restaurant is awesome")
    [{'label': 'NEUTRAL', 'score': 0.7313136458396912}]

To call a pipeline on many items, you can call it with a _list_.

Copied


    >>> pipe = pipeline("text-classification")
    >>> pipe(["This restaurant is awesome", "This restaurant is awful"])
    [{'label': 'POSITIVE', 'score': 0.9998743534088135},
     {'label': 'NEGATIVE', 'score': 0.9996669292449951}]

To iterate over full datasets it is recommended to use a `dataset` directly. This means you don’t need to allocate the whole dataset at once, nor do you need to do batching yourself. This should work just as fast as custom loops on GPU. If it doesn’t don’t hesitate to create an issue.

Copied


    import datasets
    from transformers import pipeline
    from transformers.pipelines.pt_utils import KeyDataset
    from tqdm.auto import tqdm

    pipe = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-base-960h", device=0)
    dataset = datasets.load_dataset("superb", name="asr", split="test")

    # KeyDataset (only *pt*) will simply return the item in the dict returned by the dataset item
    # as we're not interested in the *target* part of the dataset. For sentence pair use KeyPairDataset
    for out in tqdm(pipe(KeyDataset(dataset, "file"))):
        print(out)
        # {"text": "NUMBER TEN FRESH NELLY IS WAITING ON YOU GOOD NIGHT HUSBAND"}
        # {"text": ....}
        # ....

For ease of use, a generator is also possible:

Copied


    from transformers import pipeline

    pipe = pipeline("text-classification")


    def data():
        while True:
            # This could come from a dataset, a database, a queue or HTTP request
            # in a server
            # Caveat: because this is iterative, you cannot use `num_workers > 1` variable
            # to use multiple threads to preprocess data. You can still have 1 thread that
            # does the preprocessing while the main runs the big inference
            yield "This is a test"


    for out in pipe(data()):
        print(out)
        # {"text": "NUMBER TEN FRESH NELLY IS WAITING ON YOU GOOD NIGHT HUSBAND"}
        # {"text": ....}
        # ....

#### transformers.pipeline

[](#transformers.pipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/__init__.py#L641)

( task: str | None = None model: str | PreTrainedModel | None = None config: str | PreTrainedConfig | None = None tokenizer: str | PreTrainedTokenizer | PreTrainedTokenizerFast | None = None feature_extractor: str | FeatureExtractionMixin | None = None image_processor: str | BaseImageProcessor | None = None processor: str | ProcessorMixin | None = None revision: str | None = None use_fast: bool = True token: str | bool | None = None device: int | str | torch.device | None = None device_map: str | dict[str, int | str] | None = None dtype: str | torch.dtype | None = 'auto' trust_remote_code: bool | None = None model_kwargs: dict[str, Any] | None = None pipeline_class: Any | None = None **kwargs: Any ) → [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline)

Parameters

  * [](#transformers.pipeline.task) **task** (`str`) -- The task defining which pipeline will be returned. Currently accepted tasks are:

    * `"audio-classification"`: will return a [AudioClassificationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.AudioClassificationPipeline).
    * `"automatic-speech-recognition"`: will return a [AutomaticSpeechRecognitionPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.AutomaticSpeechRecognitionPipeline).
    * `"depth-estimation"`: will return a [DepthEstimationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.DepthEstimationPipeline).
    * `"document-question-answering"`: will return a [DocumentQuestionAnsweringPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.DocumentQuestionAnsweringPipeline).
    * `"feature-extraction"`: will return a [FeatureExtractionPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.FeatureExtractionPipeline).
    * `"fill-mask"`: will return a [FillMaskPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.FillMaskPipeline):.
    * `"image-classification"`: will return a [ImageClassificationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.ImageClassificationPipeline).
    * `"image-feature-extraction"`: will return an [ImageFeatureExtractionPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.ImageFeatureExtractionPipeline).
    * `"image-segmentation"`: will return a [ImageSegmentationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.ImageSegmentationPipeline).
    * `"image-text-to-text"`: will return a [ImageTextToTextPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.ImageTextToTextPipeline).
    * `"keypoint-matching"`: will return a [KeypointMatchingPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.KeypointMatchingPipeline).
    * `"mask-generation"`: will return a [MaskGenerationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.MaskGenerationPipeline).
    * `"object-detection"`: will return a [ObjectDetectionPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.ObjectDetectionPipeline).
    * `"table-question-answering"`: will return a [TableQuestionAnsweringPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.TableQuestionAnsweringPipeline).
    * `"text-classification"` (alias `"sentiment-analysis"` available): will return a [TextClassificationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.TextClassificationPipeline).
    * `"text-generation"`: will return a [TextGenerationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.TextGenerationPipeline):.
    * `"text-to-audio"` (alias `"text-to-speech"` available): will return a [TextToAudioPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.TextToAudioPipeline):.
    * `"token-classification"` (alias `"ner"` available): will return a [TokenClassificationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.TokenClassificationPipeline).
    * `"video-classification"`: will return a [VideoClassificationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.VideoClassificationPipeline).
    * `"zero-shot-classification"`: will return a [ZeroShotClassificationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.ZeroShotClassificationPipeline).
    * `"zero-shot-image-classification"`: will return a [ZeroShotImageClassificationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.ZeroShotImageClassificationPipeline).
    * `"zero-shot-audio-classification"`: will return a [ZeroShotAudioClassificationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.ZeroShotAudioClassificationPipeline).
    * `"zero-shot-object-detection"`: will return a [ZeroShotObjectDetectionPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.ZeroShotObjectDetectionPipeline).
  * [](#transformers.pipeline.model) **model** (`str` or [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel), _optional_) -- The model that will be used by the pipeline to make predictions. This can be a model identifier or an actual instance of a pretrained model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).

If not provided, the default for the `task` will be loaded.
  * [](#transformers.pipeline.config) **config** (`str` or [PreTrainedConfig](/docs/transformers/v5.8.0/en/main_classes/configuration#transformers.PreTrainedConfig), _optional_) -- The configuration that will be used by the pipeline to instantiate the model. This can be a model identifier or an actual pretrained model configuration inheriting from [PreTrainedConfig](/docs/transformers/v5.8.0/en/main_classes/configuration#transformers.PreTrainedConfig).

If not provided, the default configuration file for the requested model will be used. That means that if `model` is given, its default configuration will be used. However, if `model` is not supplied, this `task`'s default model's config is used instead.
  * [](#transformers.pipeline.tokenizer) **tokenizer** (`str` or [PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend), _optional_) -- The tokenizer that will be used by the pipeline to encode data for the model. This can be a model identifier or an actual pretrained tokenizer inheriting from [PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend).

If not provided, the default tokenizer for the given `model` will be loaded (if it is a string). If `model` is not specified or not a string, then the default tokenizer for `config` is loaded (if it is a string). However, if `config` is also not given or not a string, then the default tokenizer for the given `task` will be loaded.
  * [](#transformers.pipeline.feature_extractor) **feature_extractor** (`str` or [FeatureExtractionMixin](/docs/transformers/v5.8.0/en/main_classes/feature_extractor#transformers.FeatureExtractionMixin), _optional_) -- The feature extractor that will be used by the pipeline to encode data for the model. This can be a model identifier or an actual pretrained feature extractor inheriting from [FeatureExtractionMixin](/docs/transformers/v5.8.0/en/main_classes/feature_extractor#transformers.FeatureExtractionMixin).

Feature extractors are used for non-NLP models, such as Speech or Vision models as well as multi-modal models. Multi-modal models will also require a tokenizer to be passed.

If not provided, the default feature extractor for the given `model` will be loaded (if it is a string). If `model` is not specified or not a string, then the default feature extractor for `config` is loaded (if it is a string). However, if `config` is also not given or not a string, then the default feature extractor for the given `task` will be loaded.
  * [](#transformers.pipeline.image_processor) **image_processor** (`str` or [BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor), _optional_) -- The image processor that will be used by the pipeline to preprocess images for the model. This can be a model identifier or an actual image processor inheriting from [BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor).

Image processors are used for Vision models and multi-modal models that require image inputs. Multi-modal models will also require a tokenizer to be passed.

If not provided, the default image processor for the given `model` will be loaded (if it is a string). If `model` is not specified or not a string, then the default image processor for `config` is loaded (if it is a string).
  * [](#transformers.pipeline.processor) **processor** (`str` or [ProcessorMixin](/docs/transformers/v5.8.0/en/main_classes/processors#transformers.ProcessorMixin), _optional_) -- The processor that will be used by the pipeline to preprocess data for the model. This can be a model identifier or an actual processor inheriting from [ProcessorMixin](/docs/transformers/v5.8.0/en/main_classes/processors#transformers.ProcessorMixin).

Processors are used for multi-modal models that require multi-modal inputs, for example, a model that requires both text and image inputs.

If not provided, the default processor for the given `model` will be loaded (if it is a string). If `model` is not specified or not a string, then the default processor for `config` is loaded (if it is a string).
  * [](#transformers.pipeline.revision) **revision** (`str`, _optional_ , defaults to `"main"`) -- When passing a task name or a string model identifier: The specific model version to use. It can be a branch name, a tag name, or a commit id, since we use a git-based system for storing models and other artifacts on huggingface.co, so `revision` can be any identifier allowed by git.
  * [](#transformers.pipeline.use_fast) **use_fast** (`bool`, _optional_ , defaults to `True`) -- Whether or not to use a Fast tokenizer if possible (a [PreTrainedTokenizerFast](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.TokenizersBackend)).
  * [](#transformers.pipeline.token) **token** (`str` or _bool_ , _optional_) -- The token to use as HTTP bearer authorization for remote files. If `True`, will use the token generated when running `hf auth login`.
  * [](#transformers.pipeline.device) **device** (`int` or `str` or `torch.device`) -- Defines the device (_e.g._ , `"cpu"`, `"cuda:1"`, `"mps"`, or a GPU ordinal rank like `1`) on which this pipeline will be allocated.
  * [](#transformers.pipeline.device_map) **device_map** (`str` or `dict[str, Union[int, str, torch.device]`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut). When `accelerate` library is present, set `device_map="auto"` to compute the most optimized `device_map` automatically (see [here](https://huggingface.co/docs/accelerate/main/en/package_reference/big_modeling#accelerate.cpu_offload) for more information).

Do not use `device_map` AND `device` at the same time as they will conflict

  * [](#transformers.pipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`).
  * [](#transformers.pipeline.trust_remote_code) **trust_remote_code** (`bool`, _optional_ , defaults to `False`) -- Whether or not to allow for custom code defined on the Hub in their own modeling, configuration, tokenization or even pipeline files. This option should only be set to `True` for repositories you trust and in which you have read the code, as it will execute code present on the Hub on your local machine.
  * [](#transformers.pipeline.model_kwargs) **model_kwargs** (`dict[str, Any]`, _optional_) -- Additional dictionary of keyword arguments passed along to the model's `from_pretrained(..., **model_kwargs)` function.
  * [](#transformers.pipeline.kwargs) **kwargs** (`dict[str, Any]`, _optional_) -- Additional keyword arguments passed along to the specific pipeline init (see the documentation for the corresponding pipeline class for possible values).

Returns

[Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline)

A suitable pipeline for the task.

Utility factory method to build a [Pipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.Pipeline).

A pipeline consists of:

  * One or more components for pre-processing model inputs, such as a [tokenizer](tokenizer), [image_processor](image_processor), [feature_extractor](feature_extractor), or [processor](processors).
  * A [model](model) that generates predictions from the inputs.
  * Optional post-processing steps to refine the model’s output, which can also be handled by processors.

> While there are such optional arguments as `tokenizer`, `feature_extractor`, `image_processor`, and `processor`, they shouldn't be specified all at once. If these components are not provided, `pipeline` will try to load required ones automatically. In case you want to provide these components explicitly, please refer to a specific pipeline in order to get more details regarding what components are required.

[](#transformers.pipeline.example)

Examples:

Copied


    >>> from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer

    >>> # Sentiment analysis pipeline
    >>> analyzer = pipeline("sentiment-analysis")

    >>> # Named entity recognition pipeline, passing in a specific model and tokenizer
    >>> model = AutoModelForTokenClassification.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english")
    >>> tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-cased")
    >>> recognizer = pipeline("ner", model=model, tokenizer=tokenizer)

## [](#pipeline-batching) Pipeline batching

All pipelines can use batching. This will work whenever the pipeline uses its streaming ability (so when passing lists or `Dataset` or `generator`).

Copied


    from transformers import pipeline
    from transformers.pipelines.pt_utils import KeyDataset
    import datasets

    dataset = datasets.load_dataset("imdb", name="plain_text", split="unsupervised")
    pipe = pipeline("text-classification", device=0)
    for out in pipe(KeyDataset(dataset, "text"), batch_size=8, truncation="only_first"):
        print(out)
        # [{'label': 'POSITIVE', 'score': 0.9998743534088135}]
        # Exactly the same output as before, but the content are passed
        # as batches to the model

> However, this is not automatically a win for performance. It can be either a 10x speedup or 5x slowdown depending on hardware, data and the actual model being used.
>
> Example where it’s mostly a speedup:

Copied


    from transformers import pipeline
    from torch.utils.data import Dataset
    from tqdm.auto import tqdm

    pipe = pipeline("text-classification", device=0)


    class MyDataset(Dataset):
        def __len__(self):
            return 5000

        def __getitem__(self, i):
            return "This is a test"


    dataset = MyDataset()

    for batch_size in [1, 8, 64, 256]:
        print("-" * 30)
        print(f"Streaming batch_size={batch_size}")
        for out in tqdm(pipe(dataset, batch_size=batch_size), total=len(dataset)):
            pass

Copied


    # On GTX 970
    ------------------------------
    Streaming no batching
    100%|██████████████████████████████████████████████████████████████████████| 5000/5000 [00:26<00:00, 187.52it/s]
    ------------------------------
    Streaming batch_size=8
    100%|█████████████████████████████████████████████████████████████████████| 5000/5000 [00:04<00:00, 1205.95it/s]
    ------------------------------
    Streaming batch_size=64
    100%|█████████████████████████████████████████████████████████████████████| 5000/5000 [00:02<00:00, 2478.24it/s]
    ------------------------------
    Streaming batch_size=256
    100%|█████████████████████████████████████████████████████████████████████| 5000/5000 [00:01<00:00, 2554.43it/s]
    (diminishing returns, saturated the GPU)

Example where it’s most a slowdown:

Copied


    class MyDataset(Dataset):
        def __len__(self):
            return 5000

        def __getitem__(self, i):
            if i % 64 == 0:
                n = 100
            else:
                n = 1
            return "This is a test" * n

This is a occasional very long sentence compared to the other. In that case, the **whole** batch will need to be 400 tokens long, so the whole batch will be [64, 400] instead of [64, 4], leading to the high slowdown. Even worse, on bigger batches, the program simply crashes.

Copied


    ------------------------------
    Streaming no batching
    100%|█████████████████████████████████████████████████████████████████████| 1000/1000 [00:05<00:00, 183.69it/s]
    ------------------------------
    Streaming batch_size=8
    100%|█████████████████████████████████████████████████████████████████████| 1000/1000 [00:03<00:00, 265.74it/s]
    ------------------------------
    Streaming batch_size=64
    100%|██████████████████████████████████████████████████████████████████████| 1000/1000 [00:26<00:00, 37.80it/s]
    ------------------------------
    Streaming batch_size=256
      0%|                                                                                 | 0/1000 [00:00<?, ?it/s]
    Traceback (most recent call last):
      File "/home/nicolas/src/transformers/test.py", line 42, in <module>
        for out in tqdm(pipe(dataset, batch_size=256), total=len(dataset)):
    ....
        q = q / math.sqrt(dim_per_head)  # (bs, n_heads, q_length, dim_per_head)
    RuntimeError: CUDA out of memory. Tried to allocate 376.00 MiB (GPU 0; 3.95 GiB total capacity; 1.72 GiB already allocated; 354.88 MiB free; 2.46 GiB reserved in total by PyTorch)

There are no good (general) solutions for this problem, and your mileage may vary depending on your use cases. Rule of thumb:

For users, a rule of thumb is:

  * **Measure performance on your load, with your hardware. Measure, measure, and keep measuring. Real numbers are the only way to go.**

  * If you are latency constrained (live product doing inference), don’t batch.

  * If you are using CPU, don’t batch.

  * If you are using throughput (you want to run your model on a bunch of static data), on GPU, then:

    * If you have no clue about the size of the sequence_length (“natural” data), by default don’t batch, measure and try tentatively to add it, add OOM checks to recover when it will fail (and it will at some point if you don’t control the sequence_length.)
    * If your sequence_length is super regular, then batching is more likely to be VERY interesting, measure and push it until you get OOMs.
    * The larger the GPU the more likely batching is going to be more interesting
  * As soon as you enable batching, make sure you can handle OOMs nicely.

## [](#pipeline-chunk-batching) Pipeline chunk batching

`zero-shot-classification` and `question-answering` are slightly specific in the sense, that a single input might yield multiple forward pass of a model. Under normal circumstances, this would yield issues with `batch_size` argument.

In order to circumvent this issue, both of these pipelines are a bit specific, they are `ChunkPipeline` instead of regular `Pipeline`. In short:

Copied


    preprocessed = pipe.preprocess(inputs)
    model_outputs = pipe.forward(preprocessed)
    outputs = pipe.postprocess(model_outputs)

Now becomes:

Copied


    all_model_outputs = []
    for preprocessed in pipe.preprocess(inputs):
        model_outputs = pipe.forward(preprocessed)
        all_model_outputs.append(model_outputs)
    outputs = pipe.postprocess(all_model_outputs)

This should be very transparent to your code because the pipelines are used in the same way.

This is a simplified view, since the pipeline can handle automatically the batch to ! Meaning you don’t have to care about how many forward passes you inputs are actually going to trigger, you can optimize the `batch_size` independently of the inputs. The caveats from the previous section still apply.

## [](#pipeline-fp16-inference) Pipeline FP16 inference

Models can be run in FP16 which can be significantly faster on GPU while saving memory. Most models will not suffer noticeable performance loss from this. The larger the model, the less likely that it will.

To enable FP16 inference, you can simply pass `dtype=torch.float16` or `dtype='float16'` to the pipeline constructor. Note that this only works for models with a PyTorch backend. Your inputs will be converted to FP16 internally.

## [](#pipeline-custom-code) Pipeline custom code

If you want to override a specific pipeline.

Don’t hesitate to create an issue for your task at hand, the goal of the pipeline is to be easy to use and support most cases, so `transformers` could maybe support your use case.

If you want to try simply you can:

  * Subclass your pipeline of choice

Copied


    class MyPipeline(TextClassificationPipeline):
        def postprocess():
            # Your code goes here
            scores = scores * 100
            # And here


    my_pipeline = MyPipeline(model=model, tokenizer=tokenizer, ...)
    # or if you use *pipeline* function, then:
    my_pipeline = pipeline(model="xxxx", pipeline_class=MyPipeline)

That should enable you to do all the custom code you want.

## [](#implementing-a-pipeline) Implementing a pipeline

[Implementing a new pipeline](../add_new_pipeline)

## [](#audio) Audio

Pipelines available for audio tasks include the following.

### [](#transformers.AudioClassificationPipeline) AudioClassificationPipeline

### class transformers.AudioClassificationPipeline

[](#transformers.AudioClassificationPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/audio_classification.py#L67)

( *args **kwargs )

Parameters

  * [](#transformers.AudioClassificationPipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.AudioClassificationPipeline.feature_extractor) **feature_extractor** ([SequenceFeatureExtractor](/docs/transformers/v5.8.0/en/main_classes/feature_extractor#transformers.SequenceFeatureExtractor)) -- The feature extractor that will be used by the pipeline to encode data for the model. This object inherits from [SequenceFeatureExtractor](/docs/transformers/v5.8.0/en/main_classes/feature_extractor#transformers.SequenceFeatureExtractor).
  * [](#transformers.AudioClassificationPipeline.task) **task** (`str`, defaults to `""`) -- A task-identifier for the pipeline.
  * [](#transformers.AudioClassificationPipeline.num_workers) **num_workers** (`int`, _optional_ , defaults to 8) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the number of workers to be used.
  * [](#transformers.AudioClassificationPipeline.batch_size) **batch_size** (`int`, _optional_ , defaults to 1) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the size of the batch to use, for inference this is not always beneficial, please read [Batching with pipelines](https://huggingface.co/transformers/main_classes/pipelines.html#pipeline-batching) .
  * [](#transformers.AudioClassificationPipeline.args_parser) **args_parser** ([ArgumentHandler](/docs/transformers/v5.8.0/en/internal/pipelines_utils#transformers.pipelines.ArgumentHandler), _optional_) -- Reference to the object in charge of parsing supplied pipeline parameters.
  * [](#transformers.AudioClassificationPipeline.device) **device** (`int`, _optional_ , defaults to -1) -- Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on the associated CUDA device id. You can pass native `torch.device` or a `str` too
  * [](#transformers.AudioClassificationPipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`)
  * [](#transformers.AudioClassificationPipeline.binary_output) **binary_output** (`bool`, _optional_ , defaults to `False`) -- Flag indicating if the output the pipeline should happen in a serialized format (i.e., pickle) or as the raw output data e.g. text.

Audio classification pipeline using any `AutoModelForAudioClassification`. This pipeline predicts the class of a raw waveform or an audio file. In case of an audio file, ffmpeg should be installed to support multiple audio formats.

[](#transformers.AudioClassificationPipeline.example)

Example:

Copied


    >>> from transformers import pipeline

    >>> classifier = pipeline(model="superb/wav2vec2-base-superb-ks")
    >>> classifier("https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/1.flac")
    [{'score': 0.997, 'label': '_unknown_'}, {'score': 0.002, 'label': 'left'}, {'score': 0.0, 'label': 'yes'}, {'score': 0.0, 'label': 'down'}, {'score': 0.0, 'label': 'stop'}]

Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

This pipeline can currently be loaded from [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) using the following task identifier: `"audio-classification"`.

See the list of available models on [huggingface.co/models](https://huggingface.co/models?filter=audio-classification).

#### __call__

[](#transformers.AudioClassificationPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/audio_classification.py#L109)

( inputs: numpy.ndarray | bytes | str | dict **kwargs: typing.Any ) → A list of `dict` with the following keys

Parameters

  * [](#transformers.AudioClassificationPipeline.__call__.inputs) **inputs** (`np.ndarray` or `bytes` or `str` or `dict`) -- The inputs is either :
    * `str` that is the filename of the audio file, the file will be read at the correct sampling rate to get the waveform using _ffmpeg_. This requires _ffmpeg_ to be installed on the system.
    * `bytes` it is supposed to be the content of an audio file and is interpreted by _ffmpeg_ in the same way.
    * (`np.ndarray` of shape (n, ) of type `np.float32` or `np.float64`) Raw audio at the correct sampling rate (no further check will be done)
    * `dict` form can be used to pass raw audio sampled at arbitrary `sampling_rate` and let this pipeline do the resampling. The dict must be either be in the format `{"sampling_rate": int, "raw": np.array}`, or `{"sampling_rate": int, "array": np.array}`, where the key `"raw"` or `"array"` is used to denote the raw audio waveform.
  * [](#transformers.AudioClassificationPipeline.__call__.top_k) **top_k** (`int`, _optional_ , defaults to None) -- The number of top labels that will be returned by the pipeline. If the provided number is `None` or higher than the number of labels available in the model configuration, it will default to the number of labels.
  * [](#transformers.AudioClassificationPipeline.__call__.function_to_apply) **function_to_apply** (`str`, _optional_ , defaults to "softmax") -- The function to apply to the model output. By default, the pipeline will apply the softmax function to the output of the model. Valid options: ["softmax", "sigmoid", "none"]. Note that passing Python's built-in `None` will default to "softmax", so you need to pass the string "none" to disable any post-processing.

Returns

A list of `dict` with the following keys

  * **label** (`str`) — The label predicted.
  * **score** (`float`) — The corresponding probability.

Classify the sequence(s) given as inputs. See the [AutomaticSpeechRecognitionPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.AutomaticSpeechRecognitionPipeline) documentation for more information.

### [](#transformers.AutomaticSpeechRecognitionPipeline) AutomaticSpeechRecognitionPipeline

### class transformers.AutomaticSpeechRecognitionPipeline

[](#transformers.AutomaticSpeechRecognitionPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/automatic_speech_recognition.py#L112)

( model: PreTrainedModel feature_extractor: typing.Union[ForwardRef('SequenceFeatureExtractor'), str, NoneType] = None tokenizer: transformers.tokenization_python.PythonBackend | None = None decoder: typing.Union[ForwardRef('BeamSearchDecoderCTC'), str, NoneType] = None device: typing.Union[int, ForwardRef('torch.device'), NoneType] = None **kwargs )

Parameters

  * [](#transformers.AutomaticSpeechRecognitionPipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.AutomaticSpeechRecognitionPipeline.feature_extractor) **feature_extractor** ([SequenceFeatureExtractor](/docs/transformers/v5.8.0/en/main_classes/feature_extractor#transformers.SequenceFeatureExtractor), _optional_) -- The feature extractor that will be used by the pipeline to encode waveform for the model.
  * [](#transformers.AutomaticSpeechRecognitionPipeline.tokenizer) **tokenizer** ([PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend), _optional_) -- The tokenizer that will be used by the pipeline to encode data for the model. This object inherits from [PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend).
  * [](#transformers.AutomaticSpeechRecognitionPipeline.decoder) **decoder** (`pyctcdecode.BeamSearchDecoderCTC`, _optional_) -- [PyCTCDecode's BeamSearchDecoderCTC](https://github.com/kensho-technologies/pyctcdecode/blob/2fd33dc37c4111417e08d89ccd23d28e9b308d19/pyctcdecode/decoder.py#L180) can be passed for language model boosted decoding. See [Wav2Vec2ProcessorWithLM](/docs/transformers/v5.8.0/en/model_doc/wav2vec2#transformers.Wav2Vec2ProcessorWithLM) for more information.
  * [](#transformers.AutomaticSpeechRecognitionPipeline.device) **device** (Union[`int`, `torch.device`], _optional_) -- Device ordinal for CPU/GPU supports. Setting this to `None` will leverage CPU, a positive will run the model on the associated CUDA device id.

Pipeline that aims at extracting spoken text contained within some audio.

The input can be either a raw waveform or a audio file. In case of the audio file, ffmpeg should be installed for to support multiple audio formats

Unless the model you’re using explicitly sets these generation parameters in its configuration files (`generation_config.json`), the following default values will be used:

  * max_new_tokens: 256
  * num_beams: 5

[](#transformers.AutomaticSpeechRecognitionPipeline.example)

Example:

Copied


    >>> from transformers import pipeline

    >>> transcriber = pipeline(model="openai/whisper-base")
    >>> transcriber("https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/1.flac")
    {'text': ' He hoped there would be stew for dinner, turnips and carrots and bruised potatoes and fat mutton pieces to be ladled out in thick, peppered flour-fatten sauce.'}

Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

#### __call__

[](#transformers.AutomaticSpeechRecognitionPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/automatic_speech_recognition.py#L187)

( inputs: numpy.ndarray | bytes | str | dict **kwargs: typing.Any ) → `Dict`

Parameters

  * [](#transformers.AutomaticSpeechRecognitionPipeline.__call__.inputs) **inputs** (`np.ndarray` or `bytes` or `str` or `dict`) -- The inputs is either :

    * `str` that is either the filename of a local audio file, or a public URL address to download the audio file. The file will be read at the correct sampling rate to get the waveform using _ffmpeg_. This requires _ffmpeg_ to be installed on the system.
    * `bytes` it is supposed to be the content of an audio file and is interpreted by _ffmpeg_ in the same way.
    * (`np.ndarray` of shape (n, ) of type `np.float32` or `np.float64`) Raw audio at the correct sampling rate (no further check will be done)
    * `dict` form can be used to pass raw audio sampled at arbitrary `sampling_rate` and let this pipeline do the resampling. The dict must be in the format `{"sampling_rate": int, "raw": np.array}` with optionally a `"stride": (left: int, right: int)` than can ask the pipeline to treat the first `left` samples and last `right` samples to be ignored in decoding (but used at inference to provide more context to the model). Only use `stride` with CTC models.
  * [](#transformers.AutomaticSpeechRecognitionPipeline.__call__.return_timestamps) **return_timestamps** (_optional_ , `str` or `bool`) -- Only available for pure CTC models (Wav2Vec2, HuBERT, etc) and the Whisper model. Not available for other sequence-to-sequence models.

For CTC models, timestamps can take one of two formats:

    * `"char"`: the pipeline will return timestamps along the text for every character in the text. For instance, if you get `[{"text": "h", "timestamp": (0.5, 0.6)}, {"text": "i", "timestamp": (0.7, 0.9)}]`, then it means the model predicts that the letter "h" was spoken after `0.5` and before `0.6` seconds.
    * `"word"`: the pipeline will return timestamps along the text for every word in the text. For instance, if you get `[{"text": "hi ", "timestamp": (0.5, 0.9)}, {"text": "there", "timestamp": (1.0, 1.5)}]`, then it means the model predicts that the word "hi" was spoken after `0.5` and before `0.9` seconds.

For the Whisper model, timestamps can take one of two formats:

    * `"word"`: same as above for word-level CTC timestamps. Word-level timestamps are predicted through the _dynamic-time warping (DTW)_ algorithm, an approximation to word-level timestamps by inspecting the cross-attention weights.
    * `True`: the pipeline will return timestamps along the text for _segments_ of words in the text. For instance, if you get `[{"text": " Hi there!", "timestamp": (0.5, 1.5)}]`, then it means the model predicts that the segment "Hi there!" was spoken after `0.5` and before `1.5` seconds. Note that a segment of text refers to a sequence of one or more words, rather than individual words as with word-level timestamps.
  * [](#transformers.AutomaticSpeechRecognitionPipeline.__call__.generate_kwargs) **generate_kwargs** (`dict`, _optional_) -- The dictionary of ad-hoc parametrization of `generate_config` to be used for the generation call. For a complete overview of generate, check the [following guide](https://huggingface.co/docs/transformers/en/main_classes/text_generation).

Returns

`Dict`

A dictionary with the following keys:

  * **text** (`str`): The recognized text.
  * **chunks** (_optional(,`list[Dict]`) When using `return_timestamps`, the `chunks` will become a list containing all the various text chunks identified by the model, _e.g.* `[{"text": "hi ", "timestamp": (0.5, 0.9)}, {"text": "there", "timestamp": (1.0, 1.5)}]`. The original full text can roughly be recovered by doing `"".join(chunk["text"] for chunk in output["chunks"])`.

Transcribe the audio sequence(s) given as inputs to text. See the [AutomaticSpeechRecognitionPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.AutomaticSpeechRecognitionPipeline) documentation for more information.

### [](#transformers.TextToAudioPipeline) TextToAudioPipeline

### class transformers.TextToAudioPipeline

[](#transformers.TextToAudioPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/text_to_audio.py#L45)

( *args vocoder = None sampling_rate = None **kwargs )

Text-to-audio generation pipeline using any `AutoModelForTextToWaveform` or `AutoModelForTextToSpectrogram`. This pipeline generates an audio file from an input text and optional other conditional inputs.

Unless the model you’re using explicitly sets these generation parameters in its configuration files (`generation_config.json`), the following default values will be used:

  * max_new_tokens: 256

[](#transformers.TextToAudioPipeline.example)

Example:

Copied


    >>> from transformers import pipeline

    >>> pipe = pipeline(model="suno/bark-small")
    >>> output = pipe("Hey it's HuggingFace on the phone!")

    >>> audio = output["audio"]
    >>> sampling_rate = output["sampling_rate"]

Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

> You can specify parameters passed to the model by using `TextToAudioPipeline.__call__.forward_params` or `TextToAudioPipeline.__call__.generate_kwargs`.
>
> [](#transformers.TextToAudioPipeline.example-2)
>
> Example:
>
> Copied
>
>
>     >>> from transformers import pipeline
>
>     >>> music_generator = pipeline(task="text-to-audio", model="facebook/musicgen-small")
>
>     >>> # diversify the music generation by adding randomness with a high temperature and set a maximum music length
>     >>> generate_kwargs = {
>     ...     "do_sample": True,
>     ...     "temperature": 0.7,
>     ...     "max_new_tokens": 35,
>     ... }
>
>     >>> outputs = music_generator("Techno music with high melodic riffs", generate_kwargs=generate_kwargs)

This pipeline can currently be loaded from [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) using the following task identifiers: `"text-to-speech"` or `"text-to-audio"`.

See the list of available models on [huggingface.co/models](https://huggingface.co/models?filter=text-to-speech).

#### __call__

[](#transformers.TextToAudioPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/text_to_audio.py#L243)

( text_inputs **forward_params ) → `AudioOutput` or a list of `AudioOutput`, which is a `TypedDict` with two keys

Parameters

  * [](#transformers.TextToAudioPipeline.__call__.text_inputs) **text_inputs** (`str`, `list[str]`, `ChatType`, or `list[ChatType]`) -- One or several texts to generate. If strings or a list of string are passed, this pipeline will generate the corresponding text. Alternatively, a "chat", in the form of a list of dicts with "role" and "content" keys, can be passed, or a list of such chats. When chats are passed, the model's chat template will be used to format them before passing them to the model.
  * [](#transformers.TextToAudioPipeline.__call__.forward_params) **forward_params** (`dict`, _optional_) -- Parameters passed to the model generation/forward method. `forward_params` are always passed to the underlying model.
  * [](#transformers.TextToAudioPipeline.__call__.generate_kwargs) **generate_kwargs** (`dict`, _optional_) -- The dictionary of ad-hoc parametrization of `generate_config` to be used for the generation call. For a complete overview of generate, check the [following guide](https://huggingface.co/docs/transformers/en/main_classes/text_generation). `generate_kwargs` are only passed to the underlying model if the latter is a generative model.

Returns

`AudioOutput` or a list of `AudioOutput`, which is a `TypedDict` with two keys

  * **audio** (`np.ndarray` of shape `(nb_channels, audio_length)`) — The generated audio waveform.
  * **sampling_rate** (`int`) — The sampling rate of the generated audio waveform.

Generates speech/audio from the inputs. See the [TextToAudioPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.TextToAudioPipeline) documentation for more information.

### [](#transformers.ZeroShotAudioClassificationPipeline) ZeroShotAudioClassificationPipeline

### class transformers.ZeroShotAudioClassificationPipeline

[](#transformers.ZeroShotAudioClassificationPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/zero_shot_audio_classification.py#L32)

( **kwargs )

Parameters

  * [](#transformers.ZeroShotAudioClassificationPipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.ZeroShotAudioClassificationPipeline.tokenizer) **tokenizer** ([PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend)) -- The tokenizer that will be used by the pipeline to encode data for the model. This object inherits from [PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend).
  * [](#transformers.ZeroShotAudioClassificationPipeline.feature_extractor) **feature_extractor** ([SequenceFeatureExtractor](/docs/transformers/v5.8.0/en/main_classes/feature_extractor#transformers.SequenceFeatureExtractor)) -- The feature extractor that will be used by the pipeline to encode data for the model. This object inherits from [SequenceFeatureExtractor](/docs/transformers/v5.8.0/en/main_classes/feature_extractor#transformers.SequenceFeatureExtractor).
  * [](#transformers.ZeroShotAudioClassificationPipeline.task) **task** (`str`, defaults to `""`) -- A task-identifier for the pipeline.
  * [](#transformers.ZeroShotAudioClassificationPipeline.num_workers) **num_workers** (`int`, _optional_ , defaults to 8) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the number of workers to be used.
  * [](#transformers.ZeroShotAudioClassificationPipeline.batch_size) **batch_size** (`int`, _optional_ , defaults to 1) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the size of the batch to use, for inference this is not always beneficial, please read [Batching with pipelines](https://huggingface.co/transformers/main_classes/pipelines.html#pipeline-batching) .
  * [](#transformers.ZeroShotAudioClassificationPipeline.args_parser) **args_parser** ([ArgumentHandler](/docs/transformers/v5.8.0/en/internal/pipelines_utils#transformers.pipelines.ArgumentHandler), _optional_) -- Reference to the object in charge of parsing supplied pipeline parameters.
  * [](#transformers.ZeroShotAudioClassificationPipeline.device) **device** (`int`, _optional_ , defaults to -1) -- Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on the associated CUDA device id. You can pass native `torch.device` or a `str` too
  * [](#transformers.ZeroShotAudioClassificationPipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`)
  * [](#transformers.ZeroShotAudioClassificationPipeline.binary_output) **binary_output** (`bool`, _optional_ , defaults to `False`) -- Flag indicating if the output the pipeline should happen in a serialized format (i.e., pickle) or as the raw output data e.g. text.

Zero shot audio classification pipeline using `ClapModel`. This pipeline predicts the class of an audio when you provide an audio and a set of `candidate_labels`.

> The default `hypothesis_template` is : `"This is a sound of {}."`. Make sure you update it for your usage.

[](#transformers.ZeroShotAudioClassificationPipeline.example)

Example:

Copied


    >>> from transformers import pipeline
    >>> from datasets import load_dataset

    >>> dataset = load_dataset("ashraq/esc50")
    >>> audio = next(iter(dataset["train"]["audio"]))["array"]
    >>> classifier = pipeline(task="zero-shot-audio-classification", model="laion/clap-htsat-unfused")
    >>> classifier(audio, candidate_labels=["Sound of a dog", "Sound of vacuum cleaner"])
    [{'score': 0.9996, 'label': 'Sound of a dog'}, {'score': 0.0004, 'label': 'Sound of vacuum cleaner'}]

Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial) This audio classification pipeline can currently be loaded from [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) using the following task identifier: `"zero-shot-audio-classification"`. See the list of available models on [huggingface.co/models](https://huggingface.co/models?filter=zero-shot-audio-classification).

#### __call__

[](#transformers.ZeroShotAudioClassificationPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/zero_shot_audio_classification.py#L70)

( audios: numpy.ndarray | bytes | str | dict **kwargs: typing.Any )

Parameters

  * [](#transformers.ZeroShotAudioClassificationPipeline.__call__.audios) **audios** (`str`, `list[str]`, `np.array` or `list[np.array]`) -- The pipeline handles three types of inputs:
    * A string containing a http link pointing to an audio
    * A string containing a local path to an audio
    * An audio loaded in numpy
  * [](#transformers.ZeroShotAudioClassificationPipeline.__call__.candidate_labels) **candidate_labels** (`list[str]`) -- The candidate labels for this audio. They will be formatted using _hypothesis_template_.
  * [](#transformers.ZeroShotAudioClassificationPipeline.__call__.hypothesis_template) **hypothesis_template** (`str`, _optional_ , defaults to `"This is a sound of {}"`) -- The format used in conjunction with _candidate_labels_ to attempt the audio classification by replacing the placeholder with the candidate_labels. Pass "{}" if _candidate_labels_ are already formatted.

Assign labels to the audio(s) passed as inputs.

## [](#computer-vision) Computer vision

Pipelines available for computer vision tasks include the following.

### [](#transformers.DepthEstimationPipeline) DepthEstimationPipeline

### class transformers.DepthEstimationPipeline

[](#transformers.DepthEstimationPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/depth_estimation.py#L25)

( *args **kwargs )

Parameters

  * [](#transformers.DepthEstimationPipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.DepthEstimationPipeline.image_processor) **image_processor** ([BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor)) -- The image processor that will be used by the pipeline to encode data for the model. This object inherits from [BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor).
  * [](#transformers.DepthEstimationPipeline.task) **task** (`str`, defaults to `""`) -- A task-identifier for the pipeline.
  * [](#transformers.DepthEstimationPipeline.num_workers) **num_workers** (`int`, _optional_ , defaults to 8) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the number of workers to be used.
  * [](#transformers.DepthEstimationPipeline.batch_size) **batch_size** (`int`, _optional_ , defaults to 1) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the size of the batch to use, for inference this is not always beneficial, please read [Batching with pipelines](https://huggingface.co/transformers/main_classes/pipelines.html#pipeline-batching) .
  * [](#transformers.DepthEstimationPipeline.args_parser) **args_parser** ([ArgumentHandler](/docs/transformers/v5.8.0/en/internal/pipelines_utils#transformers.pipelines.ArgumentHandler), _optional_) -- Reference to the object in charge of parsing supplied pipeline parameters.
  * [](#transformers.DepthEstimationPipeline.device) **device** (`int`, _optional_ , defaults to -1) -- Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on the associated CUDA device id. You can pass native `torch.device` or a `str` too
  * [](#transformers.DepthEstimationPipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`)
  * [](#transformers.DepthEstimationPipeline.binary_output) **binary_output** (`bool`, _optional_ , defaults to `False`) -- Flag indicating if the output the pipeline should happen in a serialized format (i.e., pickle) or as the raw output data e.g. text.

Depth estimation pipeline using any `AutoModelForDepthEstimation`. This pipeline predicts the depth of an image.

[](#transformers.DepthEstimationPipeline.example)

Example:

Copied


    >>> from transformers import pipeline

    >>> depth_estimator = pipeline(task="depth-estimation", model="LiheYoung/depth-anything-base-hf")
    >>> output = depth_estimator("http://images.cocodataset.org/val2017/000000039769.jpg")
    >>> # This is a tensor with the values being the depth expressed in meters for each pixel
    >>> output["predicted_depth"].shape
    torch.Size([1, 384, 384])

Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

This depth estimation pipeline can currently be loaded from [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) using the following task identifier: `"depth-estimation"`.

See the list of available models on [huggingface.co/models](https://huggingface.co/models?filter=depth-estimation).

#### __call__

[](#transformers.DepthEstimationPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/depth_estimation.py#L66)

( inputs: typing.Union[str, list[str], ForwardRef('Image.Image'), list['Image.Image']] **kwargs: typing.Any )

Parameters

  * [](#transformers.DepthEstimationPipeline.__call__.inputs) **inputs** (`str`, `list[str]`, `PIL.Image` or `list[PIL.Image]`) -- The pipeline handles three types of images:

    * A string containing a http link pointing to an image
    * A string containing a local path to an image
    * An image loaded in PIL directly

The pipeline accepts either a single image or a batch of images, which must then be passed as a string. Images in a batch must all be in the same format: all as http links, all as local paths, or all as PIL images.
  * [](#transformers.DepthEstimationPipeline.__call__.parameters) **parameters** (`Dict`, _optional_) -- A dictionary of argument names to parameter values, to control pipeline behaviour. The only parameter available right now is `timeout`, which is the length of time, in seconds, that the pipeline should wait before giving up on trying to download an image.
  * [](#transformers.DepthEstimationPipeline.__call__.timeout) **timeout** (`float`, _optional_ , defaults to None) -- The maximum time in seconds to wait for fetching images from the web. If None, no timeout is set and the call may block forever.

Predict the depth(s) of the image(s) passed as inputs.

### [](#transformers.ImageClassificationPipeline) ImageClassificationPipeline

### class transformers.ImageClassificationPipeline

[](#transformers.ImageClassificationPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/image_classification.py#L73)

( *args **kwargs )

Parameters

  * [](#transformers.ImageClassificationPipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.ImageClassificationPipeline.image_processor) **image_processor** ([BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor)) -- The image processor that will be used by the pipeline to encode data for the model. This object inherits from [BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor).
  * [](#transformers.ImageClassificationPipeline.task) **task** (`str`, defaults to `""`) -- A task-identifier for the pipeline.
  * [](#transformers.ImageClassificationPipeline.num_workers) **num_workers** (`int`, _optional_ , defaults to 8) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the number of workers to be used.
  * [](#transformers.ImageClassificationPipeline.batch_size) **batch_size** (`int`, _optional_ , defaults to 1) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the size of the batch to use, for inference this is not always beneficial, please read [Batching with pipelines](https://huggingface.co/transformers/main_classes/pipelines.html#pipeline-batching) .
  * [](#transformers.ImageClassificationPipeline.args_parser) **args_parser** ([ArgumentHandler](/docs/transformers/v5.8.0/en/internal/pipelines_utils#transformers.pipelines.ArgumentHandler), _optional_) -- Reference to the object in charge of parsing supplied pipeline parameters.
  * [](#transformers.ImageClassificationPipeline.device) **device** (`int`, _optional_ , defaults to -1) -- Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on the associated CUDA device id. You can pass native `torch.device` or a `str` too
  * [](#transformers.ImageClassificationPipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`)
  * [](#transformers.ImageClassificationPipeline.binary_output) **binary_output** (`bool`, _optional_ , defaults to `False`) -- Flag indicating if the output the pipeline should happen in a serialized format (i.e., pickle) or as the raw output data e.g. text.
  * [](#transformers.ImageClassificationPipeline.function_to_apply) **function_to_apply** (`str`, _optional_ , defaults to `"default"`) -- The function to apply to the model outputs in order to retrieve the scores. Accepts four different values:

    * `"default"`: if the model has a single label, will apply the sigmoid function on the output. If the model has several labels, will apply the softmax function on the output.
    * `"sigmoid"`: Applies the sigmoid function on the output.
    * `"softmax"`: Applies the softmax function on the output.
    * `"none"`: Does not apply any function on the output.

Image classification pipeline using any `AutoModelForImageClassification`. This pipeline predicts the class of an image.

[](#transformers.ImageClassificationPipeline.example)

Example:

Copied


    >>> from transformers import pipeline

    >>> classifier = pipeline(model="microsoft/beit-base-patch16-224-pt22k-ft22k")
    >>> classifier("https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png")
    [{'score': 0.442, 'label': 'macaw'}, {'score': 0.088, 'label': 'popinjay'}, {'score': 0.075, 'label': 'parrot'}, {'score': 0.073, 'label': 'parodist, lampooner'}, {'score': 0.046, 'label': 'poll, poll_parrot'}]

Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

This image classification pipeline can currently be loaded from [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) using the following task identifier: `"image-classification"`.

See the list of available models on [huggingface.co/models](https://huggingface.co/models?filter=image-classification).

#### __call__

[](#transformers.ImageClassificationPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/image_classification.py#L127)

( inputs: typing.Union[str, list[str], ForwardRef('Image.Image'), list['Image.Image']] **kwargs: typing.Any )

Parameters

  * [](#transformers.ImageClassificationPipeline.__call__.inputs) **inputs** (`str`, `list[str]`, `PIL.Image` or `list[PIL.Image]`) -- The pipeline handles three types of images:

    * A string containing a http link pointing to an image
    * A string containing a local path to an image
    * An image loaded in PIL directly

The pipeline accepts either a single image or a batch of images, which must then be passed as a string. Images in a batch must all be in the same format: all as http links, all as local paths, or all as PIL images.
  * [](#transformers.ImageClassificationPipeline.__call__.function_to_apply) **function_to_apply** (`str`, _optional_ , defaults to `"default"`) -- The function to apply to the model outputs in order to retrieve the scores. Accepts four different values:

If this argument is not specified, then it will apply the following functions according to the number of labels:

    * If the model has a single label, will apply the sigmoid function on the output.
    * If the model has several labels, will apply the softmax function on the output.

Possible values are:

    * `"sigmoid"`: Applies the sigmoid function on the output.
    * `"softmax"`: Applies the softmax function on the output.
    * `"none"`: Does not apply any function on the output.
  * [](#transformers.ImageClassificationPipeline.__call__.top_k) **top_k** (`int`, _optional_ , defaults to 5) -- The number of top labels that will be returned by the pipeline. If the provided number is higher than the number of labels available in the model configuration, it will default to the number of labels.
  * [](#transformers.ImageClassificationPipeline.__call__.timeout) **timeout** (`float`, _optional_ , defaults to None) -- The maximum time in seconds to wait for fetching images from the web. If None, no timeout is set and the call may block forever.

Assign labels to the image(s) passed as inputs.

### [](#transformers.ImageSegmentationPipeline) ImageSegmentationPipeline

### class transformers.ImageSegmentationPipeline

[](#transformers.ImageSegmentationPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/image_segmentation.py#L27)

( *args **kwargs )

Parameters

  * [](#transformers.ImageSegmentationPipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.ImageSegmentationPipeline.image_processor) **image_processor** ([BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor)) -- The image processor that will be used by the pipeline to encode data for the model. This object inherits from [BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor).
  * [](#transformers.ImageSegmentationPipeline.task) **task** (`str`, defaults to `""`) -- A task-identifier for the pipeline.
  * [](#transformers.ImageSegmentationPipeline.num_workers) **num_workers** (`int`, _optional_ , defaults to 8) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the number of workers to be used.
  * [](#transformers.ImageSegmentationPipeline.batch_size) **batch_size** (`int`, _optional_ , defaults to 1) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the size of the batch to use, for inference this is not always beneficial, please read [Batching with pipelines](https://huggingface.co/transformers/main_classes/pipelines.html#pipeline-batching) .
  * [](#transformers.ImageSegmentationPipeline.args_parser) **args_parser** ([ArgumentHandler](/docs/transformers/v5.8.0/en/internal/pipelines_utils#transformers.pipelines.ArgumentHandler), _optional_) -- Reference to the object in charge of parsing supplied pipeline parameters.
  * [](#transformers.ImageSegmentationPipeline.device) **device** (`int`, _optional_ , defaults to -1) -- Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on the associated CUDA device id. You can pass native `torch.device` or a `str` too
  * [](#transformers.ImageSegmentationPipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`)
  * [](#transformers.ImageSegmentationPipeline.binary_output) **binary_output** (`bool`, _optional_ , defaults to `False`) -- Flag indicating if the output the pipeline should happen in a serialized format (i.e., pickle) or as the raw output data e.g. text.

Image segmentation pipeline using any `AutoModelForXXXSegmentation`. This pipeline predicts masks of objects and their classes.

[](#transformers.ImageSegmentationPipeline.example)

Example:

Copied


    >>> from transformers import pipeline

    >>> segmenter = pipeline(model="facebook/detr-resnet-50-panoptic")
    >>> segments = segmenter("https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png")
    >>> len(segments)
    2

    >>> segments[0]["label"]
    'bird'

    >>> segments[1]["label"]
    'bird'

    >>> type(segments[0]["mask"])  # This is a black and white mask showing where is the bird on the original image.
    <class 'PIL.Image.Image'>

    >>> segments[0]["mask"].size
    (768, 512)

This image segmentation pipeline can currently be loaded from [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) using the following task identifier: `"image-segmentation"`.

See the list of available models on [huggingface.co/models](https://huggingface.co/models?filter=image-segmentation).

#### __call__

[](#transformers.ImageSegmentationPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/image_segmentation.py#L101)

( inputs: typing.Union[str, ForwardRef('Image.Image'), list[str], list['Image.Image']] **kwargs: typing.Any )

Parameters

  * [](#transformers.ImageSegmentationPipeline.__call__.inputs) **inputs** (`str`, `list[str]`, `PIL.Image` or `list[PIL.Image]`) -- The pipeline handles three types of images:

    * A string containing an HTTP(S) link pointing to an image
    * A string containing a local path to an image
    * An image loaded in PIL directly

The pipeline accepts either a single image or a batch of images. Images in a batch must all be in the same format: all as HTTP(S) links, all as local paths, or all as PIL images.
  * [](#transformers.ImageSegmentationPipeline.__call__.subtask) **subtask** (`str`, _optional_) -- Segmentation task to be performed, choose [`semantic`, `instance` and `panoptic`] depending on model capabilities. If not set, the pipeline will attempt tp resolve in the following order: `panoptic`, `instance`, `semantic`.
  * [](#transformers.ImageSegmentationPipeline.__call__.threshold) **threshold** (`float`, _optional_ , defaults to 0.9) -- Probability threshold to filter out predicted masks.
  * [](#transformers.ImageSegmentationPipeline.__call__.mask_threshold) **mask_threshold** (`float`, _optional_ , defaults to 0.5) -- Threshold to use when turning the predicted masks into binary values.
  * [](#transformers.ImageSegmentationPipeline.__call__.overlap_mask_area_threshold) **overlap_mask_area_threshold** (`float`, _optional_ , defaults to 0.5) -- Mask overlap threshold to eliminate small, disconnected segments.
  * [](#transformers.ImageSegmentationPipeline.__call__.timeout) **timeout** (`float`, _optional_ , defaults to None) -- The maximum time in seconds to wait for fetching images from the web. If None, no timeout is set and the call may block forever.

Perform segmentation (detect masks & classes) in the image(s) passed as inputs.

### [](#transformers.KeypointMatchingPipeline) KeypointMatchingPipeline

### class transformers.KeypointMatchingPipeline

[](#transformers.KeypointMatchingPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/keypoint_matching.py#L69)

( *args **kwargs )

Keypoint matching pipeline using any `AutoModelForKeypointMatching`. This pipeline matches keypoints between two images.

#### __call__

[](#transformers.KeypointMatchingPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/keypoint_matching.py#L98)

( inputs: list[collections.abc.Sequence[typing.Union[ForwardRef('Image.Image'), str]]] | collections.abc.Sequence[typing.Union[ForwardRef('Image.Image'), str]] threshold: float = 0.0 **kwargs: typing.Any ) → Union[list[Match], list[list[Match]]]

Parameters

  * [](#transformers.KeypointMatchingPipeline.__call__.inputs) **inputs** (`str`, `list[str]`, `PIL.Image` or `list[PIL.Image]`) -- The pipeline handles three types of images:

    * A string containing a http link pointing to an image
    * A string containing a local path to an image
    * An image loaded in PIL directly

The pipeline accepts either a single pair of images or a batch of image pairs, which must then be passed as a string. Images in a batch must all be in the same format: all as http links, all as local paths, or all as PIL images.
  * [](#transformers.KeypointMatchingPipeline.__call__.threshold) **threshold** (`float`, _optional_ , defaults to 0.0) -- The threshold to use for keypoint matching. Keypoints matched with a lower matching score will be filtered out. A value of 0 means that all matched keypoints will be returned.
  * [](#transformers.KeypointMatchingPipeline.__call__.kwargs) **kwargs** -- `timeout (`float`, *optional*, defaults to None)` The maximum time in seconds to wait for fetching images from the web. If None, no timeout is set and the call may block forever.

Returns

Union[list[Match], list[list[Match]]]

A list of matches or a list if a single image pair is provided, or of lists of matches if a batch of image pairs is provided. Each match is a dictionary containing the following keys:

  * **keypoint_image_0** (`Keypoint`): The keypoint in the first image (x, y coordinates).
  * **keypoint_image_1** (`Keypoint`): The keypoint in the second image (x, y coordinates).
  * **score** (`float`): The matching score between the two keypoints.

Find matches between keypoints in two images.

### [](#transformers.ObjectDetectionPipeline) ObjectDetectionPipeline

### class transformers.ObjectDetectionPipeline

[](#transformers.ObjectDetectionPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/object_detection.py#L26)

( *args **kwargs )

Parameters

  * [](#transformers.ObjectDetectionPipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.ObjectDetectionPipeline.image_processor) **image_processor** ([BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor)) -- The image processor that will be used by the pipeline to encode data for the model. This object inherits from [BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor).
  * [](#transformers.ObjectDetectionPipeline.task) **task** (`str`, defaults to `""`) -- A task-identifier for the pipeline.
  * [](#transformers.ObjectDetectionPipeline.num_workers) **num_workers** (`int`, _optional_ , defaults to 8) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the number of workers to be used.
  * [](#transformers.ObjectDetectionPipeline.batch_size) **batch_size** (`int`, _optional_ , defaults to 1) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the size of the batch to use, for inference this is not always beneficial, please read [Batching with pipelines](https://huggingface.co/transformers/main_classes/pipelines.html#pipeline-batching) .
  * [](#transformers.ObjectDetectionPipeline.args_parser) **args_parser** ([ArgumentHandler](/docs/transformers/v5.8.0/en/internal/pipelines_utils#transformers.pipelines.ArgumentHandler), _optional_) -- Reference to the object in charge of parsing supplied pipeline parameters.
  * [](#transformers.ObjectDetectionPipeline.device) **device** (`int`, _optional_ , defaults to -1) -- Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on the associated CUDA device id. You can pass native `torch.device` or a `str` too
  * [](#transformers.ObjectDetectionPipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`)
  * [](#transformers.ObjectDetectionPipeline.binary_output) **binary_output** (`bool`, _optional_ , defaults to `False`) -- Flag indicating if the output the pipeline should happen in a serialized format (i.e., pickle) or as the raw output data e.g. text.

Object detection pipeline using any `AutoModelForObjectDetection`. This pipeline predicts bounding boxes of objects and their classes.

[](#transformers.ObjectDetectionPipeline.example)

Example:

Copied


    >>> from transformers import pipeline

    >>> detector = pipeline(model="facebook/detr-resnet-50")
    >>> detector("https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png")
    [{'score': 0.997, 'label': 'bird', 'box': {'xmin': 69, 'ymin': 171, 'xmax': 396, 'ymax': 507}}, {'score': 0.999, 'label': 'bird', 'box': {'xmin': 398, 'ymin': 105, 'xmax': 767, 'ymax': 507}}]

    >>> # x, y  are expressed relative to the top left hand corner.

Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

This object detection pipeline can currently be loaded from [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) using the following task identifier: `"object-detection"`.

See the list of available models on [huggingface.co/models](https://huggingface.co/models?filter=object-detection).

#### __call__

[](#transformers.ObjectDetectionPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/object_detection.py#L81)

( *args **kwargs )

Parameters

  * [](#transformers.ObjectDetectionPipeline.__call__.inputs) **inputs** (`str`, `list[str]`, `PIL.Image` or `list[PIL.Image]`) -- The pipeline handles three types of images:

    * A string containing an HTTP(S) link pointing to an image
    * A string containing a local path to an image
    * An image loaded in PIL directly

The pipeline accepts either a single image or a batch of images. Images in a batch must all be in the same format: all as HTTP(S) links, all as local paths, or all as PIL images.
  * [](#transformers.ObjectDetectionPipeline.__call__.threshold) **threshold** (`float`, _optional_ , defaults to 0.5) -- The probability necessary to make a prediction.
  * [](#transformers.ObjectDetectionPipeline.__call__.timeout) **timeout** (`float`, _optional_ , defaults to None) -- The maximum time in seconds to wait for fetching images from the web. If None, no timeout is set and the call may block forever.

Detect objects (bounding boxes & classes) in the image(s) passed as inputs.

### [](#transformers.VideoClassificationPipeline) VideoClassificationPipeline

### class transformers.VideoClassificationPipeline

[](#transformers.VideoClassificationPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/video_classification.py#L41)

( *args **kwargs )

Parameters

  * [](#transformers.VideoClassificationPipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.VideoClassificationPipeline.image_processor) **image_processor** ([BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor)) -- The image processor that will be used by the pipeline to encode data for the model. This object inherits from [BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor).
  * [](#transformers.VideoClassificationPipeline.task) **task** (`str`, defaults to `""`) -- A task-identifier for the pipeline.
  * [](#transformers.VideoClassificationPipeline.num_workers) **num_workers** (`int`, _optional_ , defaults to 8) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the number of workers to be used.
  * [](#transformers.VideoClassificationPipeline.batch_size) **batch_size** (`int`, _optional_ , defaults to 1) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the size of the batch to use, for inference this is not always beneficial, please read [Batching with pipelines](https://huggingface.co/transformers/main_classes/pipelines.html#pipeline-batching) .
  * [](#transformers.VideoClassificationPipeline.args_parser) **args_parser** ([ArgumentHandler](/docs/transformers/v5.8.0/en/internal/pipelines_utils#transformers.pipelines.ArgumentHandler), _optional_) -- Reference to the object in charge of parsing supplied pipeline parameters.
  * [](#transformers.VideoClassificationPipeline.device) **device** (`int`, _optional_ , defaults to -1) -- Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on the associated CUDA device id. You can pass native `torch.device` or a `str` too
  * [](#transformers.VideoClassificationPipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`)
  * [](#transformers.VideoClassificationPipeline.binary_output) **binary_output** (`bool`, _optional_ , defaults to `False`) -- Flag indicating if the output the pipeline should happen in a serialized format (i.e., pickle) or as the raw output data e.g. text.

Video classification pipeline using any `AutoModelForVideoClassification`. This pipeline predicts the class of a video.

This video classification pipeline can currently be loaded from [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) using the following task identifier: `"video-classification"`.

See the list of available models on [huggingface.co/models](https://huggingface.co/models?filter=video-classification).

#### __call__

[](#transformers.VideoClassificationPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/video_classification.py#L90)

( inputs: str | list[str] | None **kwargs )

Parameters

  * [](#transformers.VideoClassificationPipeline.__call__.inputs) **inputs** (`str`, `list[str]`) -- The pipeline handles three types of videos:

    * A string containing a http link pointing to a video
    * A string containing a local path to a video

The pipeline accepts either a single video or a batch of videos, which must then be passed as a string. Videos in a batch must all be in the same format: all as http links or all as local paths.
  * [](#transformers.VideoClassificationPipeline.__call__.top_k) **top_k** (`int`, _optional_ , defaults to 5) -- The number of top labels that will be returned by the pipeline. If the provided number is higher than the number of labels available in the model configuration, it will default to the number of labels.
  * [](#transformers.VideoClassificationPipeline.__call__.num_frames) **num_frames** (`int`, _optional_ , defaults to `self.model.config.num_frames`) -- The number of frames sampled from the video to run the classification on. If not provided, will default to the number of frames specified in the model configuration.
  * [](#transformers.VideoClassificationPipeline.__call__.frame_sampling_rate) **frame_sampling_rate** (`int`, _optional_ , defaults to 1) -- The sampling rate used to select frames from the video. If not provided, will default to 1, i.e. every frame will be used.
  * [](#transformers.VideoClassificationPipeline.__call__.function_to_apply\(str,) **function_to_apply(`str`,** _optional_ , defaults to "softmax") -- The function to apply to the model output. By default, the pipeline will apply the softmax function to the output of the model. Valid options: ["softmax", "sigmoid", "none"]. Note that passing Python's built-in `None` will default to "softmax", so you need to pass the string "none" to disable any post-processing.

Assign labels to the video(s) passed as inputs.

### [](#transformers.ZeroShotImageClassificationPipeline) ZeroShotImageClassificationPipeline

### class transformers.ZeroShotImageClassificationPipeline

[](#transformers.ZeroShotImageClassificationPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/zero_shot_image_classification.py#L29)

( **kwargs )

Parameters

  * [](#transformers.ZeroShotImageClassificationPipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.ZeroShotImageClassificationPipeline.image_processor) **image_processor** ([BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor)) -- The image processor that will be used by the pipeline to encode data for the model. This object inherits from [BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor).
  * [](#transformers.ZeroShotImageClassificationPipeline.task) **task** (`str`, defaults to `""`) -- A task-identifier for the pipeline.
  * [](#transformers.ZeroShotImageClassificationPipeline.num_workers) **num_workers** (`int`, _optional_ , defaults to 8) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the number of workers to be used.
  * [](#transformers.ZeroShotImageClassificationPipeline.batch_size) **batch_size** (`int`, _optional_ , defaults to 1) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the size of the batch to use, for inference this is not always beneficial, please read [Batching with pipelines](https://huggingface.co/transformers/main_classes/pipelines.html#pipeline-batching) .
  * [](#transformers.ZeroShotImageClassificationPipeline.args_parser) **args_parser** ([ArgumentHandler](/docs/transformers/v5.8.0/en/internal/pipelines_utils#transformers.pipelines.ArgumentHandler), _optional_) -- Reference to the object in charge of parsing supplied pipeline parameters.
  * [](#transformers.ZeroShotImageClassificationPipeline.device) **device** (`int`, _optional_ , defaults to -1) -- Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on the associated CUDA device id. You can pass native `torch.device` or a `str` too
  * [](#transformers.ZeroShotImageClassificationPipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`)
  * [](#transformers.ZeroShotImageClassificationPipeline.binary_output) **binary_output** (`bool`, _optional_ , defaults to `False`) -- Flag indicating if the output the pipeline should happen in a serialized format (i.e., pickle) or as the raw output data e.g. text.

Zero shot image classification pipeline using `CLIPModel`. This pipeline predicts the class of an image when you provide an image and a set of `candidate_labels`.

[](#transformers.ZeroShotImageClassificationPipeline.example)

Example:

Copied


    >>> from transformers import pipeline

    >>> classifier = pipeline(model="google/siglip-so400m-patch14-384")
    >>> classifier(
    ...     "https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png",
    ...     candidate_labels=["animals", "humans", "landscape"],
    ... )
    [{'score': 0.965, 'label': 'animals'}, {'score': 0.03, 'label': 'humans'}, {'score': 0.005, 'label': 'landscape'}]

    >>> classifier(
    ...     "https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png",
    ...     candidate_labels=["black and white", "photorealist", "painting"],
    ... )
    [{'score': 0.996, 'label': 'black and white'}, {'score': 0.003, 'label': 'photorealist'}, {'score': 0.0, 'label': 'painting'}]

Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

This image classification pipeline can currently be loaded from [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) using the following task identifier: `"zero-shot-image-classification"`.

See the list of available models on [huggingface.co/models](https://huggingface.co/models?filter=zero-shot-image-classification).

#### __call__

[](#transformers.ZeroShotImageClassificationPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/zero_shot_image_classification.py#L83)

( image: typing.Union[str, list[str], ForwardRef('Image.Image'), list['Image.Image']] candidate_labels: list **kwargs: typing.Any )

Parameters

  * [](#transformers.ZeroShotImageClassificationPipeline.__call__.image) **image** (`str`, `list[str]`, `PIL.Image` or `list[PIL.Image]`) -- The pipeline handles three types of images:

    * A string containing a http link pointing to an image
    * A string containing a local path to an image
    * An image loaded in PIL directly
  * [](#transformers.ZeroShotImageClassificationPipeline.__call__.candidate_labels) **candidate_labels** (`list[str]`) -- The candidate labels for this image. They will be formatted using _hypothesis_template_.
  * [](#transformers.ZeroShotImageClassificationPipeline.__call__.hypothesis_template) **hypothesis_template** (`str`, _optional_ , defaults to `"This is a photo of {}"`) -- The format used in conjunction with _candidate_labels_ to attempt the image classification by replacing the placeholder with the candidate_labels. Pass "{}" if _candidate_labels_ are already formatted.
  * [](#transformers.ZeroShotImageClassificationPipeline.__call__.timeout) **timeout** (`float`, _optional_ , defaults to None) -- The maximum time in seconds to wait for fetching images from the web. If None, no timeout is set and the call may block forever.

Assign labels to the image(s) passed as inputs.

### [](#transformers.ZeroShotObjectDetectionPipeline) ZeroShotObjectDetectionPipeline

### class transformers.ZeroShotObjectDetectionPipeline

[](#transformers.ZeroShotObjectDetectionPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/zero_shot_object_detection.py#L23)

( **kwargs )

Parameters

  * [](#transformers.ZeroShotObjectDetectionPipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.ZeroShotObjectDetectionPipeline.image_processor) **image_processor** ([BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor)) -- The image processor that will be used by the pipeline to encode data for the model. This object inherits from [BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor).
  * [](#transformers.ZeroShotObjectDetectionPipeline.task) **task** (`str`, defaults to `""`) -- A task-identifier for the pipeline.
  * [](#transformers.ZeroShotObjectDetectionPipeline.num_workers) **num_workers** (`int`, _optional_ , defaults to 8) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the number of workers to be used.
  * [](#transformers.ZeroShotObjectDetectionPipeline.batch_size) **batch_size** (`int`, _optional_ , defaults to 1) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the size of the batch to use, for inference this is not always beneficial, please read [Batching with pipelines](https://huggingface.co/transformers/main_classes/pipelines.html#pipeline-batching) .
  * [](#transformers.ZeroShotObjectDetectionPipeline.args_parser) **args_parser** ([ArgumentHandler](/docs/transformers/v5.8.0/en/internal/pipelines_utils#transformers.pipelines.ArgumentHandler), _optional_) -- Reference to the object in charge of parsing supplied pipeline parameters.
  * [](#transformers.ZeroShotObjectDetectionPipeline.device) **device** (`int`, _optional_ , defaults to -1) -- Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on the associated CUDA device id. You can pass native `torch.device` or a `str` too
  * [](#transformers.ZeroShotObjectDetectionPipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`)
  * [](#transformers.ZeroShotObjectDetectionPipeline.binary_output) **binary_output** (`bool`, _optional_ , defaults to `False`) -- Flag indicating if the output the pipeline should happen in a serialized format (i.e., pickle) or as the raw output data e.g. text.

Zero shot object detection pipeline using `OwlViTForObjectDetection`. This pipeline predicts bounding boxes of objects when you provide an image and a set of `candidate_labels`.

[](#transformers.ZeroShotObjectDetectionPipeline.example)

Example:

Copied


    >>> from transformers import pipeline

    >>> detector = pipeline(model="google/owlvit-base-patch32", task="zero-shot-object-detection")
    >>> detector(
    ...     "http://images.cocodataset.org/val2017/000000039769.jpg",
    ...     candidate_labels=["cat", "couch"],
    ... )
    [{'score': 0.287, 'label': 'cat', 'box': {'xmin': 324, 'ymin': 20, 'xmax': 640, 'ymax': 373}}, {'score': 0.254, 'label': 'cat', 'box': {'xmin': 1, 'ymin': 55, 'xmax': 315, 'ymax': 472}}, {'score': 0.121, 'label': 'couch', 'box': {'xmin': 4, 'ymin': 0, 'xmax': 642, 'ymax': 476}}]

    >>> detector(
    ...     "https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png",
    ...     candidate_labels=["head", "bird"],
    ... )
    [{'score': 0.119, 'label': 'bird', 'box': {'xmin': 71, 'ymin': 170, 'xmax': 410, 'ymax': 508}}]

Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

This object detection pipeline can currently be loaded from [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) using the following task identifier: `"zero-shot-object-detection"`.

See the list of available models on [huggingface.co/models](https://huggingface.co/models?filter=zero-shot-object-detection).

#### __call__

[](#transformers.ZeroShotObjectDetectionPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/zero_shot_object_detection.py#L75)

( image: typing.Union[str, ForwardRef('Image.Image'), list[dict[str, typing.Any]]] candidate_labels: str | list[str] | None = None **kwargs: typing.Any )

Parameters

  * [](#transformers.ZeroShotObjectDetectionPipeline.__call__.image) **image** (`str`, `PIL.Image` or `list[dict[str, Any]]`) -- The pipeline handles three types of images:

    * A string containing an http url pointing to an image
    * A string containing a local path to an image
    * An image loaded in PIL directly

You can use this parameter to send directly a list of images, or a dataset or a generator like so:

Detect objects (bounding boxes & classes) in the image(s) passed as inputs.

## [](#natural-language-processing) Natural Language Processing

Pipelines available for natural language processing tasks include the following.

### [](#transformers.FillMaskPipeline) FillMaskPipeline

### class transformers.FillMaskPipeline

[](#transformers.FillMaskPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/fill_mask.py#L28)

( model: PreTrainedModel tokenizer: PreTrainedTokenizer | None = None feature_extractor: PreTrainedFeatureExtractor | None = None image_processor: BaseImageProcessor | None = None processor: ProcessorMixin | None = None task: str = '' device: int | torch.device | None = None binary_output: bool = False **kwargs )

Parameters

  * [](#transformers.FillMaskPipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.FillMaskPipeline.tokenizer) **tokenizer** ([PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend)) -- The tokenizer that will be used by the pipeline to encode data for the model. This object inherits from [PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend).
  * [](#transformers.FillMaskPipeline.task) **task** (`str`, defaults to `""`) -- A task-identifier for the pipeline.
  * [](#transformers.FillMaskPipeline.num_workers) **num_workers** (`int`, _optional_ , defaults to 8) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the number of workers to be used.
  * [](#transformers.FillMaskPipeline.batch_size) **batch_size** (`int`, _optional_ , defaults to 1) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the size of the batch to use, for inference this is not always beneficial, please read [Batching with pipelines](https://huggingface.co/transformers/main_classes/pipelines.html#pipeline-batching) .
  * [](#transformers.FillMaskPipeline.args_parser) **args_parser** ([ArgumentHandler](/docs/transformers/v5.8.0/en/internal/pipelines_utils#transformers.pipelines.ArgumentHandler), _optional_) -- Reference to the object in charge of parsing supplied pipeline parameters.
  * [](#transformers.FillMaskPipeline.device) **device** (`int`, _optional_ , defaults to -1) -- Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on the associated CUDA device id. You can pass native `torch.device` or a `str` too
  * [](#transformers.FillMaskPipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`)
  * [](#transformers.FillMaskPipeline.binary_output) **binary_output** (`bool`, _optional_ , defaults to `False`) -- Flag indicating if the output the pipeline should happen in a serialized format (i.e., pickle) or as the raw output data e.g. text.
  * [](#transformers.FillMaskPipeline.top_k) **top_k** (`int`, _optional_ , defaults to 5) -- The number of predictions to return.
  * [](#transformers.FillMaskPipeline.targets) **targets** (`str` or `list[str]`, _optional_) -- When passed, the model will limit the scores to the passed targets instead of looking up in the whole vocab. If the provided targets are not in the model vocab, they will be tokenized and the first resulting token will be used (with a warning, and that might be slower).
  * [](#transformers.FillMaskPipeline.tokenizer_kwargs) **tokenizer_kwargs** (`dict`, _optional_) -- Additional dictionary of keyword arguments passed along to the tokenizer.

#### __call__

[](#transformers.FillMaskPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/fill_mask.py#L234)

( inputs: str | list[str] **kwargs: typing.Any ) → A list or a list of list of `dict`

Parameters

  * [](#transformers.FillMaskPipeline.__call__.inputs) **inputs** (`str` or `list[str]`) -- One or several texts (or one list of prompts) with masked tokens.
  * [](#transformers.FillMaskPipeline.__call__.targets) **targets** (`str` or `list[str]`, _optional_) -- When passed, the model will limit the scores to the passed targets instead of looking up in the whole vocab. If the provided targets are not in the model vocab, they will be tokenized and the first resulting token will be used (with a warning, and that might be slower).
  * [](#transformers.FillMaskPipeline.__call__.top_k) **top_k** (`int`, _optional_) -- When passed, overrides the number of predictions to return.

Returns

A list or a list of list of `dict`

Each result comes as list of dictionaries with the following keys:

  * **sequence** (`str`) — The corresponding input with the mask token prediction.
  * **score** (`float`) — The corresponding probability.
  * **token** (`int`) — The predicted token id (to replace the masked one).
  * **token_str** (`str`) — The predicted token (to replace the masked one).

Fill the masked token in the text(s) given as inputs.

### [](#transformers.TableQuestionAnsweringPipeline) TableQuestionAnsweringPipeline

### class transformers.TableQuestionAnsweringPipeline

[](#transformers.TableQuestionAnsweringPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/table_question_answering.py#L78)

( args_parser = <transformers.pipelines.table_question_answering.TableQuestionAnsweringArgumentHandler object at 0x7f8a52149840> **kwargs )

Parameters

  * [](#transformers.TableQuestionAnsweringPipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.TableQuestionAnsweringPipeline.tokenizer) **tokenizer** ([PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend)) -- The tokenizer that will be used by the pipeline to encode data for the model. This object inherits from [PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend).
  * [](#transformers.TableQuestionAnsweringPipeline.task) **task** (`str`, defaults to `""`) -- A task-identifier for the pipeline.
  * [](#transformers.TableQuestionAnsweringPipeline.num_workers) **num_workers** (`int`, _optional_ , defaults to 8) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the number of workers to be used.
  * [](#transformers.TableQuestionAnsweringPipeline.batch_size) **batch_size** (`int`, _optional_ , defaults to 1) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the size of the batch to use, for inference this is not always beneficial, please read [Batching with pipelines](https://huggingface.co/transformers/main_classes/pipelines.html#pipeline-batching) .
  * [](#transformers.TableQuestionAnsweringPipeline.args_parser) **args_parser** ([ArgumentHandler](/docs/transformers/v5.8.0/en/internal/pipelines_utils#transformers.pipelines.ArgumentHandler), _optional_) -- Reference to the object in charge of parsing supplied pipeline parameters.
  * [](#transformers.TableQuestionAnsweringPipeline.device) **device** (`int`, _optional_ , defaults to -1) -- Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on the associated CUDA device id. You can pass native `torch.device` or a `str` too
  * [](#transformers.TableQuestionAnsweringPipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`)
  * [](#transformers.TableQuestionAnsweringPipeline.binary_output) **binary_output** (`bool`, _optional_ , defaults to `False`) -- Flag indicating if the output the pipeline should happen in a serialized format (i.e., pickle) or as the raw output data e.g. text.

Table Question Answering pipeline using a `ModelForTableQuestionAnswering`. This pipeline is only available in PyTorch.

Unless the model you’re using explicitly sets these generation parameters in its configuration files (`generation_config.json`), the following default values will be used:

  * max_new_tokens: 256

[](#transformers.TableQuestionAnsweringPipeline.example)

Example:

Copied


    >>> from transformers import pipeline

    >>> oracle = pipeline(model="google/tapas-base-finetuned-wtq")
    >>> table = {
    ...     "Repository": ["Transformers", "Datasets", "Tokenizers"],
    ...     "Stars": ["36542", "4512", "3934"],
    ...     "Contributors": ["651", "77", "34"],
    ...     "Programming language": ["Python", "Python", "Rust, Python and NodeJS"],
    ... }
    >>> oracle(query="How many stars does the transformers repository have?", table=table)
    {'answer': 'AVERAGE > 36542', 'coordinates': [(0, 1)], 'cells': ['36542'], 'aggregator': 'AVERAGE'}

Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

This tabular question answering pipeline can currently be loaded from [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) using the following task identifier: `"table-question-answering"`.

The models that this pipeline can use are models that have been fine-tuned on a tabular question answering task. See the up-to-date list of available models on [huggingface.co/models](https://huggingface.co/models?filter=table-question-answering).

#### __call__

[](#transformers.TableQuestionAnsweringPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/table_question_answering.py#L208)

( *args **kwargs ) → A dictionary or a list of dictionaries containing results

Parameters

  * [](#transformers.TableQuestionAnsweringPipeline.__call__.table) **table** (`pd.DataFrame` or `Dict`) -- Pandas DataFrame or dictionary that will be converted to a DataFrame containing all the table values. See above for an example of dictionary.
  * [](#transformers.TableQuestionAnsweringPipeline.__call__.query) **query** (`str` or `list[str]`) -- Query or list of queries that will be sent to the model alongside the table.
  * [](#transformers.TableQuestionAnsweringPipeline.__call__.sequential) **sequential** (`bool`, _optional_ , defaults to `False`) -- Whether to do inference sequentially or as a batch. Batching is faster, but models like SQA require the inference to be done sequentially to extract relations within sequences, given their conversational nature.
  * [](#transformers.TableQuestionAnsweringPipeline.__call__.padding) **padding** (`bool`, `str` or [PaddingStrategy](/docs/transformers/v5.8.0/en/internal/file_utils#transformers.utils.PaddingStrategy), _optional_ , defaults to `False`) -- Activates and controls padding. Accepts the following values:

    * `True` or `'longest'`: Pad to the longest sequence in the batch (or no padding if only a single sequence if provided).
    * `'max_length'`: Pad to a maximum length specified with the argument `max_length` or to the maximum acceptable input length for the model if that argument is not provided.
    * `False` or `'do_not_pad'` (default): No padding (i.e., can output a batch with sequences of different lengths).
  * [](#transformers.TableQuestionAnsweringPipeline.__call__.truncation) **truncation** (`bool`, `str` or `TapasTruncationStrategy`, _optional_ , defaults to `False`) -- Activates and controls truncation. Accepts the following values:

    * `True` or `'drop_rows_to_fit'`: Truncate to a maximum length specified with the argument `max_length` or to the maximum acceptable input length for the model if that argument is not provided. This will truncate row by row, removing rows from the table.
    * `False` or `'do_not_truncate'` (default): No truncation (i.e., can output batch with sequence lengths greater than the model maximum admissible input size).

Returns

A dictionary or a list of dictionaries containing results

Each result is a dictionary with the following keys:

  * **answer** (`str`) — The answer of the query given the table. If there is an aggregator, the answer will be preceded by `AGGREGATOR >`.
  * **coordinates** (`list[tuple[int, int]]`) — Coordinates of the cells of the answers.
  * **cells** (`list[str]`) — List of strings made up of the answer cell values.
  * **aggregator** (`str`) — If the model has an aggregator, this returns the aggregator.

Answers queries according to a table. The pipeline accepts several types of inputs which are detailed below:

  * `pipeline(table, query)`
  * `pipeline(table, [query])`
  * `pipeline(table=table, query=query)`
  * `pipeline(table=table, query=[query])`
  * `pipeline({"table": table, "query": query})`
  * `pipeline({"table": table, "query": [query]})`
  * `pipeline([{"table": table, "query": query}, {"table": table, "query": query}])`

The `table` argument should be a dict or a DataFrame built from that dict, containing the whole table:

[](#transformers.TableQuestionAnsweringPipeline.__call__.example)

Example:

Copied


    data = {
        "actors": ["brad pitt", "leonardo di caprio", "george clooney"],
        "age": ["56", "45", "59"],
        "number of movies": ["87", "53", "69"],
        "date of birth": ["7 february 1967", "10 june 1996", "28 november 1967"],
    }

This dictionary can be passed in as such, or can be converted to a pandas DataFrame:

[](#transformers.TableQuestionAnsweringPipeline.__call__.example-2)

Example:

Copied


    import pandas as pd

    table = pd.DataFrame.from_dict(data)

### [](#transformers.TextClassificationPipeline) TextClassificationPipeline

### class transformers.TextClassificationPipeline

[](#transformers.TextClassificationPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/text_classification.py#L43)

( **kwargs )

Parameters

  * [](#transformers.TextClassificationPipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.TextClassificationPipeline.tokenizer) **tokenizer** ([PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend)) -- The tokenizer that will be used by the pipeline to encode data for the model. This object inherits from [PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend).
  * [](#transformers.TextClassificationPipeline.task) **task** (`str`, defaults to `""`) -- A task-identifier for the pipeline.
  * [](#transformers.TextClassificationPipeline.num_workers) **num_workers** (`int`, _optional_ , defaults to 8) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the number of workers to be used.
  * [](#transformers.TextClassificationPipeline.batch_size) **batch_size** (`int`, _optional_ , defaults to 1) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the size of the batch to use, for inference this is not always beneficial, please read [Batching with pipelines](https://huggingface.co/transformers/main_classes/pipelines.html#pipeline-batching) .
  * [](#transformers.TextClassificationPipeline.args_parser) **args_parser** ([ArgumentHandler](/docs/transformers/v5.8.0/en/internal/pipelines_utils#transformers.pipelines.ArgumentHandler), _optional_) -- Reference to the object in charge of parsing supplied pipeline parameters.
  * [](#transformers.TextClassificationPipeline.device) **device** (`int`, _optional_ , defaults to -1) -- Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on the associated CUDA device id. You can pass native `torch.device` or a `str` too
  * [](#transformers.TextClassificationPipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`)
  * [](#transformers.TextClassificationPipeline.binary_output) **binary_output** (`bool`, _optional_ , defaults to `False`) -- Flag indicating if the output the pipeline should happen in a serialized format (i.e., pickle) or as the raw output data e.g. text.
  * [](#transformers.TextClassificationPipeline.function_to_apply) **function_to_apply** (`str`, _optional_ , defaults to `"default"`) -- The function to apply to the model outputs in order to retrieve the scores. Accepts four different values:

    * `"default"`: if the model has a single label, will apply the sigmoid function on the output. If the model has several labels, will apply the softmax function on the output. In case of regression tasks, will not apply any function on the output.
    * `"sigmoid"`: Applies the sigmoid function on the output.
    * `"softmax"`: Applies the softmax function on the output.
    * `"none"`: Does not apply any function on the output.

Text classification pipeline using any `ModelForSequenceClassification`. See the [sequence classification examples](../task_summary#sequence-classification) for more information.

[](#transformers.TextClassificationPipeline.example)

Example:

Copied


    >>> from transformers import pipeline

    >>> classifier = pipeline(model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
    >>> classifier("This movie is disgustingly good !")
    [{'label': 'POSITIVE', 'score': 1.0}]

    >>> classifier("Director tried too much.")
    [{'label': 'NEGATIVE', 'score': 0.996}]

Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

This text classification pipeline can currently be loaded from [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) using the following task identifier: `"sentiment-analysis"` (for classifying sequences according to positive or negative sentiments).

If multiple classification labels are available (`model.config.num_labels >= 2`), the pipeline will run a softmax over the results. If there is a single label, the pipeline will run a sigmoid over the result. In case of regression tasks (`model.config.problem_type == "regression"`), will not apply any function on the output.

The models that this pipeline can use are models that have been fine-tuned on a sequence classification task. See the up-to-date list of available models on [huggingface.co/models](https://huggingface.co/models?filter=text-classification).

#### __call__

[](#transformers.TextClassificationPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/text_classification.py#L105)

( inputs: str | list[str] | dict[str, str] | list[dict[str, str]] **kwargs: typing.Any ) → A list of `dict`

Parameters

  * [](#transformers.TextClassificationPipeline.__call__.inputs) **inputs** (`str` or `list[str]` or `dict[str]`, or `list[dict[str]]`) -- One or several texts to classify. In order to use text pairs for your classification, you can send a dictionary containing `{"text", "text_pair"}` keys, or a list of those.
  * [](#transformers.TextClassificationPipeline.__call__.top_k) **top_k** (`int`, _optional_ , defaults to `1`) -- How many results to return.
  * [](#transformers.TextClassificationPipeline.__call__.function_to_apply) **function_to_apply** (`str`, _optional_ , defaults to `"default"`) -- The function to apply to the model outputs in order to retrieve the scores. Accepts four different values:

If this argument is not specified, then it will apply the following functions according to the number of labels:

    * If problem type is regression, will not apply any function on the output.
    * If the model has a single label, will apply the sigmoid function on the output.
    * If the model has several labels, will apply the softmax function on the output.

Possible values are:

    * `"sigmoid"`: Applies the sigmoid function on the output.
    * `"softmax"`: Applies the softmax function on the output.
    * `"none"`: Does not apply any function on the output.

Returns

A list of `dict`

Each result comes as list of dictionaries with the following keys:

  * **label** (`str`) — The label predicted.
  * **score** (`float`) — The corresponding probability.

If `top_k` is used, one such dictionary is returned per label.

Classify the text(s) given as inputs.

### [](#transformers.TextGenerationPipeline) TextGenerationPipeline

### class transformers.TextGenerationPipeline

[](#transformers.TextGenerationPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/text_generation.py#L23)

( *args **kwargs )

Parameters

  * [](#transformers.TextGenerationPipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.TextGenerationPipeline.tokenizer) **tokenizer** ([PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend)) -- The tokenizer that will be used by the pipeline to encode data for the model. This object inherits from [PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend).
  * [](#transformers.TextGenerationPipeline.task) **task** (`str`, defaults to `""`) -- A task-identifier for the pipeline.
  * [](#transformers.TextGenerationPipeline.num_workers) **num_workers** (`int`, _optional_ , defaults to 8) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the number of workers to be used.
  * [](#transformers.TextGenerationPipeline.batch_size) **batch_size** (`int`, _optional_ , defaults to 1) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the size of the batch to use, for inference this is not always beneficial, please read [Batching with pipelines](https://huggingface.co/transformers/main_classes/pipelines.html#pipeline-batching) .
  * [](#transformers.TextGenerationPipeline.args_parser) **args_parser** ([ArgumentHandler](/docs/transformers/v5.8.0/en/internal/pipelines_utils#transformers.pipelines.ArgumentHandler), _optional_) -- Reference to the object in charge of parsing supplied pipeline parameters.
  * [](#transformers.TextGenerationPipeline.device) **device** (`int`, _optional_ , defaults to -1) -- Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on the associated CUDA device id. You can pass native `torch.device` or a `str` too
  * [](#transformers.TextGenerationPipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`)
  * [](#transformers.TextGenerationPipeline.binary_output) **binary_output** (`bool`, _optional_ , defaults to `False`) -- Flag indicating if the output the pipeline should happen in a serialized format (i.e., pickle) or as the raw output data e.g. text.

Language generation pipeline using any `ModelWithLMHead` or `ModelForCausalLM`. This pipeline predicts the words that will follow a specified text prompt. When the underlying model is a conversational model, it can also accept one or more chats, in which case the pipeline will operate in chat mode and will continue the chat(s) by adding its response(s). Each chat takes the form of a list of dicts, where each dict contains “role” and “content” keys.

Unless the model you’re using explicitly sets these generation parameters in its configuration files (`generation_config.json`), the following default values will be used:

  * max_new_tokens: 256
  * do_sample: True
  * temperature: 0.7

[](#transformers.TextGenerationPipeline.example)

Examples:

Copied


    >>> from transformers import pipeline

    >>> generator = pipeline(model="openai-community/gpt2")
    >>> generator("I can't believe you did such a ", do_sample=False)
    [{'generated_text': "I can't believe you did such a icky thing to me. I'm so sorry. I'm so sorry. I'm so sorry. I'm so sorry. I'm so sorry. I'm so sorry. I'm so sorry. I"}]

    >>> # These parameters will return suggestions, and only the newly created text making it easier for prompting suggestions.
    >>> outputs = generator("My tart needs some", num_return_sequences=4, return_full_text=False)

[](#transformers.TextGenerationPipeline.example-2)

Copied


    >>> from transformers import pipeline

    >>> generator = pipeline(model="HuggingFaceH4/zephyr-7b-beta")
    >>> # Zephyr-beta is a conversational model, so let's pass it a chat instead of a single string
    >>> generator([{"role": "user", "content": "What is the capital of France? Answer in one word."}], do_sample=False, max_new_tokens=2)
    [{'generated_text': [{'role': 'user', 'content': 'What is the capital of France? Answer in one word.'}, {'role': 'assistant', 'content': 'Paris'}]}]

Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial). You can pass text generation parameters to this pipeline to control stopping criteria, decoding strategy, and more. Learn more about text generation parameters in [Text generation strategies](../generation_strategies) and [Text generation](text_generation).

This language generation pipeline can currently be loaded from [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) using the following task identifier: `"text-generation"`.

The models that this pipeline can use are models that have been trained with an autoregressive language modeling objective. See the list of available [text completion models](https://huggingface.co/models?filter=text-generation) and the list of [conversational models](https://huggingface.co/models?other=conversational) on [huggingface.co/models].

#### __call__

[](#transformers.TextGenerationPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/text_generation.py#L249)

( text_inputs **kwargs ) → A list or a list of lists of `dict`

Parameters

  * [](#transformers.TextGenerationPipeline.__call__.text_inputs) **text_inputs** (`str`, `list[str]`, `ChatType`, or `list[ChatType]`) -- One or several prompts (or one list of prompts) to complete. If strings or a list of string are passed, this pipeline will continue each prompt. Alternatively, a "chat", in the form of a list of dicts with "role" and "content" keys, can be passed, or a list of such chats. When chats are passed, the model's chat template will be used to format them before passing them to the model.
  * [](#transformers.TextGenerationPipeline.__call__.return_tensors) **return_tensors** (`bool`, _optional_ , defaults to `False`) -- Returns the tensors of predictions (as token indices) in the outputs. If set to `True`, the decoded text is not returned.
  * [](#transformers.TextGenerationPipeline.__call__.return_text) **return_text** (`bool`, _optional_) -- Returns the decoded texts in the outputs.
  * [](#transformers.TextGenerationPipeline.__call__.return_full_text) **return_full_text** (`bool`, _optional_ , defaults to `True`) -- If set to `False` only added text is returned, otherwise the full text is returned. Cannot be specified at the same time as `return_text`.
  * [](#transformers.TextGenerationPipeline.__call__.clean_up_tokenization_spaces) **clean_up_tokenization_spaces** (`bool`, _optional_ , defaults to `True`) -- Whether or not to clean up the potential extra spaces in the text output.
  * [](#transformers.TextGenerationPipeline.__call__.continue_final_message\() **continue_final_message(** `bool`, _optional_) -- This indicates that you want the model to continue the last message in the input chat rather than starting a new one, allowing you to "prefill" its response. By default this is `True` when the final message in the input chat has the `assistant` role and `False` otherwise, but you can manually override that behaviour by setting this flag.
  * [](#transformers.TextGenerationPipeline.__call__.prefix) **prefix** (`str`, _optional_) -- Prefix added to prompt.
  * [](#transformers.TextGenerationPipeline.__call__.handle_long_generation) **handle_long_generation** (`str`, _optional_) -- By default, this pipelines does not handle long generation (ones that exceed in one form or the other the model maximum length). There is no perfect way to address this (more info :<https://github.com/huggingface/transformers/issues/14033#issuecomment-948385227>). This provides common strategies to work around that problem depending on your use case.

    * `None` : default strategy where nothing in particular happens
    * `"hole"`: Truncates left of input, and leaves a gap wide enough to let generation happen (might truncate a lot of the prompt and not suitable when generation exceed the model capacity)
  * [](#transformers.TextGenerationPipeline.__call__.tokenizer_encode_kwargs) **tokenizer_encode_kwargs** (`dict`, _optional_) -- Additional keyword arguments to pass along to the encoding step of the tokenizer. If the text input is a chat, it is passed to `apply_chat_template`. Otherwise, it is passed to `__call__`.
  * [](#transformers.TextGenerationPipeline.__call__.generate_kwargs) **generate_kwargs** (`dict`, _optional_) -- Additional keyword arguments to pass along to the generate method of the model (see the generate method [here](./text_generation)).

Returns

A list or a list of lists of `dict`

Returns one of the following dictionaries (cannot return a combination of both `generated_text` and `generated_token_ids`):

  * **generated_text** (`str`, present when `return_text=True`) — The generated text.
  * **generated_token_ids** (`torch.Tensor`, present when `return_tensors=True`) — The token ids of the generated text.

Complete the prompt(s) given as inputs.

### [](#transformers.TokenClassificationPipeline) TokenClassificationPipeline

### class transformers.TokenClassificationPipeline

[](#transformers.TokenClassificationPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/token_classification.py#L92)

( args_parser = <transformers.pipelines.token_classification.TokenClassificationArgumentHandler object at 0x7f8a52148e50> **kwargs )

Parameters

  * [](#transformers.TokenClassificationPipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.TokenClassificationPipeline.tokenizer) **tokenizer** ([PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend)) -- The tokenizer that will be used by the pipeline to encode data for the model. This object inherits from [PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend).
  * [](#transformers.TokenClassificationPipeline.task) **task** (`str`, defaults to `""`) -- A task-identifier for the pipeline.
  * [](#transformers.TokenClassificationPipeline.num_workers) **num_workers** (`int`, _optional_ , defaults to 8) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the number of workers to be used.
  * [](#transformers.TokenClassificationPipeline.batch_size) **batch_size** (`int`, _optional_ , defaults to 1) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the size of the batch to use, for inference this is not always beneficial, please read [Batching with pipelines](https://huggingface.co/transformers/main_classes/pipelines.html#pipeline-batching) .
  * [](#transformers.TokenClassificationPipeline.args_parser) **args_parser** ([ArgumentHandler](/docs/transformers/v5.8.0/en/internal/pipelines_utils#transformers.pipelines.ArgumentHandler), _optional_) -- Reference to the object in charge of parsing supplied pipeline parameters.
  * [](#transformers.TokenClassificationPipeline.device) **device** (`int`, _optional_ , defaults to -1) -- Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on the associated CUDA device id. You can pass native `torch.device` or a `str` too
  * [](#transformers.TokenClassificationPipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`)
  * [](#transformers.TokenClassificationPipeline.binary_output) **binary_output** (`bool`, _optional_ , defaults to `False`) -- Flag indicating if the output the pipeline should happen in a serialized format (i.e., pickle) or as the raw output data e.g. text.
  * [](#transformers.TokenClassificationPipeline.ignore_labels) **ignore_labels** (`list[str]`, defaults to `["O"]`) -- A list of labels to ignore.
  * [](#transformers.TokenClassificationPipeline.stride) **stride** (`int`, _optional_) -- If stride is provided, the pipeline is applied on all the text. The text is split into chunks of size model_max_length. Works only with fast tokenizers and `aggregation_strategy` different from `NONE`. The value of this argument defines the number of overlapping tokens between chunks. In other words, the model will shift forward by `tokenizer.model_max_length - stride` tokens each step.
  * [](#transformers.TokenClassificationPipeline.aggregation_strategy) **aggregation_strategy** (`str`, _optional_ , defaults to `"none"`) -- The strategy to fuse (or not) tokens based on the model prediction.

    * "none" : Will simply not do any aggregation and simply return raw results from the model
    * "simple" : Will attempt to group entities following the default schema. (A, B-TAG), (B, I-TAG), (C, I-TAG), (D, B-TAG2) (E, B-TAG2) will end up being [{"word": ABC, "entity": "TAG"}, {"word": "D", "entity": "TAG2"}, {"word": "E", "entity": "TAG2"}] Notice that two consecutive B tags will end up as different entities. On word based languages, we might end up splitting words undesirably : Imagine Microsoft being tagged as [{"word": "Micro", "entity": "ENTERPRISE"}, {"word": "soft", "entity": "NAME"}]. Look for FIRST, MAX, AVERAGE for ways to mitigate that and disambiguate words (on languages that support that meaning, which is basically tokens separated by a space). These mitigations will only work on real words, "New york" might still be tagged with two different entities.
    * "first" : (works only on word based models) Will use the `SIMPLE` strategy except that words, cannot end up with different tags. Words will simply use the tag of the first token of the word when there is ambiguity.
    * "average" : (works only on word based models) Will use the `SIMPLE` strategy except that words, cannot end up with different tags. scores will be averaged first across tokens, and then the maximum label is applied.
    * "max" : (works only on word based models) Will use the `SIMPLE` strategy except that words, cannot end up with different tags. Word entity will simply be the token with the maximum score.

Named Entity Recognition pipeline using any `ModelForTokenClassification`. See the [named entity recognition examples](../task_summary#named-entity-recognition) for more information.

[](#transformers.TokenClassificationPipeline.example)

Example:

Copied


    >>> from transformers import pipeline

    >>> token_classifier = pipeline(model="Jean-Baptiste/camembert-ner", aggregation_strategy="simple")
    >>> sentence = "Je m'appelle jean-baptiste et je vis à montréal"
    >>> tokens = token_classifier(sentence)
    >>> tokens
    [{'entity_group': 'PER', 'score': 0.9931, 'word': 'jean-baptiste', 'start': 12, 'end': 26}, {'entity_group': 'LOC', 'score': 0.998, 'word': 'montréal', 'start': 38, 'end': 47}]

    >>> token = tokens[0]
    >>> # Start and end provide an easy way to highlight words in the original text.
    >>> sentence[token["start"] : token["end"]]
    ' jean-baptiste'

    >>> # Some models use the same idea to do part of speech.
    >>> syntaxer = pipeline(model="vblagoje/bert-english-uncased-finetuned-pos", aggregation_strategy="simple")
    >>> syntaxer("My name is Sarah and I live in London")
    [{'entity_group': 'PRON', 'score': 0.999, 'word': 'my', 'start': 0, 'end': 2}, {'entity_group': 'NOUN', 'score': 0.997, 'word': 'name', 'start': 3, 'end': 7}, {'entity_group': 'AUX', 'score': 0.994, 'word': 'is', 'start': 8, 'end': 10}, {'entity_group': 'PROPN', 'score': 0.999, 'word': 'sarah', 'start': 11, 'end': 16}, {'entity_group': 'CCONJ', 'score': 0.999, 'word': 'and', 'start': 17, 'end': 20}, {'entity_group': 'PRON', 'score': 0.999, 'word': 'i', 'start': 21, 'end': 22}, {'entity_group': 'VERB', 'score': 0.998, 'word': 'live', 'start': 23, 'end': 27}, {'entity_group': 'ADP', 'score': 0.999, 'word': 'in', 'start': 28, 'end': 30}, {'entity_group': 'PROPN', 'score': 0.999, 'word': 'london', 'start': 31, 'end': 37}]

Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

This token recognition pipeline can currently be loaded from [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) using the following task identifier: `"ner"` (for predicting the classes of tokens in a sequence: person, organisation, location or miscellaneous).

The models that this pipeline can use are models that have been fine-tuned on a token classification task. See the up-to-date list of available models on [huggingface.co/models](https://huggingface.co/models?filter=token-classification).

#### __call__

[](#transformers.TokenClassificationPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/token_classification.py#L209)

( inputs: str | list[str] **kwargs: typing.Any ) → A list or a list of list of `dict`

Parameters

  * [](#transformers.TokenClassificationPipeline.__call__.inputs) **inputs** (`str` or `List[str]`) -- One or several texts (or one list of texts) for token classification. Can be pre-tokenized when `is_split_into_words=True`.

Returns

A list or a list of list of `dict`

Each result comes as a list of dictionaries (one for each token in the corresponding input, or each entity if this pipeline was instantiated with an aggregation_strategy) with the following keys:

  * **word** (`str`) — The token/word classified. This is obtained by decoding the selected tokens. If you want to have the exact string in the original sentence, use `start` and `end`.
  * **score** (`float`) — The corresponding probability for `entity`.
  * **entity** (`str`) — The entity predicted for that token/word (it is named _entity_group_ when _aggregation_strategy_ is not `"none"`.
  * **index** (`int`, only present when `aggregation_strategy="none"`) — The index of the corresponding token in the sentence.
  * **start** (`int`, _optional_) — The index of the start of the corresponding entity in the sentence. Only exists if the offsets are available within the tokenizer
  * **end** (`int`, _optional_) — The index of the end of the corresponding entity in the sentence. Only exists if the offsets are available within the tokenizer

Classify each token of the text(s) given as inputs.

#### aggregate_words

[](#transformers.TokenClassificationPipeline.aggregate_words) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/token_classification.py#L521)

( entities: list aggregation_strategy: AggregationStrategy )

Override tokens from a given word that disagree to force agreement on word boundaries.

Example: micro|soft| com|pany| B-ENT I-NAME I-ENT I-ENT will be rewritten with first strategy as microsoft| company| B-ENT I-ENT

#### gather_pre_entities

[](#transformers.TokenClassificationPipeline.gather_pre_entities) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/token_classification.py#L397)

( sentence: str input_ids: ndarray scores: ndarray offset_mapping: list[tuple[int, int]] | None special_tokens_mask: ndarray aggregation_strategy: AggregationStrategy word_ids: list[int | None] | None = None word_to_chars_map: list[tuple[int, int]] | None = None )

Fuse various numpy arrays into dicts with all the information needed for aggregation

#### group_entities

[](#transformers.TokenClassificationPipeline.group_entities) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/token_classification.py#L584)

( entities: list )

Parameters

  * [](#transformers.TokenClassificationPipeline.group_entities.entities) **entities** (`dict`) -- The entities predicted by the pipeline.

Find and group together the adjacent tokens with the same entity predicted.

#### group_sub_entities

[](#transformers.TokenClassificationPipeline.group_sub_entities) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/token_classification.py#L549)

( entities: list )

Parameters

  * [](#transformers.TokenClassificationPipeline.group_sub_entities.entities) **entities** (`dict`) -- The entities predicted by the pipeline.

Group together the adjacent tokens with the same entity predicted.

### [](#transformers.ZeroShotClassificationPipeline) ZeroShotClassificationPipeline

### class transformers.ZeroShotClassificationPipeline

[](#transformers.ZeroShotClassificationPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/zero_shot_classification.py#L44)

( args_parser = <transformers.pipelines.zero_shot_classification.ZeroShotClassificationArgumentHandler object at 0x7f8a4b11c5e0> **kwargs )

Parameters

  * [](#transformers.ZeroShotClassificationPipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.ZeroShotClassificationPipeline.tokenizer) **tokenizer** ([PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend)) -- The tokenizer that will be used by the pipeline to encode data for the model. This object inherits from [PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend).
  * [](#transformers.ZeroShotClassificationPipeline.task) **task** (`str`, defaults to `""`) -- A task-identifier for the pipeline.
  * [](#transformers.ZeroShotClassificationPipeline.num_workers) **num_workers** (`int`, _optional_ , defaults to 8) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the number of workers to be used.
  * [](#transformers.ZeroShotClassificationPipeline.batch_size) **batch_size** (`int`, _optional_ , defaults to 1) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the size of the batch to use, for inference this is not always beneficial, please read [Batching with pipelines](https://huggingface.co/transformers/main_classes/pipelines.html#pipeline-batching) .
  * [](#transformers.ZeroShotClassificationPipeline.args_parser) **args_parser** ([ArgumentHandler](/docs/transformers/v5.8.0/en/internal/pipelines_utils#transformers.pipelines.ArgumentHandler), _optional_) -- Reference to the object in charge of parsing supplied pipeline parameters.
  * [](#transformers.ZeroShotClassificationPipeline.device) **device** (`int`, _optional_ , defaults to -1) -- Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on the associated CUDA device id. You can pass native `torch.device` or a `str` too
  * [](#transformers.ZeroShotClassificationPipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`)
  * [](#transformers.ZeroShotClassificationPipeline.binary_output) **binary_output** (`bool`, _optional_ , defaults to `False`) -- Flag indicating if the output the pipeline should happen in a serialized format (i.e., pickle) or as the raw output data e.g. text.

NLI-based zero-shot classification pipeline using a `ModelForSequenceClassification` trained on NLI (natural language inference) tasks. Equivalent of `text-classification` pipelines, but these models don’t require a hardcoded number of potential classes, they can be chosen at runtime. It usually means it’s slower but it is **much** more flexible.

Any combination of sequences and labels can be passed and each combination will be posed as a premise/hypothesis pair and passed to the pretrained model. Then, the logit for _entailment_ is taken as the logit for the candidate label being valid. Any NLI model can be used, but the id of the _entailment_ label must be included in the model config’s :attr:_~transformers.PreTrainedConfig.label2id_.

[](#transformers.ZeroShotClassificationPipeline.example)

Example:

Copied


    >>> from transformers import pipeline

    >>> oracle = pipeline(model="facebook/bart-large-mnli")
    >>> oracle(
    ...     "I have a problem with my iphone that needs to be resolved asap!!",
    ...     candidate_labels=["urgent", "not urgent", "phone", "tablet", "computer"],
    ... )
    {'sequence': 'I have a problem with my iphone that needs to be resolved asap!!', 'labels': ['urgent', 'phone', 'computer', 'not urgent', 'tablet'], 'scores': [0.504, 0.479, 0.013, 0.003, 0.002]}

    >>> oracle(
    ...     "I have a problem with my iphone that needs to be resolved asap!!",
    ...     candidate_labels=["english", "german"],
    ... )
    {'sequence': 'I have a problem with my iphone that needs to be resolved asap!!', 'labels': ['english', 'german'], 'scores': [0.814, 0.186]}

Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

This NLI pipeline can currently be loaded from [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) using the following task identifier: `"zero-shot-classification"`.

The models that this pipeline can use are models that have been fine-tuned on an NLI task. See the up-to-date list of available models on [huggingface.co/models](https://huggingface.co/models?search=nli).

#### __call__

[](#transformers.ZeroShotClassificationPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/zero_shot_classification.py#L159)

( sequences: str | list[str] *args **kwargs ) → A `dict` or a list of `dict`

Parameters

  * [](#transformers.ZeroShotClassificationPipeline.__call__.sequences) **sequences** (`str` or `list[str]`) -- The sequence(s) to classify, will be truncated if the model input is too large.
  * [](#transformers.ZeroShotClassificationPipeline.__call__.candidate_labels) **candidate_labels** (`str` or `list[str]`) -- The set of possible class labels to classify each sequence into. Can be a single label, a string of comma-separated labels, or a list of labels.
  * [](#transformers.ZeroShotClassificationPipeline.__call__.hypothesis_template) **hypothesis_template** (`str`, _optional_ , defaults to `"This example is {}."`) -- The template used to turn each label into an NLI-style hypothesis. This template must include a {} or similar syntax for the candidate label to be inserted into the template. For example, the default template is `"This example is {}."` With the candidate label `"sports"`, this would be fed into the model like `"<cls> sequence to classify <sep> This example is sports . <sep>"`. The default template works well in many cases, but it may be worthwhile to experiment with different templates depending on the task setting.
  * [](#transformers.ZeroShotClassificationPipeline.__call__.multi_label) **multi_label** (`bool`, _optional_ , defaults to `False`) -- Whether or not multiple candidate labels can be true. If `False`, the scores are normalized such that the sum of the label likelihoods for each sequence is 1. If `True`, the labels are considered independent and probabilities are normalized for each candidate by doing a softmax of the entailment score vs. the contradiction score.

Returns

A `dict` or a list of `dict`

Each result comes as a dictionary with the following keys:

  * **sequence** (`str`) — The sequence for which this is the output.
  * **labels** (`list[str]`) — The labels sorted by order of likelihood.
  * **scores** (`list[float]`) — The probabilities for each of the labels.

Classify the sequence(s) given as inputs. See the [ZeroShotClassificationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.ZeroShotClassificationPipeline) documentation for more information.

## [](#multimodal) Multimodal

Pipelines available for multimodal tasks include the following.

### [](#transformers.DocumentQuestionAnsweringPipeline) DocumentQuestionAnsweringPipeline

### class transformers.DocumentQuestionAnsweringPipeline

[](#transformers.DocumentQuestionAnsweringPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/document_question_answering.py#L206)

( *args **kwargs )

Parameters

  * [](#transformers.DocumentQuestionAnsweringPipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.DocumentQuestionAnsweringPipeline.tokenizer) **tokenizer** ([PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend)) -- The tokenizer that will be used by the pipeline to encode data for the model. This object inherits from [PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend).
  * [](#transformers.DocumentQuestionAnsweringPipeline.image_processor) **image_processor** ([BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor)) -- The image processor that will be used by the pipeline to encode data for the model. This object inherits from [BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor).
  * [](#transformers.DocumentQuestionAnsweringPipeline.task) **task** (`str`, defaults to `""`) -- A task-identifier for the pipeline.
  * [](#transformers.DocumentQuestionAnsweringPipeline.num_workers) **num_workers** (`int`, _optional_ , defaults to 8) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the number of workers to be used.
  * [](#transformers.DocumentQuestionAnsweringPipeline.batch_size) **batch_size** (`int`, _optional_ , defaults to 1) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the size of the batch to use, for inference this is not always beneficial, please read [Batching with pipelines](https://huggingface.co/transformers/main_classes/pipelines.html#pipeline-batching) .
  * [](#transformers.DocumentQuestionAnsweringPipeline.args_parser) **args_parser** ([ArgumentHandler](/docs/transformers/v5.8.0/en/internal/pipelines_utils#transformers.pipelines.ArgumentHandler), _optional_) -- Reference to the object in charge of parsing supplied pipeline parameters.
  * [](#transformers.DocumentQuestionAnsweringPipeline.device) **device** (`int`, _optional_ , defaults to -1) -- Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on the associated CUDA device id. You can pass native `torch.device` or a `str` too
  * [](#transformers.DocumentQuestionAnsweringPipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`)
  * [](#transformers.DocumentQuestionAnsweringPipeline.binary_output) **binary_output** (`bool`, _optional_ , defaults to `False`) -- Flag indicating if the output the pipeline should happen in a serialized format (i.e., pickle) or as the raw output data e.g. text.

Document Question Answering pipeline using any `AutoModelForDocumentQuestionAnswering`. The inputs/outputs are similar to the (extractive) question answering pipeline; however, the pipeline takes an image (and optional OCR’d words/boxes) as input instead of text context.

Unless the model you’re using explicitly sets these generation parameters in its configuration files (`generation_config.json`), the following default values will be used:

  * max_new_tokens: 256

[](#transformers.DocumentQuestionAnsweringPipeline.example)

Example:

Copied


    >>> from transformers import pipeline

    >>> document_qa = pipeline(model="impira/layoutlm-document-qa")
    >>> document_qa(
    ...     image="https://huggingface.co/spaces/impira/docquery/resolve/2359223c1837a7587402bda0f2643382a6eefeab/invoice.png",
    ...     question="What is the invoice number?",
    ... )
    [{'score': 0.425, 'answer': 'us-001', 'start': 16, 'end': 16}]

Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

This document question answering pipeline can currently be loaded from [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) using the following task identifier: `"document-question-answering"`.

The models that this pipeline can use are models that have been fine-tuned on a document question answering task. See the up-to-date list of available models on [huggingface.co/models](https://huggingface.co/models?filter=document-question-answering).

#### __call__

[](#transformers.DocumentQuestionAnsweringPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/document_question_answering.py#L336)

( image: typing.Union[ForwardRef('Image.Image'), str, list[dict[str, typing.Any]]] question: str | None = None word_boxes: tuple[str, list[float]] | None = None **kwargs: typing.Any ) → A `dict` or a list of `dict`

Parameters

  * [](#transformers.DocumentQuestionAnsweringPipeline.__call__.image) **image** (`str` or `PIL.Image`) -- The pipeline handles three types of images:

    * A string containing a http link pointing to an image
    * A string containing a local path to an image
    * An image loaded in PIL directly

The pipeline accepts either a single image or a batch of images. If given a single image, it can be broadcasted to multiple questions.
  * [](#transformers.DocumentQuestionAnsweringPipeline.__call__.question) **question** (`str`) -- A question to ask of the document.
  * [](#transformers.DocumentQuestionAnsweringPipeline.__call__.word_boxes) **word_boxes** (`list[str, tuple[float, float, float, float]]`, _optional_) -- A list of words and bounding boxes (normalized 0->1000). If you provide this optional input, then the pipeline will use these words and boxes instead of running OCR on the image to derive them for models that need them (e.g. LayoutLM). This allows you to reuse OCR'd results across many invocations of the pipeline without having to re-run it each time.
  * [](#transformers.DocumentQuestionAnsweringPipeline.__call__.top_k) **top_k** (`int`, _optional_ , defaults to 1) -- The number of answers to return (will be chosen by order of likelihood). Note that we return less than top_k answers if there are not enough options available within the context.
  * [](#transformers.DocumentQuestionAnsweringPipeline.__call__.doc_stride) **doc_stride** (`int`, _optional_ , defaults to 128) -- If the words in the document are too long to fit with the question for the model, it will be split in several chunks with some overlap. This argument controls the size of that overlap.
  * [](#transformers.DocumentQuestionAnsweringPipeline.__call__.max_answer_len) **max_answer_len** (`int`, _optional_ , defaults to 15) -- The maximum length of predicted answers (e.g., only answers with a shorter length are considered).
  * [](#transformers.DocumentQuestionAnsweringPipeline.__call__.max_seq_len) **max_seq_len** (`int`, _optional_ , defaults to 384) -- The maximum length of the total sentence (context + question) in tokens of each chunk passed to the model. The context will be split in several chunks (using `doc_stride` as overlap) if needed.
  * [](#transformers.DocumentQuestionAnsweringPipeline.__call__.max_question_len) **max_question_len** (`int`, _optional_ , defaults to 64) -- The maximum length of the question after tokenization. It will be truncated if needed.
  * [](#transformers.DocumentQuestionAnsweringPipeline.__call__.handle_impossible_answer) **handle_impossible_answer** (`bool`, _optional_ , defaults to `False`) -- Whether or not we accept impossible as an answer.
  * [](#transformers.DocumentQuestionAnsweringPipeline.__call__.lang) **lang** (`str`, _optional_) -- Language to use while running OCR. Defaults to english.
  * [](#transformers.DocumentQuestionAnsweringPipeline.__call__.tesseract_config) **tesseract_config** (`str`, _optional_) -- Additional flags to pass to tesseract while running OCR.
  * [](#transformers.DocumentQuestionAnsweringPipeline.__call__.timeout) **timeout** (`float`, _optional_ , defaults to None) -- The maximum time in seconds to wait for fetching images from the web. If None, no timeout is set and the call may block forever.

Returns

A `dict` or a list of `dict`

Each result comes as a dictionary with the following keys:

  * **score** (`float`) — The probability associated to the answer.
  * **start** (`int`) — The start word index of the answer (in the OCR’d version of the input or provided `word_boxes`).
  * **end** (`int`) — The end word index of the answer (in the OCR’d version of the input or provided `word_boxes`).
  * **answer** (`str`) — The answer to the question.
  * **words** (`list[int]`) — The index of each word/box pair that is in the answer

Answer the question(s) given as inputs by using the document(s). A document is defined as an image and an optional list of (word, box) tuples which represent the text in the document. If the `word_boxes` are not provided, it will use the Tesseract OCR engine (if available) to extract the words and boxes automatically for LayoutLM-like models which require them as input. For Donut, no OCR is run.

You can invoke the pipeline several ways:

  * `pipeline(image=image, question=question)`
  * `pipeline(image=image, question=question, word_boxes=word_boxes)`
  * `pipeline([{"image": image, "question": question}])`
  * `pipeline([{"image": image, "question": question, "word_boxes": word_boxes}])`

### [](#transformers.FeatureExtractionPipeline) FeatureExtractionPipeline

### class transformers.FeatureExtractionPipeline

[](#transformers.FeatureExtractionPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/feature_extraction.py#L15)

( model: PreTrainedModel tokenizer: PreTrainedTokenizer | None = None feature_extractor: PreTrainedFeatureExtractor | None = None image_processor: BaseImageProcessor | None = None processor: ProcessorMixin | None = None task: str = '' device: int | torch.device | None = None binary_output: bool = False **kwargs )

Parameters

  * [](#transformers.FeatureExtractionPipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.FeatureExtractionPipeline.tokenizer) **tokenizer** ([PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend)) -- The tokenizer that will be used by the pipeline to encode data for the model. This object inherits from [PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend).
  * [](#transformers.FeatureExtractionPipeline.task) **task** (`str`, defaults to `""`) -- A task-identifier for the pipeline.
  * [](#transformers.FeatureExtractionPipeline.num_workers) **num_workers** (`int`, _optional_ , defaults to 8) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the number of workers to be used.
  * [](#transformers.FeatureExtractionPipeline.batch_size) **batch_size** (`int`, _optional_ , defaults to 1) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the size of the batch to use, for inference this is not always beneficial, please read [Batching with pipelines](https://huggingface.co/transformers/main_classes/pipelines.html#pipeline-batching) .
  * [](#transformers.FeatureExtractionPipeline.args_parser) **args_parser** ([ArgumentHandler](/docs/transformers/v5.8.0/en/internal/pipelines_utils#transformers.pipelines.ArgumentHandler), _optional_) -- Reference to the object in charge of parsing supplied pipeline parameters.
  * [](#transformers.FeatureExtractionPipeline.device) **device** (`int`, _optional_ , defaults to -1) -- Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on the associated CUDA device id. You can pass native `torch.device` or a `str` too
  * [](#transformers.FeatureExtractionPipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`)
  * [](#transformers.FeatureExtractionPipeline.tokenize_kwargs) **tokenize_kwargs** (`dict`, _optional_) -- Additional dictionary of keyword arguments passed along to the tokenizer.
  * [](#transformers.FeatureExtractionPipeline.return_tensors) **return_tensors** (`bool`, _optional_) -- If `True`, returns a tensor according to the specified framework, otherwise returns a list.

Feature extraction pipeline uses no model head. This pipeline extracts the hidden states from the base transformer, which can be used as features in downstream tasks.

[](#transformers.FeatureExtractionPipeline.example)

Example:

Copied


    >>> from transformers import pipeline

    >>> extractor = pipeline(model="google-bert/bert-base-uncased", task="feature-extraction")
    >>> result = extractor("This is a simple test.", return_tensors=True)
    >>> result.shape  # This is a tensor of shape [1, sequence_length, hidden_dimension] representing the input string.
    torch.Size([1, 8, 768])

Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

This feature extraction pipeline can currently be loaded from [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) using the task identifier: `"feature-extraction"`.

All models may be used for this pipeline. See a list of all models, including community-contributed models on [huggingface.co/models](https://huggingface.co/models).

#### __call__

[](#transformers.FeatureExtractionPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/feature_extraction.py#L78)

( *args: str | list[str] **kwargs: typing.Any ) → A nested list of `float`

Parameters

  * [](#transformers.FeatureExtractionPipeline.__call__.args) **args** (`str` or `list[str]`) -- One or several texts (or one list of texts) to get the features of.

Returns

A nested list of `float`

The features computed by the model.

Extract the features of the input(s) text.

### [](#transformers.ImageFeatureExtractionPipeline) ImageFeatureExtractionPipeline

### class transformers.ImageFeatureExtractionPipeline

[](#transformers.ImageFeatureExtractionPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/image_feature_extraction.py#L23)

( model: PreTrainedModel tokenizer: PreTrainedTokenizer | None = None feature_extractor: PreTrainedFeatureExtractor | None = None image_processor: BaseImageProcessor | None = None processor: ProcessorMixin | None = None task: str = '' device: int | torch.device | None = None binary_output: bool = False **kwargs )

Parameters

  * [](#transformers.ImageFeatureExtractionPipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.ImageFeatureExtractionPipeline.image_processor) **image_processor** ([BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor)) -- The image processor that will be used by the pipeline to encode data for the model. This object inherits from [BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor).
  * [](#transformers.ImageFeatureExtractionPipeline.task) **task** (`str`, defaults to `""`) -- A task-identifier for the pipeline.
  * [](#transformers.ImageFeatureExtractionPipeline.num_workers) **num_workers** (`int`, _optional_ , defaults to 8) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the number of workers to be used.
  * [](#transformers.ImageFeatureExtractionPipeline.batch_size) **batch_size** (`int`, _optional_ , defaults to 1) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the size of the batch to use, for inference this is not always beneficial, please read [Batching with pipelines](https://huggingface.co/transformers/main_classes/pipelines.html#pipeline-batching) .
  * [](#transformers.ImageFeatureExtractionPipeline.args_parser) **args_parser** ([ArgumentHandler](/docs/transformers/v5.8.0/en/internal/pipelines_utils#transformers.pipelines.ArgumentHandler), _optional_) -- Reference to the object in charge of parsing supplied pipeline parameters.
  * [](#transformers.ImageFeatureExtractionPipeline.device) **device** (`int`, _optional_ , defaults to -1) -- Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on the associated CUDA device id. You can pass native `torch.device` or a `str` too
  * [](#transformers.ImageFeatureExtractionPipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`)
  * [](#transformers.ImageFeatureExtractionPipeline.binary_output) **binary_output** (`bool`, _optional_ , defaults to `False`) -- Flag indicating if the output the pipeline should happen in a serialized format (i.e., pickle) or as the raw output data e.g. text.
  * [](#transformers.ImageFeatureExtractionPipeline.image_processor_kwargs) **image_processor_kwargs** (`dict`, _optional_) -- Additional dictionary of keyword arguments passed along to the image processor e.g. {"size": {"height": 100, "width": 100}‌}
  * [](#transformers.ImageFeatureExtractionPipeline.pool) **pool** (`bool`, _optional_ , defaults to `False`) -- Whether or not to return the pooled output. If `False`, the model will return the raw hidden states.

Image feature extraction pipeline uses no model head. This pipeline extracts the hidden states from the base transformer, which can be used as features in downstream tasks.

[](#transformers.ImageFeatureExtractionPipeline.example)

Example:

Copied


    >>> from transformers import pipeline

    >>> extractor = pipeline(model="google/vit-base-patch16-224", task="image-feature-extraction")
    >>> result = extractor("https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png", return_tensors=True)
    >>> result.shape  # This is a tensor of shape [1, sequence_length, hidden_dimension] representing the input image.
    torch.Size([1, 197, 768])

Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

This image feature extraction pipeline can currently be loaded from [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) using the task identifier: `"image-feature-extraction"`.

All vision models may be used for this pipeline. See a list of all models, including community-contributed models on [huggingface.co/models](https://huggingface.co/models).

#### __call__

[](#transformers.ImageFeatureExtractionPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/image_feature_extraction.py#L94)

( *args: typing.Union[str, ForwardRef('Image.Image'), list['Image.Image'], list[str]] **kwargs: typing.Any ) → A nested list of `float`

Parameters

  * [](#transformers.ImageFeatureExtractionPipeline.__call__.images) **images** (`str`, `list[str]`, `PIL.Image` or `list[PIL.Image]`) -- The pipeline handles three types of images:

    * A string containing a http link pointing to an image
    * A string containing a local path to an image
    * An image loaded in PIL directly

The pipeline accepts either a single image or a batch of images, which must then be passed as a string. Images in a batch must all be in the same format: all as http links, all as local paths, or all as PIL images.
  * [](#transformers.ImageFeatureExtractionPipeline.__call__.timeout) **timeout** (`float`, _optional_ , defaults to None) -- The maximum time in seconds to wait for fetching images from the web. If None, no timeout is used and the call may block forever.

Returns

A nested list of `float`

The features computed by the model.

Extract the features of the input(s).

### [](#transformers.ImageTextToTextPipeline) ImageTextToTextPipeline

### class transformers.ImageTextToTextPipeline

[](#transformers.ImageTextToTextPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/image_text_to_text.py#L53)

( *args **kwargs )

Parameters

  * [](#transformers.ImageTextToTextPipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.ImageTextToTextPipeline.processor) **processor** ([ProcessorMixin](/docs/transformers/v5.8.0/en/main_classes/processors#transformers.ProcessorMixin)) -- The processor that will be used by the pipeline to encode data for the model. This object inherits from [ProcessorMixin](/docs/transformers/v5.8.0/en/main_classes/processors#transformers.ProcessorMixin). Processor is a composite object that might contain `tokenizer`, `feature_extractor`, and `image_processor`.
  * [](#transformers.ImageTextToTextPipeline.task) **task** (`str`, defaults to `""`) -- A task-identifier for the pipeline.
  * [](#transformers.ImageTextToTextPipeline.num_workers) **num_workers** (`int`, _optional_ , defaults to 8) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the number of workers to be used.
  * [](#transformers.ImageTextToTextPipeline.batch_size) **batch_size** (`int`, _optional_ , defaults to 1) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the size of the batch to use, for inference this is not always beneficial, please read [Batching with pipelines](https://huggingface.co/transformers/main_classes/pipelines.html#pipeline-batching) .
  * [](#transformers.ImageTextToTextPipeline.args_parser) **args_parser** ([ArgumentHandler](/docs/transformers/v5.8.0/en/internal/pipelines_utils#transformers.pipelines.ArgumentHandler), _optional_) -- Reference to the object in charge of parsing supplied pipeline parameters.
  * [](#transformers.ImageTextToTextPipeline.device) **device** (`int`, _optional_ , defaults to -1) -- Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on the associated CUDA device id. You can pass native `torch.device` or a `str` too
  * [](#transformers.ImageTextToTextPipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`)
  * [](#transformers.ImageTextToTextPipeline.binary_output) **binary_output** (`bool`, _optional_ , defaults to `False`) -- Flag indicating if the output the pipeline should happen in a serialized format (i.e., pickle) or as the raw output data e.g. text.

Image-text-to-text pipeline using an `AutoModelForImageTextToText`. This pipeline generates text given an image and text. When the underlying model is a conversational model, it can also accept one or more chats, in which case the pipeline will operate in chat mode and will continue the chat(s) by adding its response(s). Each chat takes the form of a list of dicts, where each dict contains “role” and “content” keys.

Unless the model you’re using explicitly sets these generation parameters in its configuration files (`generation_config.json`), the following default values will be used:

  * max_new_tokens: 256

[](#transformers.ImageTextToTextPipeline.example)

Example:

Copied


    >>> from transformers import pipeline

    >>> pipe = pipeline(task="image-text-to-text", model="Salesforce/blip-image-captioning-base")
    >>> pipe("https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png", text="A photo of")
    [{'generated_text': 'a photo of two birds'}]

[](#transformers.ImageTextToTextPipeline.example-2)

Copied


    >>> from transformers import pipeline

    >>> pipe = pipeline("image-text-to-text", model="llava-hf/llava-interleave-qwen-0.5b-hf")
    >>> messages = [
    >>>     {
    >>>         "role": "user",
    >>>         "content": [
    >>>             {
    >>>                 "type": "image",
    >>>                 "url": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg",
    >>>             },
    >>>             {"type": "text", "text": "Describe this image."},
    >>>         ],
    >>>     },
    >>>     {
    >>>         "role": "assistant",
    >>>         "content": [
    >>>             {"type": "text", "text": "There is a dog and"},
    >>>         ],
    >>>     },
    >>> ]
    >>> pipe(text=messages, max_new_tokens=20, return_full_text=False)
    [{'input_text': [{'role': 'user',
        'content': [{'type': 'image',
        'url': 'https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg'},
        {'type': 'text', 'text': 'Describe this image.'}]},
    {'role': 'assistant',
        'content': [{'type': 'text', 'text': 'There is a dog and'}]}],
    'generated_text': ' a person in the image. The dog is sitting on the sand, and the person is sitting on'}]

Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

This image-text to text pipeline can currently be loaded from pipeline() using the following task identifier: “image-text-to-text”.

See the list of available models on [huggingface.co/models](https://huggingface.co/models?pipeline_tag=image-text-to-text).

#### __call__

[](#transformers.ImageTextToTextPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/image_text_to_text.py#L216)

( images: typing.Union[str, list[str], list[list[str]], ForwardRef('Image.Image'), list['Image.Image'], list[list['Image.Image']], list[dict], NoneType] = None text: str | list[str] | list[dict] | None = None **kwargs ) → A list or a list of list of `dict`

Parameters

  * [](#transformers.ImageTextToTextPipeline.__call__.images) **images** (`str`, `list[str]`, `PIL.Image, `list[PIL.Image]`, `list[dict[str, Union[str, PIL.Image]]]`) -- The pipeline handles three types of images:

    * A string containing a HTTP(s) link pointing to an image
    * A string containing a local path to an image
    * An image loaded in PIL directly

The pipeline accepts either a single image or a batch of images. Finally, this pipeline also supports the chat format (see `text`) containing images and text in this argument.
  * [](#transformers.ImageTextToTextPipeline.__call__.text) **text** (str, list[str], `list[dict[str, Union[str, PIL.Image]]]`) -- The text to be used for generation. If a list of strings is passed, the length of the list should be the same as the number of images. Text can also follow the chat format: a list of dictionaries where each dictionary represents a message in a conversation. Each dictionary should have two keys: 'role' and 'content'. 'role' should be one of 'user', 'system' or 'assistant'. 'content' should be a list of dictionary containing the text of the message and the type of the message. The type of the message can be either 'text' or 'image'. If the type is 'image', no text is needed.
  * [](#transformers.ImageTextToTextPipeline.__call__.return_tensors) **return_tensors** (`bool`, _optional_ , defaults to `False`) -- Returns the tensors of predictions (as token indices) in the outputs. If set to `True`, the decoded text is not returned.
  * [](#transformers.ImageTextToTextPipeline.__call__.return_text) **return_text** (`bool`, _optional_) -- Returns the decoded texts in the outputs.
  * [](#transformers.ImageTextToTextPipeline.__call__.return_full_text) **return_full_text** (`bool`, _optional_ , defaults to `True`) -- If set to `False` only added text is returned, otherwise the full text is returned. Cannot be specified at the same time as `return_text`.
  * [](#transformers.ImageTextToTextPipeline.__call__.clean_up_tokenization_spaces) **clean_up_tokenization_spaces** (`bool`, _optional_ , defaults to `True`) -- Whether or not to clean up the potential extra spaces in the text output.
  * [](#transformers.ImageTextToTextPipeline.__call__.continue_final_message\() **continue_final_message(** `bool`, _optional_) -- This indicates that you want the model to continue the last message in the input chat rather than starting a new one, allowing you to "prefill" its response. By default this is `True` when the final message in the input chat has the `assistant` role and `False` otherwise, but you can manually override that behaviour by setting this flag.

Returns

A list or a list of list of `dict`

Each result comes as a dictionary with the following key (cannot return a combination of both `generated_text` and `generated_token_ids`):

  * **generated_text** (`str`, present when `return_text=True`) — The generated text.
  * **generated_token_ids** (`torch.Tensor`, present when `return_tensors=True`) — The token ids of the generated text.
  * **input_text** (`str`) — The input text.

Generate a text given text and the image(s) passed as inputs.

### [](#transformers.AnyToAnyPipeline) AnyToAnyPipeline

### class transformers.AnyToAnyPipeline

[](#transformers.AnyToAnyPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/any_to_any.py#L67)

( *args **kwargs )

Parameters

  * [](#transformers.AnyToAnyPipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.AnyToAnyPipeline.processor) **processor** ([ProcessorMixin](/docs/transformers/v5.8.0/en/main_classes/processors#transformers.ProcessorMixin)) -- The processor that will be used by the pipeline to encode data for the model. This object inherits from [ProcessorMixin](/docs/transformers/v5.8.0/en/main_classes/processors#transformers.ProcessorMixin). Processor is a composite object that might contain `tokenizer`, `feature_extractor`, and `image_processor`.
  * [](#transformers.AnyToAnyPipeline.task) **task** (`str`, defaults to `""`) -- A task-identifier for the pipeline.
  * [](#transformers.AnyToAnyPipeline.num_workers) **num_workers** (`int`, _optional_ , defaults to 8) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the number of workers to be used.
  * [](#transformers.AnyToAnyPipeline.batch_size) **batch_size** (`int`, _optional_ , defaults to 1) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the size of the batch to use, for inference this is not always beneficial, please read [Batching with pipelines](https://huggingface.co/transformers/main_classes/pipelines.html#pipeline-batching) .
  * [](#transformers.AnyToAnyPipeline.args_parser) **args_parser** ([ArgumentHandler](/docs/transformers/v5.8.0/en/internal/pipelines_utils#transformers.pipelines.ArgumentHandler), _optional_) -- Reference to the object in charge of parsing supplied pipeline parameters.
  * [](#transformers.AnyToAnyPipeline.device) **device** (`int`, _optional_ , defaults to -1) -- Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on the associated CUDA device id. You can pass native `torch.device` or a `str` too
  * [](#transformers.AnyToAnyPipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`)
  * [](#transformers.AnyToAnyPipeline.binary_output) **binary_output** (`bool`, _optional_ , defaults to `False`) -- Flag indicating if the output the pipeline should happen in a serialized format (i.e., pickle) or as the raw output data e.g. text.

Multimodal Generation pipeline using an `AutoModelForMultimodalLM`. This pipeline generates text given any combination of multimodal data and text.When the underlying model is a conversational model, it can also accept one or more chats, in which case the pipeline will operate in chat mode and will continue the chat(s) by adding its response(s). Each chat takes the form of a list of dicts, where each dict contains “role” and “content” keys.

Unless the model you’re using explicitly sets these generation parameters in its configuration files (`generation_config.json`), the following default values will be used:

  * max_new_tokens: 256

[](#transformers.AnyToAnyPipeline.example)

Example:

Copied


    >>> from transformers import pipeline

    >>> pipe = pipeline(task="any-to-any", model="google/gemma-3n-E4B-it")
    >>> pipe("https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png", text="A photo of")
    [{'generated_text': 'a photo of two birds'}]

[](#transformers.AnyToAnyPipeline.example-2)

Copied


    >>> from transformers import pipeline

    >>> pipe = pipeline("any-to-any", model="google/gemma-3n-E4B-it")
    >>> messages = [
    >>>     {
    >>>         "role": "user",
    >>>         "content": [
    >>>             {
    >>>                 "type": "image",
    >>>                 "url": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg",
    >>>             },
    >>>             {"type": "text", "text": "Describe this image."},
    >>>         ],
    >>>     },
    >>>     {
    >>>         "role": "assistant",
    >>>         "content": [
    >>>             {"type": "text", "text": "There is a dog and"},
    >>>         ],
    >>>     },
    >>> ]
    >>> pipe(text=messages, max_new_tokens=20, return_full_text=False)
    [{'input_text': [{'role': 'user',
        'content': [{'type': 'image',
        'url': 'https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg'},
        {'type': 'text', 'text': 'Describe this image.'}]},
    {'role': 'assistant',
        'content': [{'type': 'text', 'text': 'There is a dog and'}]}],
    'generated_text': ' a person in the image. The dog is sitting on the sand, and the person is sitting on'}]

Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

This multimodal pipeline can currently be loaded from pipeline() using the following task identifier: “any-to-any”.

See the list of available models on [huggingface.co/models](https://huggingface.co/models?pipeline_tag=any-to-any).

#### __call__

[](#transformers.AnyToAnyPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/any_to_any.py#L258)

( text: str | list[str] | list[dict] images: typing.Union[str, list[str], list[list[str]], ForwardRef('PIL.Image.Image'), numpy.ndarray, ForwardRef('torch.Tensor'), list['PIL.Image.Image'], list[numpy.ndarray], list['torch.Tensor'], NoneType] = None videos: typing.Union[str, list[str], list['PIL.Image.Image'], numpy.ndarray, ForwardRef('torch.Tensor'), list[numpy.ndarray], list['torch.Tensor'], list[list['PIL.Image.Image']], list[list[numpy.ndarray]], list[list['torch.Tensor']], transformers.video_utils.URL, list[transformers.video_utils.URL], list[list[transformers.video_utils.URL]], transformers.video_utils.Path, list[transformers.video_utils.Path], list[list[transformers.video_utils.Path]], NoneType] = None audio: typing.Union[str, list[str], numpy.ndarray, ForwardRef('torch.Tensor'), collections.abc.Sequence[numpy.ndarray], collections.abc.Sequence['torch.Tensor'], NoneType] = None **kwargs ) → A list or a list of list of `dict`

Parameters

  * [](#transformers.AnyToAnyPipeline.__call__.text) **text** (`str`, `list[str]`, `list[dict]`) -- The text to be used for generation. If a list of strings is passed, the length of the list should be the same as the number of images. Text can also follow the chat format: a list of dictionaries where each dictionary represents a message in a conversation. Each dictionary should have two keys: 'role' and 'content'. 'role' should be one of 'user', 'system' or 'assistant'. 'content' should be a list of dictionary containing the text of the message and the type of the message.
  * [](#transformers.AnyToAnyPipeline.__call__.images) **images** (`str`, `list[str]`, `ImageInput`) -- The pipeline handles three types of images:

    * A string containing a HTTP(s) link pointing to an image
    * A string containing a local path to an image
    * An image loaded in PIL directly

The pipeline accepts either a single image or a batch of images. Finally, this pipeline also supports the chat format (see `text`) containing images and text in this argument.
  * [](#transformers.AnyToAnyPipeline.__call__.videos) **videos** (`str`, `list[str]`, `VideoInput`) -- The pipeline handles three types of videos:

    * A string containing a HTTP(s) link pointing to a video
    * A string containing a local path to a video
    * A video loaded and decoded to array format

The pipeline accepts either a single video or a batch of videos. Finally, this pipeline also supports the chat format (see `text`) containing videos and text in this argument.
  * [](#transformers.AnyToAnyPipeline.__call__.audio) **audio** (`str`, `list[str]`, `AudioInput`) -- The pipeline handles three types of audios:

    * A string containing a HTTP(s) link pointing to an audio
    * A string containing a local path to an audio
    * An audio loaded in PIL directly

The pipeline accepts either a single audios or a batch of audios. Finally, this pipeline also supports the chat format (see `text`) containing audios and text in this argument.
  * [](#transformers.AnyToAnyPipeline.__call__.return_tensors) **return_tensors** (`bool`, _optional_ , defaults to `False`) -- Returns the tensors of predictions (as token indices) in the outputs. If set to `True`, the decoded text is not returned.
  * [](#transformers.AnyToAnyPipeline.__call__.return_text) **return_text** (`bool`, _optional_) -- Returns the decoded texts in the outputs.
  * [](#transformers.AnyToAnyPipeline.__call__.return_full_text) **return_full_text** (`bool`, _optional_ , defaults to `True`) -- If set to `False` only added text is returned, otherwise the full text is returned. Cannot be specified at the same time as `return_text`.
  * [](#transformers.AnyToAnyPipeline.__call__.clean_up_tokenization_spaces) **clean_up_tokenization_spaces** (`bool`, _optional_ , defaults to `True`) -- Whether or not to clean up the potential extra spaces in the text output.
  * [](#transformers.AnyToAnyPipeline.__call__.continue_final_message\() **continue_final_message(** `bool`, _optional_) -- This indicates that you want the model to continue the last message in the input chat rather than starting a new one, allowing you to "prefill" its response. By default this is `True` when the final message in the input chat has the `assistant` role and `False` otherwise, but you can manually override that behaviour by setting this flag.

Returns

A list or a list of list of `dict`

Each result comes as a dictionary with the following key (cannot return a combination of both `generated_text` and `generated_token_ids`):

  * **generated_text** (`str`, present when `return_text=True` and `generation_mode="text"`) — The generated text.
  * **generated_audio** (`np.ndarray`, present when `generation_mode="audio"`) — The generated audio.
  * **generated_image** (`PIL.Image.Image`, present when `generation_mode="image"`) — The generated image.
  * **generated_token_ids** (`torch.Tensor`, present when `return_tensors=True` and `generation_mode="text"`) — The token ids of the generated text.
  * **input_text** (`str`) — The input text.

Generate a text given text and optionally multimodal data passed as inputs.

### [](#transformers.MaskGenerationPipeline) MaskGenerationPipeline

### class transformers.MaskGenerationPipeline

[](#transformers.MaskGenerationPipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/mask_generation.py#L36)

( **kwargs )

Parameters

  * [](#transformers.MaskGenerationPipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.MaskGenerationPipeline.image_processor) **image_processor** ([BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor)) -- The image processor that will be used by the pipeline to encode data for the model. This object inherits from [BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor).
  * [](#transformers.MaskGenerationPipeline.task) **task** (`str`, defaults to `""`) -- A task-identifier for the pipeline.
  * [](#transformers.MaskGenerationPipeline.num_workers) **num_workers** (`int`, _optional_ , defaults to 8) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the number of workers to be used.
  * [](#transformers.MaskGenerationPipeline.batch_size) **batch_size** (`int`, _optional_ , defaults to 1) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the size of the batch to use, for inference this is not always beneficial, please read [Batching with pipelines](https://huggingface.co/transformers/main_classes/pipelines.html#pipeline-batching) .
  * [](#transformers.MaskGenerationPipeline.args_parser) **args_parser** ([ArgumentHandler](/docs/transformers/v5.8.0/en/internal/pipelines_utils#transformers.pipelines.ArgumentHandler), _optional_) -- Reference to the object in charge of parsing supplied pipeline parameters.
  * [](#transformers.MaskGenerationPipeline.device) **device** (`int`, _optional_ , defaults to -1) -- Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on the associated CUDA device id. You can pass native `torch.device` or a `str` too
  * [](#transformers.MaskGenerationPipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`)
  * [](#transformers.MaskGenerationPipeline.binary_output) **binary_output** (`bool`, _optional_ , defaults to `False`) -- Flag indicating if the output the pipeline should happen in a serialized format (i.e., pickle) or as the raw output data e.g. text.
  * [](#transformers.MaskGenerationPipeline.points_per_batch) **points_per_batch** (_optional_ , int, default to 64) -- Sets the number of points run simultaneously by the model. Higher numbers may be faster but use more GPU memory.
  * [](#transformers.MaskGenerationPipeline.output_bboxes_mask) **output_bboxes_mask** (`bool`, _optional_ , default to `False`) -- Whether or not to output the bounding box predictions.
  * [](#transformers.MaskGenerationPipeline.output_rle_masks) **output_rle_masks** (`bool`, _optional_ , default to `False`) -- Whether or not to output the masks in `RLE` format

Automatic mask generation for images using `SamForMaskGeneration`. This pipeline predicts binary masks for an image, given an image. It is a `ChunkPipeline` because you can separate the points in a mini-batch in order to avoid OOM issues. Use the `points_per_batch` argument to control the number of points that will be processed at the same time. Default is `64`.

The pipeline works in 3 steps:

  1. `preprocess`: A grid of 1024 points evenly separated is generated along with bounding boxes and point labels. For more details on how the points and bounding boxes are created, check the `_generate_crop_boxes` function. The image is also preprocessed using the `image_processor`. This function `yields` a minibatch of `points_per_batch`.

  2. `forward`: feeds the outputs of `preprocess` to the model. The image embedding is computed only once. Calls both `self.model.get_image_embeddings` and makes sure that the gradients are not computed, and the tensors and models are on the same device.

  3. `postprocess`: The most important part of the automatic mask generation happens here. Three steps are induced:

     * image_processor.postprocess_masks (run on each minibatch loop): takes in the raw output masks, resizes them according to the image size, and transforms there to binary masks.
     * image_processor.filter_masks (on each minibatch loop): uses both `pred_iou_thresh` and `stability_scores`. Also applies a variety of filters based on non maximum suppression to remove bad masks.
     * image_processor.postprocess_masks_for_amg applies the NSM on the mask to only keep relevant ones.

[](#transformers.MaskGenerationPipeline.example)

Example:

Copied


    >>> from transformers import pipeline

    >>> generator = pipeline(model="facebook/sam-vit-base", task="mask-generation")
    >>> outputs = generator(
    ...     "http://images.cocodataset.org/val2017/000000039769.jpg",
    ... )

    >>> outputs = generator(
    ...     "https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png", points_per_batch=128
    ... )

Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

This segmentation pipeline can currently be loaded from [pipeline()](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.pipeline) using the following task identifier: `"mask-generation"`.

See the list of available models on [huggingface.co/models](https://huggingface.co/models?filter=mask-generation).

#### __call__

[](#transformers.MaskGenerationPipeline.__call__) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/mask_generation.py#L143)

( image: typing.Union[str, ForwardRef('Image.Image'), list[str], list['Image.Image']] *args: typing.Any **kwargs: typing.Any ) → `Dict`

Parameters

  * [](#transformers.MaskGenerationPipeline.__call__.image) **image** (`str`, `List[str]`, `PIL.Image` or `List[PIL.Image]`) -- Image or list of images.
  * [](#transformers.MaskGenerationPipeline.__call__.mask_threshold) **mask_threshold** (`float`, _optional_ , defaults to 0.0) -- Threshold to use when turning the predicted masks into binary values.
  * [](#transformers.MaskGenerationPipeline.__call__.pred_iou_thresh) **pred_iou_thresh** (`float`, _optional_ , defaults to 0.88) -- A filtering threshold in `[0,1]` applied on the model's predicted mask quality.
  * [](#transformers.MaskGenerationPipeline.__call__.stability_score_thresh) **stability_score_thresh** (`float`, _optional_ , defaults to 0.95) -- A filtering threshold in `[0,1]`, using the stability of the mask under changes to the cutoff used to binarize the model's mask predictions.
  * [](#transformers.MaskGenerationPipeline.__call__.stability_score_offset) **stability_score_offset** (`int`, _optional_ , defaults to 1) -- The amount to shift the cutoff when calculated the stability score.
  * [](#transformers.MaskGenerationPipeline.__call__.crops_nms_thresh) **crops_nms_thresh** (`float`, _optional_ , defaults to 0.7) -- The box IoU cutoff used by non-maximal suppression to filter duplicate masks.
  * [](#transformers.MaskGenerationPipeline.__call__.crops_n_layers) **crops_n_layers** (`int`, _optional_ , defaults to 0) -- If `crops_n_layers>0`, mask prediction will be run again on crops of the image. Sets the number of layers to run, where each layer has 2**i_layer number of image crops.
  * [](#transformers.MaskGenerationPipeline.__call__.crop_overlap_ratio) **crop_overlap_ratio** (`float`, _optional_ , defaults to `512 / 1500`) -- Sets the degree to which crops overlap. In the first crop layer, crops will overlap by this fraction of the image length. Later layers with more crops scale down this overlap.
  * [](#transformers.MaskGenerationPipeline.__call__.crop_n_points_downscale_factor) **crop_n_points_downscale_factor** (`int`, _optional_ , defaults to `1`) -- The number of points-per-side sampled in layer n is scaled down by crop_n_points_downscale_factor**n.
  * [](#transformers.MaskGenerationPipeline.__call__.timeout) **timeout** (`float`, _optional_ , defaults to None) -- The maximum time in seconds to wait for fetching images from the web. If None, no timeout is set and the call may block forever.

Returns

`Dict`

A dictionary with the following keys:

  * **mask** (`PIL.Image`) — A binary mask of the detected object as a PIL Image of shape `(width, height)` of the original image. Returns a mask filled with zeros if no object is found.
  * **score** (_optional_ `float`) — Optionally, when the model is capable of estimating a confidence of the “object” described by the label and the mask.

Generates binary segmentation masks

## [](#transformers.Pipeline) Parent class: Pipeline

### class transformers.Pipeline

[](#transformers.Pipeline) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/base.py#L739)

( model: PreTrainedModel tokenizer: PreTrainedTokenizer | None = None feature_extractor: PreTrainedFeatureExtractor | None = None image_processor: BaseImageProcessor | None = None processor: ProcessorMixin | None = None task: str = '' device: int | torch.device | None = None binary_output: bool = False **kwargs )

Parameters

  * [](#transformers.Pipeline.model) **model** ([PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel)) -- The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from [PreTrainedModel](/docs/transformers/v5.8.0/en/main_classes/model#transformers.PreTrainedModel).
  * [](#transformers.Pipeline.tokenizer) **tokenizer** ([PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend)) -- The tokenizer that will be used by the pipeline to encode data for the model. This object inherits from [PreTrainedTokenizer](/docs/transformers/v5.8.0/en/main_classes/tokenizer#transformers.PythonBackend).
  * [](#transformers.Pipeline.feature_extractor) **feature_extractor** ([SequenceFeatureExtractor](/docs/transformers/v5.8.0/en/main_classes/feature_extractor#transformers.SequenceFeatureExtractor)) -- The feature extractor that will be used by the pipeline to encode data for the model. This object inherits from [SequenceFeatureExtractor](/docs/transformers/v5.8.0/en/main_classes/feature_extractor#transformers.SequenceFeatureExtractor).
  * [](#transformers.Pipeline.image_processor) **image_processor** ([BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor)) -- The image processor that will be used by the pipeline to encode data for the model. This object inherits from [BaseImageProcessor](/docs/transformers/v5.8.0/en/main_classes/image_processor#transformers.BaseImageProcessor).
  * [](#transformers.Pipeline.processor) **processor** ([ProcessorMixin](/docs/transformers/v5.8.0/en/main_classes/processors#transformers.ProcessorMixin)) -- The processor that will be used by the pipeline to encode data for the model. This object inherits from [ProcessorMixin](/docs/transformers/v5.8.0/en/main_classes/processors#transformers.ProcessorMixin). Processor is a composite object that might contain `tokenizer`, `feature_extractor`, and `image_processor`.
  * [](#transformers.Pipeline.task) **task** (`str`, defaults to `""`) -- A task-identifier for the pipeline.
  * [](#transformers.Pipeline.num_workers) **num_workers** (`int`, _optional_ , defaults to 8) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the number of workers to be used.
  * [](#transformers.Pipeline.batch_size) **batch_size** (`int`, _optional_ , defaults to 1) -- When the pipeline will use _DataLoader_ (when passing a dataset, on GPU for a Pytorch model), the size of the batch to use, for inference this is not always beneficial, please read [Batching with pipelines](https://huggingface.co/transformers/main_classes/pipelines.html#pipeline-batching) .
  * [](#transformers.Pipeline.args_parser) **args_parser** ([ArgumentHandler](/docs/transformers/v5.8.0/en/internal/pipelines_utils#transformers.pipelines.ArgumentHandler), _optional_) -- Reference to the object in charge of parsing supplied pipeline parameters.
  * [](#transformers.Pipeline.device) **device** (`int`, _optional_ , defaults to -1) -- Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on the associated CUDA device id. You can pass native `torch.device` or a `str` too
  * [](#transformers.Pipeline.dtype) **dtype** (`str` or `torch.dtype`, _optional_) -- Sent directly as `model_kwargs` (just a simpler shortcut) to use the available precision for this model (`torch.float16`, `torch.bfloat16`, … or `"auto"`)
  * [](#transformers.Pipeline.binary_output) **binary_output** (`bool`, _optional_ , defaults to `False`) -- Flag indicating if the output the pipeline should happen in a serialized format (i.e., pickle) or as the raw output data e.g. text.

The Pipeline class is the class from which all pipelines inherit. Refer to this class for methods shared across different pipelines.

Base class implementing pipelined operations. Pipeline workflow is defined as a sequence of the following operations:

Input -> Tokenization -> Model Inference -> Post-Processing (task dependent) -> Output

Pipeline supports running on CPU or GPU through the device argument (see below).

Some pipeline, like for instance [FeatureExtractionPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.FeatureExtractionPipeline) (`'feature-extraction'`) output large tensor object as nested-lists. In order to avoid dumping such large structure as textual data we provide the `binary_output` constructor argument. If set to `True`, the output will be stored in the pickle format.

#### check_model_type

[](#transformers.Pipeline.check_model_type) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/base.py#L1081)

( supported_models: list[str] | dict )

Parameters

  * [](#transformers.Pipeline.check_model_type.supported_models) **supported_models** (`list[str]` or `dict`) -- The list of models supported by the pipeline, or a dictionary with model class values.

Check if the model class is in supported by the pipeline.

#### device_placement

[](#transformers.Pipeline.device_placement) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/base.py#L1017)

( )

Context Manager allowing tensor allocation on the user-specified device.

[](#transformers.Pipeline.device_placement.example)

Examples:

Copied


    # Explicitly ask for tensor allocation on CUDA device :0
    pipe = pipeline(..., device=0)
    with pipe.device_placement():
        # Every tensor allocation will be done on the request device
        output = pipe(...)

#### ensure_tensor_on_device

[](#transformers.Pipeline.ensure_tensor_on_device) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/base.py#L1049)

( **inputs ) → `dict[str, torch.Tensor]`

Parameters

  * [](#transformers.Pipeline.ensure_tensor_on_device.inputs) **inputs** (keyword arguments that should be `torch.Tensor`, the rest is ignored) -- The tensors to place on `self.device`.
  * [](#transformers.Pipeline.ensure_tensor_on_device.Recursive) **Recursive** on lists **only**. --

Returns

`dict[str, torch.Tensor]`

The same as `inputs` but on the proper device.

Ensure PyTorch tensors are on the specified device.

#### postprocess

[](#transformers.Pipeline.postprocess) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/base.py#L1148)

( model_outputs: ModelOutput **postprocess_parameters: dict )

Postprocess will receive the raw outputs of the `_forward` method, generally tensors, and reformat them into something more friendly. Generally it will output a list or a dict or results (containing just strings and numbers).

#### predict

[](#transformers.Pipeline.predict) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/base.py#L996)

( X )

Scikit / Keras interface to transformers’ pipelines. This method will forward to **call**().

#### preprocess

[](#transformers.Pipeline.preprocess) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/base.py#L1127)

( input_: Any **preprocess_parameters: dict )

Preprocess will take the `input_` of a specific pipeline and return a dictionary of everything necessary for `_forward` to run properly. It should contain at least one tensor, but might have arbitrary other items.

#### push_to_hub

[](#transformers.Pipeline.push_to_hub) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/utils/hub.py#L720)

( repo_id: str commit_message: str | None = None commit_description: str | None = None private: bool | None = None token: bool | str | None = None revision: str | None = None create_pr: bool = False max_shard_size: int | str | None = '50GB' tags: list[str] | None = None )

Parameters

  * [](#transformers.Pipeline.push_to_hub.repo_id) **repo_id** (`str`) -- The name of the repository you want to push your pipe to. It should contain your organization name when pushing to a given organization.
  * [](#transformers.Pipeline.push_to_hub.commit_message) **commit_message** (`str`, _optional_) -- Message to commit while pushing. Will default to `"Upload pipe"`.
  * [](#transformers.Pipeline.push_to_hub.commit_description) **commit_description** (`str`, _optional_) -- The description of the commit that will be created
  * [](#transformers.Pipeline.push_to_hub.private) **private** (`bool`, _optional_) -- Whether to make the repo private. If `None` (default), the repo will be public unless the organization's default is private. This value is ignored if the repo already exists.
  * [](#transformers.Pipeline.push_to_hub.token) **token** (`bool` or `str`, _optional_) -- The token to use as HTTP bearer authorization for remote files. If `True` (default), will use the token generated when running `hf auth login` (stored in `~/.huggingface`).
  * [](#transformers.Pipeline.push_to_hub.revision) **revision** (`str`, _optional_) -- Branch to push the uploaded files to.
  * [](#transformers.Pipeline.push_to_hub.create_pr) **create_pr** (`bool`, _optional_ , defaults to `False`) -- Whether or not to create a PR with the uploaded files or directly commit.
  * [](#transformers.Pipeline.push_to_hub.max_shard_size) **max_shard_size** (`int` or `str`, _optional_ , defaults to `"50GB"`) -- Only applicable for models. The maximum size for a checkpoint before being sharded. Checkpoints shard will then be each of size lower than this size. If expressed as a string, needs to be digits followed by a unit (like `"5MB"`).
  * [](#transformers.Pipeline.push_to_hub.tags) **tags** (`list[str]`, _optional_) -- List of tags to push on the Hub.

Upload the pipeline file to the 🤗 Model Hub.

[](#transformers.Pipeline.push_to_hub.example)

Examples:

Copied


    from transformers import pipeline

    pipe = pipeline("google-bert/bert-base-cased")

    # Push the pipe to your namespace with the name "my-finetuned-bert".
    pipe.push_to_hub("my-finetuned-bert")

    # Push the pipe to an organization with the name "my-finetuned-bert".
    pipe.push_to_hub("huggingface/my-finetuned-bert")

#### save_pretrained

[](#transformers.Pipeline.save_pretrained) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/base.py#L944)

( save_directory: str | os.PathLike **kwargs: Any )

Parameters

  * [](#transformers.Pipeline.save_pretrained.save_directory) **save_directory** (`str` or `os.PathLike`) -- A path to the directory where to saved. It will be created if it doesn't exist.
  * [](#transformers.Pipeline.save_pretrained.kwargs) **kwargs** (`dict[str, Any]`, _optional_) -- Additional key word arguments passed along to the [push_to_hub()](/docs/transformers/v5.8.0/en/main_classes/model#transformers.utils.PushToHubMixin.push_to_hub) method.

Save the pipeline’s model and tokenizer.

#### transform

[](#transformers.Pipeline.transform) [< source >](https://github.com/huggingface/transformers/blob/v5.8.0/src/transformers/pipelines/base.py#L990)

( X )

Scikit / Keras interface to transformers’ pipelines. This method will forward to **call**().

[ Update on GitHub](https://github.com/huggingface/transformers/blob/main/docs/source/en/main_classes/pipelines.md)

[←PEFT](/docs/transformers/main_classes/peft) [Processors→](/docs/transformers/main_classes/processors)

[Pipelines](#pipelines)[The pipeline abstraction](#transformers.pipeline)[Pipeline batching](#pipeline-batching)[Pipeline chunk batching](#pipeline-chunk-batching)[Pipeline FP16 inference](#pipeline-fp16-inference)[Pipeline custom code](#pipeline-custom-code)[Implementing a pipeline](#implementing-a-pipeline)[Audio](#audio)[AudioClassificationPipeline](#transformers.AudioClassificationPipeline)[AutomaticSpeechRecognitionPipeline](#transformers.AutomaticSpeechRecognitionPipeline)[TextToAudioPipeline](#transformers.TextToAudioPipeline)[ZeroShotAudioClassificationPipeline](#transformers.ZeroShotAudioClassificationPipeline)[Computer vision](#computer-vision)[DepthEstimationPipeline](#transformers.DepthEstimationPipeline)[ImageClassificationPipeline](#transformers.ImageClassificationPipeline)[ImageSegmentationPipeline](#transformers.ImageSegmentationPipeline)[KeypointMatchingPipeline](#transformers.KeypointMatchingPipeline)[ObjectDetectionPipeline](#transformers.ObjectDetectionPipeline)[VideoClassificationPipeline](#transformers.VideoClassificationPipeline)[ZeroShotImageClassificationPipeline](#transformers.ZeroShotImageClassificationPipeline)[ZeroShotObjectDetectionPipeline](#transformers.ZeroShotObjectDetectionPipeline)[Natural Language Processing](#natural-language-processing)[FillMaskPipeline](#transformers.FillMaskPipeline)[TableQuestionAnsweringPipeline](#transformers.TableQuestionAnsweringPipeline)[TextClassificationPipeline](#transformers.TextClassificationPipeline)[TextGenerationPipeline](#transformers.TextGenerationPipeline)[TokenClassificationPipeline](#transformers.TokenClassificationPipeline)[ZeroShotClassificationPipeline](#transformers.ZeroShotClassificationPipeline)[Multimodal](#multimodal)[DocumentQuestionAnsweringPipeline](#transformers.DocumentQuestionAnsweringPipeline)[FeatureExtractionPipeline](#transformers.FeatureExtractionPipeline)[ImageFeatureExtractionPipeline](#transformers.ImageFeatureExtractionPipeline)[ImageTextToTextPipeline](#transformers.ImageTextToTextPipeline)[AnyToAnyPipeline](#transformers.AnyToAnyPipeline)[MaskGenerationPipeline](#transformers.MaskGenerationPipeline)[Parent class: Pipeline](#transformers.Pipeline)
