Created: 2022-12-02 17:08
#note

It is the method used to updates the parameters after a forward pass (so it is used during the backward pass).

The key element used in back propagation is the chain rule of differentiation. It states that: if $y=f(u)$ and $u=g(x)$ (i.e. $y=f(g(x))$), then the derivative of y with respect to x is $\frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx}$.


## References
1. [GitHub](https://github.com/rentruewang/learning-machine/blob/main/book/basics/gradients/back-prop.ipynb)
2. [Towards Data Science](https://towardsdatascience.com/how-does-back-propagation-work-in-neural-networks-with-worked-example-bc59dfb97f48)
3. [3Blue1Brown](https://www.youtube.com/watch?v=Ilg3gGewQ5U&feature=emb_imp_woyt&ab_channel=3Blue1Brown)
