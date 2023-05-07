Created: 2023-04-04 11:59
#quicknote

Use gradient accumulation to train models with large batch sizes in order to work around hardware limitations when GPU memory is a concern.

Gradient accumulation is a way to virtually increase the batch size during training, which is very useful when the available GPU memory is insufficient to accommodate the desired batch size. In gradient accumulation, gradients are computed for smaller batches and accumulated (usually summed or averaged) over multiple iterations instead of updating the model weights after every batch. Once the accumulated gradients reach the target “virtual” batch size, the model weights are updated with the accumulated gradients.

## Resources
1. [Lightning](https://lightning.ai/pages/blog/gradient-accumulation/)
2. [Hugging Face](https://huggingface.co/docs/accelerate/usage_guides/gradient_accumulation#:~:text=Gradient%20accumulation%20is%20a%20technique,of%20batches%20have%20been%20performed.)
#### Tags
#training 