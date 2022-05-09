# LDA
Created: 2022-05-03 09:59
#note
 
 LDA is a Bayesian version of [[PLSA]].
Latent Dirichlet Allocation works as follow:
1. Specify the number of topics;
2. Each word is randomly assigned to one of the topics (technically the distribution is a Dirichlet one, i.e. the numbers of assigned across the topics add up to 1);
3. Topic assignments for each word are updated in an iterative fashion by updating the prevalence of the word across the topics, as well as the prevalence of the topics in the document. TF-IDF is used in this stage.
4. Stop when iterations begin to have little impact on the probabilities assigned to each word.


## References
1. [TowardsDataScience](https://towardsdatascience.com/latent-dirichlet-allocation-lda-9d1cd064ffa2)
2. [Theory+Tutorial](https://cbail.github.io/SICSS_Topic_Modeling.html)

## Code
1. 

#### Tags
#topic_modeling 