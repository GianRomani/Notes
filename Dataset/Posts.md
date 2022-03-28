# Posts
Created: 2022-03-23 16:00

Stats:
- 1000 characters;
- 5-8 sentences;
-  100-150 characters for sentence (10 words more or less);
-  80 unique words;
-  few tags (0-2 max), some tags are used very often (100-150 times), others not;
-  few likes, 1-2, per post
-  Verbs and adjectives are not really relevant for clusters, nouns are

Fields ( #yes #no #idk if they are going to be considered as features ) [[Doubts]]:
- id;
- userId;
- userName #no
- documentType, contains just "experience" #no;
- title #yes;
- description #yes;
- locations #no but in future #yes;
- feature, mostly empty #no;
- duration, in seconds? There are a lot of zeros #yes; #doubts
- imageId, #no but in future #yes;
- previewId, a lot of null #no;
- distance, mostly zero #no;
- datePublishing, #yes;
- widgets, #no but I have to look at it deeply;
- counterUseful, #yes;
- tags, #no but in future #yes;
- numberOfPositions, how many places were seen during experience? #idk;  #doubts
- creationDate, difference with datePublishing? #doubts
- videoId, #no but in future #yes;
- version, what is this? #no; #doubts
- categories, #yes;
- media, #no but in future #yes;
- shareType, it contains "shared" or nan #no;
- status, it contains "Published" or nan #no;
- lastUpdate, #id;
- versionHistory, "draft", "published", "approving" #idk;
- viewCounter, #yes;
- device, #no ;

## References
1. 


#### Tags
#posts