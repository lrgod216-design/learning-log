# Day 4 — [2026/7/21]

**Week:** 1 · **Focus today:** 

## What I did
- 2 neetcode problems: group anagram and topk frequent elements
- continue watching Dave's video on python for aie
## What I actually understood (in my own words)
- 


## What confused me / still don't get
- 

## NeetCode today

### Group Anagram
```
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list) # automatically creates an empty list if the key is not there

        for word in strs:
            count = [0] * 26 # Refers to the 26 letters

            for letter in word:
                count[ord(letter) - ord('a')] += 1 # 0 to a, 1 to b, 2 to c....
            key = tuple(count)
            
            result[key].append(word)
        
        return list(result.values())
```
- Using defaultdict(list) automatically creates an empty list if the key.values() doesn't appear
- Key idea: the key of the dictionary is ```count```, and ```count``` represents tbe number of 26 letters in each string. Using ```ord()``` returns the ASCII value of the letter, and make sure index 0 represents 'a', 1 to 'b', 2 to 'c'...
- Finally, we can apend the word to their corresponding count

### Top K frequent elements
- Visit leetcode section for more detailed explanation

## Tomorrow's first task
- 
