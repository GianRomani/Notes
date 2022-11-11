A [string](https://www.techinterviewhandbook.org/algorithms/string/) is a sequence of characters.

**Time complexity (operations on single string)**
|Operation|Big-O|
|----|----|
|Access|O(1)|
|Search|O(n)|
|Insert|O(n)|
|Remove|O(n)|

**Time complexity (operations on 2 strings)**
|Operation|Big-O|Note|
|---|---|---|
|Find substring|O(nm)|This is the most naive case. There are more efficient algorithms for string searching such as the KMP algorithm|
|Concatenating strings|O(n+m)||
|Slice|O(m)||
|Split (by token)|O(n+m)||
|Strip (remove leading and trailing whitespaces)|O(n)||

**Things to ask about during the interview**
Ask about input character set and cases sensitivity.

**Corner cases:**
- empty string;
- string with 1 or 2 characters;
- string with repeated characters;
- strings with only distinct characters

## Data structures

### Trie
See [here](https://en.wikipedia.org/wiki/Trie). It is also called prefix tree or digital tree. It is a type of k-ary search tree, a tree data structure used for locating specific keys from within a set. These keys are most often strings, with links between nodes defined not by the entire key, but by individual characters. In order to access a key (to recover its value, change it, or remove it), the trie is traversed depth-first, following the links between nodes, which represent each character in the key.

### Suffix tree
It is a compressed [[#Trie]] containing all the suffixes of the given text as their keys and positions in the text as their values. Suffix trees allow particularly fast implementations of many important string operations.

## Common string algorithms
- [Rabin-Karp](https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm)
- [KMP](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm)

## Techniques

### Counting characters
To count the frequency of characters in a string, use hash table/map (or use built-in classes like Counter in Python). Note that, by using a counter, the space complexity is O(1).

### String of unique characters
A neat trick to count the characters in a string of unique characters is to use a 26-bit bit mask to indicate which lower case Latin characters are inside the string.

```python
mask = 0
for c in word:  
	mask |= (1 << (ord(c) - ord('a')))
```

To determine if two strings have common characters, perform `&` on the two bit masks. If the result is non-zero, i.e. `mask_a & mask_b > 0`, then the two strings have common characters.

### Anagram
An anagram is word switch or word play. It is the result of rearranging the letters of a word or phrase to produce a new word or phrase, while using all the original letters only once. In interviews, usually we are only bothered with words without spaces in them.

To determine if two strings are anagrams, there are a few approaches:

-   Sorting both strings should produce the same resulting string. This takes O(nlog(n)) time and O(log(n)) space.
-   If we map each character to a prime number and we multiply each mapped number together, anagrams should have the same multiple (prime factor decomposition). This takes O(n) time and O(1) space. Examples: [Group Anagram](https://leetcode.com/problems/group-anagrams/)
-   Frequency counting of characters will help to determine if two strings are anagrams. This also takes O(n) time and O(1) space.

### Palindrome
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward, such as `madam` or `racecar`.

Here are ways to determine if a string is a palindrome:

-   Reverse the string and it should be equal to itself.
-   Have two pointers at the start and end of the string. Move the pointers inward till they meet. At every point in time, the characters at both pointers should match.

The order of characters within the string matters, so hash tables are usually not helpful.

When a question is about counting the number of palindromes, a common trick is to have two pointers that move outward, away from the middle. Note that palindromes can be even or odd length. For each middle pivot position, you need to check it twice - once that includes the character and once without the character. This technique is used in [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/).

-   For substrings, you can terminate early once there is no match
-   For subsequences, use dynamic programming as there are overlapping subproblems. Check out [this question](https://leetcode.com/problems/longest-palindromic-subsequence/).

# References
[Tech Interview](https://www.techinterviewhandbook.org/algorithms/string/)