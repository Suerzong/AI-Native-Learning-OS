[ Hugging Face](/)

Transformers 文档

聊天模板

# Transformers

聊天模板

[聊天基础](./conversations)指南介绍了如何存储聊天历史记录以及使用 [TextGenerationPipeline](/docs/transformers/v5.8.0/en/main_classes/pipelines#transformers.TextGenerationPipeline) 从聊天模型生成文本。

本指南面向更高级的用户，涵盖底层类和方法，以及理解与模型聊天时实际发生情况的关键概念。

理解聊天模型的关键洞察是：所有因果语言模型（causal LM），无论是否经过聊天训练，都是继续一个词元序列。当因果语言模型被训练时，训练通常从在大量文本语料库上进行"预训练"开始，这创建了一个"基础"模型。这些基础模型随后通常被"微调"用于聊天，这意味着在格式化为消息序列的数据上训练它们。聊天仍然只是一个词元序列！你传递给聊天模型的 `role` 和 `content` 字典列表被转换为词元序列，通常带有控制词元如 `<|user|>` 或 `<|assistant|>` 或 `<|end_of_message|>`，使模型能够看到聊天结构。有许多可能的聊天格式，不同的模型可能使用不同的格式或控制词元，即使它们是从同一个基础模型微调而来！

不过不要惊慌——你不需要记住每种可能的聊天格式来使用聊天模型。聊天模型附带**聊天模板**，指示它们期望的聊天格式。你可以使用 `apply_chat_template` 方法访问这些模板。让我们看两个例子。这两个模型都是从同一个 `Mistral-7B` 基础模型微调而来：

    from transformers import AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")
    chat = [
      {"role": "user", "content": "Hello, how are you?"},
      {"role": "assistant", "content": "I'm doing great. How can I help you today?"},
      {"role": "user", "content": "I'd like to show off how chat templating works!"},
    ]

    tokenizer.apply_chat_template(chat, tokenize=False)

    '<s>[INST] Hello, how are you? [/INST]I\'m doing great. How can I help you today?</s> [INST] I\'d like to show off how chat templating works! [/INST]'

Mistral-7B-Instruct 使用 `[INST]` 和 `[/INST]` 词元来指示用户消息的开始和结束，而 Zephyr-7B 使用 `<|user|>` 和 `<|assistant|>` 词元来指示说话者角色。这就是聊天模板很重要的原因——使用错误的控制词元，这些模型的性能会大幅下降。

## [](#using-applychattemplate) 使用 apply_chat_template

`apply_chat_template` 的输入应该结构化为包含 `role` 和 `content` 键的字典列表。`role` 键指定说话者，`content` 键包含消息。常见的角色有：

  * `user` 表示来自用户的消息
  * `assistant` 表示来自模型的消息
  * `system` 表示关于模型应如何行为的指令（通常放在聊天的开头）

`apply_chat_template` 接受此列表并返回格式化的序列。如果你想对序列进行分词，设置 `tokenize=True`。

    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained("HuggingFaceH4/zephyr-7b-beta")
    model = AutoModelForCausalLM.from_pretrained("HuggingFaceH4/zephyr-7b-beta", device_map="auto", dtype=torch.bfloat16)

    messages = [
        {"role": "system", "content": "You are a friendly chatbot who always responds in the style of a pirate",},
        {"role": "user", "content": "How many helicopters can a human eat in one sitting?"},
     ]
    tokenized_chat = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")
    print(tokenizer.decode(tokenized_chat[0]))

    '<|system|>\nYou are a friendly chatbot who always responds in the style of a pirate</s>\n<|user|>\nHow many helicopters can a human eat in one sitting?</s>\n<|assistant|>\n'

将分词后的聊天传递给 [generate()](/docs/transformers/v5.8.0/en/main_classes/text_generation#transformers.GenerationMixin.generate) 以生成响应。

    outputs = model.generate(tokenized_chat, max_new_tokens=128)
    print(tokenizer.decode(outputs[0]))

> 一些分词器会添加特殊的 `<bos>` 和 `<eos>` 词元。聊天模板应该已经包含所有必要的特殊词元，添加额外的特殊词元通常是不正确或重复的，会损害模型性能。当你使用 `apply_chat_template(tokenize=False)` 格式化文本时，如果你稍后要分词，请确保设置 `add_special_tokens=False` 以避免重复这些词元。如果你使用 `apply_chat_template(tokenize=True)`，这通常不是问题，这意味着它通常是更安全的选项！

### [](#addgenerationprompt) add_generation_prompt

你可能注意到了上面示例中的 [add_generation_prompt](https://huggingface.co/docs/transformers/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.apply_chat_template.add_generation_prompt) 参数。此参数在聊天末尾添加指示 `assistant` 响应开始的词元。记住：在所有聊天抽象之下，聊天模型仍然只是继续词元序列的语言模型！如果你包含告诉它现在处于 `assistant` 响应的词元，它将正确地编写响应，但如果你不包含这些词元，模型可能会困惑并做一些奇怪的事情，比如**继续**用户的消息而不是回复它！

当 `add_generation_prompt=True` 时，会在末尾添加 `<|im_start|>assistant` 以指示 `assistant` 消息的开始。这让模型知道接下来是 `assistant` 响应。

并非所有模型都需要生成提示，一些模型（如 [Llama](./model_doc/llama)）在 `assistant` 响应之前没有任何特殊词元。在这些情况下，[add_generation_prompt](https://huggingface.co/docs/transformers/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.apply_chat_template.add_generation_prompt) 没有效果。

### [](#continuefinalmessage) continue_final_message

[continue_final_message](https://huggingface.co/docs/transformers/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.apply_chat_template.continue_final_message) 参数控制是否应该继续聊天中的最后一条消息，而不是开始一条新消息。它移除序列结束词元，使模型从最后一条消息继续生成。

这对于"预填充"模型响应非常有用。在下面的示例中，模型生成继续 JSON 字符串的文本，而不是开始新消息。当你知道如何开始其回复时，这对于提高指令遵循的准确性非常有用。

    chat = [
        {"role": "user", "content": "Can you format the answer in JSON?"},
        {"role": "assistant", "content": '{"name": "'},
    ]

    formatted_chat = tokenizer.apply_chat_template(chat, tokenize=True, return_dict=True, continue_final_message=True)
    model.generate(**formatted_chat)

> 你不应该同时使用 [add_generation_prompt](https://huggingface.co/docs/transformers/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.apply_chat_template.add_generation_prompt) 和 [continue_final_message](https://huggingface.co/docs/transformers/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.apply_chat_template.continue_final_message)。前者添加开始新消息的词元，而后者移除序列结束词元。同时使用它们会返回错误。

## [](#model-training) 模型训练

使用聊天模板训练模型是确保模板与模型训练的词元匹配的好方法。将聊天模板应用为你数据集的预处理步骤。设置 `add_generation_prompt=False`，因为在训练期间提示 assistant 响应的额外词元没有帮助。

    from transformers import AutoTokenizer
    from datasets import Dataset

    tokenizer = AutoTokenizer.from_pretrained("HuggingFaceH4/zephyr-7b-beta")

    chat1 = [
        {"role": "user", "content": "Which is bigger, the moon or the sun?"},
        {"role": "assistant", "content": "The sun."}
    ]
    chat2 = [
        {"role": "user", "content": "Which is bigger, a virus or a bacterium?"},
        {"role": "assistant", "content": "A bacterium."}
    ]

    dataset = Dataset.from_dict({"chat": [chat1, chat2]})
    dataset = dataset.map(lambda x: {"formatted_chat": tokenizer.apply_chat_template(x["chat"], tokenize=False, add_generation_prompt=False)})
    print(dataset['formatted_chat'][0])

    '<|user|>\nWhich is bigger, the moon or the sun?</s>\n<|assistant|>\nThe sun.</s>'

在此步骤之后，你可以继续使用 `formatted_chat` 列遵循因果语言模型的[训练手册](./tasks/language_modeling)。

[ 在 GitHub 上更新](https://github.com/huggingface/transformers/blob/main/docs/source/en/chat_templating.md)

[←聊天基础](/docs/transformers/conversations) [聊天消息模式→](/docs/transformers/chat_content_patterns)

[聊天模板](#chat-templates)[使用 apply_chat_template](#using-applychattemplate)[add_generation_prompt](#addgenerationprompt)[continue_final_message](#continuefinalmessage)[模型训练](#model-training)
