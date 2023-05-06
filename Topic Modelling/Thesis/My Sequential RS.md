# My Sequential RS

^781da5

Created: 2022-06-23 09:24
#note

**Goal**: provide recommendations based on both short-term and long-term preferences -> use two different models or just one?

[[BERT4Rec]] is really good for short-term recommendations.
[[NxtPost - User to Post Recommendations in Facebook Groups]] is able to consider both aspects in its recommendations.

I could leverage Topic modeling models to cluster documents, images and users(?) -> from this I could get long-term preferences.

If I have two models for short and long term preferences, I need to find a way to mix the recommendations.

Another cool feature could consist in a model that can suggest the image to show in the recommendations -> I need embeddings of images and texts in the same space -> look into image clustering.

To model long-term preferences, I could learn embeddings for users (similarly to [ig2Vec](https://ai.facebook.com/blog/powered-by-ai-instagrams-explore-recommender-system/?utm_source=datarootlabs&utm_medium=blog)) -> use userIDs of the users with whom I interacted or postsIDs. In this way is easy to retrieve similar users (just define distance metric and use [[kNN]]).

Another aspect to consider is the presence of side information like popularity or recency of posts, time, location or device of a user etc.

Possible flow:
1. compute users embeddings -> long-term preferences; ^1
2. get list of recommendations based on users embeddings; ^2
3. modify the list using a sequential recommender; ^3
4. periodically update users embeddings using new interactions ^4

About [[#^1]], we initially have the users divided in 80 categories, each with an initial list of recommendations. Once users embeddings are updated I could get the lists by mapping users and documents in the same space -> then use kNN. 

For [[#^3]] I could use two approaches:
- compute item to be recommended using just actual session and then merge with pre-computed list;
- consider both long-term and session-based preferences to suggest new items.

For [[#^4]] consider interactions to update users embeddings.

To recap, I need to decide:
- how to get and update users embeddings;
- whether sequential recommender consider both long-term preferences or just the actual session;
- learn users embeddings and posts embeddings jointly or separately, i.e. learn items embeddings and then use them to compute users embeddings?
- how to consider side information in recommendations;
- how to introduce and work with multi-modality -> images are consider in the computation of the recommendations or used later, just to decide which one to show?

For our problem we should keep in mind (apart from similarity between users and items consumed):
- recency of the post;
- popularity of the post;
- period of the year

## Images
The choice of the image in the thumbnail is really important to get users to click on an item. We could change the image depending on:
- the section in which the item is showed;
- user's long-term preferences;
- user's latest interactions

Some insights [here](https://becominghuman.ai/how-netflix-uses-ai-and-machine-learning-a087614630fe)

## Idea n°1
**Long-term preference** -> user embeddings obtained from postIDs they interacted with or userIDs of the users who posted the posts they interacted with. Then get a starting list of recommendations in one of the following ways:
- clustering of users gives us the recommendation list;
- recommendation list composed by posts of the users I interacted with

**Short-term preferences** -> use models like BERT4Rec to modify the list obtained above. 

Periodically update the starting list of recommendations.

For each recommendation use clustering methods to get best image to show.

## Idea n°2
Learning separately user and item embeddings could be useful for the development of multiple models with different goals and for scalability issues.
A model based on a decoupled learning of the embeddings can work in the following way:
- Firstly compute embeddings for items.
- Use them to get user embeddings;
- Use those embeddings + contextual info to generate a session-level user embedding before any interaction -> use (approximate) nearest-neighbour search to get recommendations, i.e. do not predict the individual tracks inside the session, but encode the session and use encoding to retrieve list.

Using this approach I can have a general list of recommendations + a session-based short list (I can have different lists for different times of the day, days of the week line in [[CoSeRNN]]) and then I could use another sequential recommender for long sessions (maybe using models like [[BERT4Rec]]).

Having the embeddings pre-computed can also help us with other features -> explaining recommendations, choice of the images to show etc. For example, we could map both images and documents to the same embeddings space, in this way, once we have the session embedding, we can show in the thumbnail the most suitable image -> check [[Concept]] and see if there are other approaches that leverage for example [[CLIP - Contrastive Language-Image Pre-Training]].

## References
1. 

## Code
1. 

#### Tags