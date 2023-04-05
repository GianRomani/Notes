Created: 2023-04-04 11:48
#quicknote

Quantization is a technique to reduce the computational and memory costs of running inference by representing the weights and activations with low-precision data types like 8-bit integer (`int8`) instead of the usual 32-bit floating point (`float32`).

Reducing the number of bits means the resulting model requires less memory storage, consumes less energy (in theory), and operations like matrix multiplication can be performed much faster with integer arithmetic. It also allows to run models on embedded devices, which sometimes only support integer data types.

The most common lower precision data types are:

-   `float16`, accumulation data type `float16`
-   `bfloat16`, accumulation data type `float32`
-   `int16`, accumulation data type `int32`
-   `int8`, accumulation data type `int32`

The accumulation data type specifies the type of the result of accumulating (adding, multiplying, etc) values of the data type in question.

Performing quantization to go from `float32` to `int8` is more tricky. Only 256 values can be represented in `int8`, while `float32` can represent a very wide range of values. The idea is to find the best way to project our range `[a, b]` of `float32` values to the `int8` space.
A common quantization scheme is called *affine quantization scheme* and works in the following way:
$x = S* (x_q - Z)$, where $x_q$ is the quantized `int8` value associated to x, S and Z are the quantization parameters (S is the scale, a positive `float32`, and Z is the zero-point, the `int8` value that corresponds to the value 0 in the `float32` realm).
So the quantized value for $x_q$ in `[a,b]` is computed as follows: $x_q=round(x/S + Z)$.  `float32` values outside of the `[a, b]` range are clipped to the closest representable value.

## Resources
1. [Hugging Face](https://huggingface.co/docs/optimum/concept_guides/quantization)

#### Tags
#training #huggingface #transformers