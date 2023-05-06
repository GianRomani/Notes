Created: 2023-03-06 10:30
#quicknote

**Entropy** is the number of bits required to transmit a randomly selected event from a probability distribution. A skewed distribution has a low entropy, whereas a distribution where events have equal probability has a larger entropy.

A skewed probability distribution has less “surprise” and in turn a low entropy because likely events dominate. Balanced distribution are more surprising and turn have higher entropy because events are equally likely.

-   **Skewed Probability Distribution** (_unsurprising_): Low entropy.
-   **Balanced Probability Distribution** (_surprising_): High entropy.

Entropy $H(x)$ can eb calculated for a random variable with a set of $x$ in $X$ discrete states and their probability $P(x)$ as follows: $H(x)=-\sum_{x \in X} P(x)\log(P(x))$ 

#### Tags
#measures #ml