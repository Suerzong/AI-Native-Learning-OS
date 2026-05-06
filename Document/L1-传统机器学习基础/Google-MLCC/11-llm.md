#  Introduction to Large Language Models
  * This module explores language models, which estimate the probability of a token or sequence of tokens occurring within a longer sequence, enabling tasks like text generation, translation, and summarization.

  * Language models utilize context, the surrounding information of a target token, to enhance prediction accuracy, with recurrent neural networks offering more context than traditional N-grams.

  * N-grams are ordered sequences of words used to build language models, with longer N-grams providing more context but potentially encountering sparsity issues.

  * Tokens, the atomic units of language modeling, represent words, subwords, or characters and are crucial for understanding and processing language.

  * While recurrent neural networks improve context understanding compared to N-grams, they have limitations, paving the way for the emergence of large language models that evaluate the whole context simultaneously.

## What is a language model?

A [**language model**](</machine-learning/glossary#language-model>) estimates the probability of a [**token**](</machine-learning/glossary#token>) or sequence of tokens occurring within a longer sequence of tokens. A token could be a word, a subword (a subset of a word), or even a single character.

####  Click the icon to learn more about tokens.

Most modern language models tokenize by subwords, that is, by chunks of text containing semantic meaning. The chunks could vary in length from single characters like punctuation or the possessive _s_ to whole words. Prefixes and suffixes might be represented as separate subwords. For example, the word _unwatched_ might be represented by the following three subwords:

  * un (the prefix)
  * watch (the root)
  * ed (the suffix)

The word _cats_ might be represented by the following two subwords:

  * cat (the root)
  * s (the suffix)

A more complex word like "antidisestablishmentarianism" might be represented as six subwords:

  * anti
  * dis
  * establish
  * ment
  * arian
  * ism

Tokenization is language specific, so the number of characters per token differs across languages. For English, one token corresponds to ~4 characters or about 3/4 of a word, so 400 tokens ~= 300 English words.

Tokens are the atomic unit or smallest unit of language modeling.

Tokens are now also being successfully applied to [ computer vision](<https://ai.googleblog.com/2023/03/scaling-vision-transformers-to-22.html>) and [ audio generation](<https://ai.googleblog.com/2022/10/audiolm-language-modeling-approach-to.html>).

Consider the following sentence and the token(s) that might complete it:

    When I hear rain on my roof, I _______ in my kitchen.

A language model determines the probabilities of different tokens or sequences of tokens to complete that blank. For example, the following probability table identifies some possible tokens and their probabilities:

Probability | Token(s)
---|---
9.4% | cook soup
5.2% | warm up a kettle
3.6% | cower
2.5% | nap
2.2% | relax

In some situations, the sequence of tokens could be an entire sentence, paragraph, or even an entire essay.

An application can use the probability table to make predictions. The prediction might be the highest probability (for example, "cook soup") or a random selection from tokens having a probability greater than a certain threshold.

Estimating the probability of what fills in the blank in a text sequence can be extended to more complex tasks, including:

  * Generating text.
  * Translating text from one language to another.
  * Summarizing documents.

By modeling the statistical patterns of tokens, modern language models develop extremely powerful internal representations of language and can generate plausible language.

### N-gram language models

[**N-grams**](</machine-learning/glossary#n-gram>) are ordered sequences of words used to build language models, where N is the number of words in the sequence. For example, when N is 2, the N-gram is called a **2-gram** (or a [**bigram**](</machine-learning/glossary#bigram>)); when N is 5, the N-gram is called a 5-gram. Given the following phrase in a training document:

    you are very nice

The resulting 2-grams are as follows:

  * you are
  * are very
  * very nice

When N is 3, the N-gram is called a **3-gram** (or a [**trigram**](</machine-learning/glossary#trigram>)). Given that same phrase, the resulting 3-grams are:

  * you are very
  * are very nice

Given two words as input, a language model based on 3-grams can predict the likelihood of the third word. For example, given the following two words:

    orange is

A language model examines all the different 3-grams derived from its training corpus that start with `orange is` to determine the most likely third word. Hundreds of 3-grams could start with the two words `orange is`, but you can focus solely on the following two possibilities:

    orange is ripe
    orange is cheerful

The first possibility (`orange is ripe`) is about orange the fruit, while the second possibility (`orange is cheerful`) is about the color orange.

## Context

Humans can retain relatively long contexts. While watching Act 3 of a play, you retain knowledge of characters introduced in Act 1. Similarly, the punchline of a long joke makes you laugh because you can remember the context from the joke's setup.

In language models, **context** is helpful information before or after the target token. Context can help a language model determine whether "orange" refers to a citrus fruit or a color.

Context can help a language model make better predictions, but does a 3-gram provide sufficient context? Unfortunately, the only context a 3-gram provides is the first two words. For example, the two words `orange is` doesn't provide enough context for the language model to predict the third word. Due to lack of context, language models based on 3-grams make a lot of mistakes.

Longer N-grams would certainly provide more context than shorter N-grams. However, as N grows, the relative occurrence of each instance decreases. When N becomes very large, the language model typically has only a single instance of each occurrence of N tokens, which isn't very helpful in predicting the target token.

### Recurrent neural networks

[**Recurrent neural networks**](</machine-learning/glossary#recurrent-neural-network>) provide more context than N-grams. A recurrent neural network is a type of [**neural network**](</machine-learning/glossary#neural-network>) that trains on a sequence of tokens. For example, a recurrent neural network can _gradually_ learn (and learn to ignore) selected context from each word in a sentence, kind of like you would when listening to someone speak. A large recurrent neural network can gain context from a passage of several sentences.

Although recurrent neural networks learn more context than N-grams, the amount of useful context recurrent neural networks can intuit is still relatively limited. Recurrent neural networks evaluate information "token by token." In contrast, large language models—the topic of the next section—can evaluate the whole context at once.

Note that training recurrent neural networks for long contexts is constrained by the [**vanishing gradient problem**](</machine-learning/glossary#vanishing-gradient-problem>).

## Exercise: Check your understanding

Which language model makes better predictions for English text?

  * A language model based on 6-grams
  * A language model based on 5-grams

The answer depends on the size and diversity of the training set.

If the training set spans millions of diverse documents, then the model based on 6-grams will probably outperform the model based on 5-grams.

The language model based on 6-grams.

This language model has more context, but unless this model has trained on a lot of documents, most of the 6-grams will be rare.

The language model based on 5-grams.

This language model has less context, so it is unlikely to outperform the language model based on 6-grams.

[Help Center](<https://support.google.com/machinelearningeducation>)

[ Previous arrow_back  Test your knowledge (10 min)  ](</machine-learning/crash-course/embeddings/test-your-knowledge>)

[ Next What's a Large Language Model? (15 min)  arrow_forward  ](</machine-learning/crash-course/llm/transformers>)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](<https://creativecommons.org/licenses/by/4.0/>), and code samples are licensed under the [Apache 2.0 License](<https://www.apache.org/licenses/LICENSE-2.0>). For details, see the [Google Developers Site Policies](<https://developers.google.com/site-policies>). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-09 UTC.
