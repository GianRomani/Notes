# Cold-start
Created: 2022-03-23 11:55

This problem occurs when it is impossible to make valid recommendations due to an initial lack of ratings.
Types:
- #new_community -> not enough data (for example in a new RS system) -> it occurs in [[Collaborative filtering]] systems -> encourage users to make ratings
- #new_item -> new items don't have ratings so they are not recommended 
- #new_user -> new user have not rated anything yet so we can recommend items to them -> can not use [[Collaborative filtering]] again

Possible solutions:
- get additional information from new users;
- use #hybrid_filtering  approaches
## References
1. 


#### Tags
#cold_start