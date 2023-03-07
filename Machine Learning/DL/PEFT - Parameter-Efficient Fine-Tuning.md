Created: 2023-03-07 17:48
#note

[[Large Language Models (LLMs)]] based on the [[Transformer]] architecture are considered SOTA in several NLP (and not only) tasks. A typical way to use such models is to fine-tune large-scale pretrained generic models to downstream tasks. Fine-tuning could lead to huge performance improvements.

However, these models are really big, so fine-tuning and storing them on regular hardware can be a problem.

PEFT approaches could solve these problems by fine-tuning just a small amount of extra model parameters while keeping intact most of the parameters of the pretrained models.
This helps with the computational and storage costs, and also it can avoid the issue of [catastrophic forgetting](https://arxiv.org/abs/1312.6211), where a pretrained model, once trained on a second task, "forgets" how to perform the first task.

PEFT techniques have also shown better results in low-data regimes and in out-of-scenarios contexts.

The small trained weights from PEFT approaches are added on top of the pretrained LLM. So the same LLM can be used for multiple tasks by adding small weights without having to replace the entire model. This also means that users get just tiny checkpoints after a PEFT (compared to large checkpoints of full fine-tuning, e.g. few MBs vs tens of GBs).


## References
1. [HF blog](https://huggingface.co/blog/peft)
2. [Few-shot PEFT vs In-Context Learning](https://arxiv.org/pdf/2205.05638.pdf)

## Code
1. [HF GitHub](https://github.com/huggingface/peft)
2. [Use cases](https://github.com/huggingface/peft#use-cases)