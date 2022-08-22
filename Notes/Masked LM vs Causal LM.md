# Masked LM vs Causal LM
Created: 2022-08-21 11:24
#note

**MLM loss is preferred when the goal is to learn a good representation of the input document**, whereas, **CLM is mostly preferred when we wish to learn a system that generates fluent text**. Also, intuitively this makes sense, because while learning good input representation for every word you would want to know the words that occur to it’s both left and right, whereas, when you want to learn a system that generates text, you can only see what all you have generated till now_(it’s just like how humans write as well)_. So, making a system that could peek to the other side as well while generating text can introduce bias limiting the creative ability of the model.

## References
1. [Towards Data Science](https://towardsdatascience.com/understanding-masked-language-models-mlm-and-causal-language-models-clm-in-nlp-194c15f56a5#:~:text=MLM%20loss%20is%20preferred%20when,system%20that%20generates%20fluent%20text.)

#### Tags
#transformer 