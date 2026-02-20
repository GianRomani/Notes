[[Large Language Models (LLMs)]] are not easy to fine-tune, but some methods (line [[LoRA - Low-Rank Adaptation of LLMs]]) can help. Let's see some numbers about costs and hours needed to fine-tune such models.

## How many hours?
- Alpaca-7B (Llama + LoRA): 3 epochs, 40-52k instructions ([Stanford Alpaca](https://huggingface.co/datasets/tatsu-lab/alpaca)), quantization-> ==1 hour== with A100 on Colab, ([cabrita](https://github.com/22-hours/cabrita)), ==1 hour== with 3090 ([camoscio](https://github.com/teelinsan/camoscio)) 
- FlanT5-xxl (11B) sharded with LoRA: g5.2xlarge AWS EC2 Instance, including 1 NVIDIA A10G (18GB) for ==10 hours== (13$), 5 epochs, quantization -> dataset: samsum (summarization task) ~15k samples ([hugging face](https://www.philschmid.de/fine-tune-flan-t5-peft))
- Alpaca-13B can be barely trained on a 4090 ([thread](https://github.com/tloen/alpaca-lora/issues/28)), in ==10 hours== for three epochs
- [Tried to run fine-tuning 33B Alpaca LoRA with A6000. It uses 48.4GB out of 49 and says that 1 epoch will take about 12 hours. Maybe do it later.](https://github.com/tloen/alpaca-lora/issues/28)
- on Discord someone is claiming that he trained 30B Alpaca on 4090 in ==40 hours==.


---
## Considerations

Alpaca (Llama + LoRA) 30B can be trained on a 80GBs A100 ([here](https://github.com/PhoebusSi/Alpaca-CoT)).
LLaMA-13B outperforms GPT-3(175B) and LLaMA-65B is competitive to PaLM-540M ([paper](https://arxiv.org/pdf/2302.13971v1.pdf)) -> sometimes smaller model trained on more or better data are better than bigger models.

From [Llama model paper](https://arxiv.org/pdf/2302.13971v1.pdf): When training a 65B-parameter model, our code processes around 380 tokens/sec/GPU on 2048 A100 GPU with 80GB of RAM. This means that training over our dataset containing 1.4T tokens takes approximately ==21 days==.


BLOOM (176B) is really expensive to fine-tune ([see here](https://huggingface.co/bigscience/bloom/discussions/46)).
BLOOM (560m) can be trained on 130k dataset (squad v2) with a V100 on VertxAI ([more info](https://huggingface.co/jasoneden/bloom560m-squad-helloworld) and [here](https://huggingface.co/bigscience/bloom/discussions/46)).

To run BLOOM (176B) we need ~180GB GPU ([here](https://huggingface.co/bigscience/bloom/discussions/46)).

I have not found a lot of attempt to use LoRA on BLOOM, [this](https://github.com/linhduongtuan/BLOOM-LORA) is the only one -> they fine-tuned it on Stanford Alpaca dataset.