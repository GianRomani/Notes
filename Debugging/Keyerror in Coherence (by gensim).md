# Keyerror in Coherence (by gensim)
Created: 2022-09-08 11:41
#note

It is caused by the fact that the topics contain words that are not in the dictionary.

It was fixed in the latest versions of gensim, so just update the version (>4.1.0).

## References
1. [GitHub issue](https://github.com/RaRe-Technologies/gensim/pull/2830)

## Code
1. 

#### Tags
#bug