Created: 2022-03-23 11:55
#note

This problem occurs when it is impossible to make valid recommendations due to an initial lack of ratings.

Types:
- new community -> not enough data (for example in a new RS system) -> it occurs in [[Collaborative filtering]] systems -> encourage users to make ratings
- new item -> new items don't have ratings, so they are not recommended 
- new user -> new user have not rated anything yet, so we can recommend items to them -> can not use [[Collaborative filtering]] again

Possible solutions:
- get additional information from new users;
- use cookies;
- geo-ip;
- recommend top-sellers or promotions;
- interview the user;
- use #hybrid_filtering  approaches;
- use [[Content-based filtering]] in case of new items;
- map attributes to latent features (in case of new items);
- random exploration


## References
1. 

#### Tags
#cold_start