"""
# 242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


"""

# Solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False # if two string are not same in length, definitely not anagram
        count_s, count_t = {},{} # dictionaries for 2 words to map the letter with their count
        for i in range(len(s)): # here already confirms that the length is the same
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1

        return count_s == count_t
        

"""
Time: O(n) where n = length of the list
Space: O(n) if not bounded(i.e. unicode, arbitrary characters), else O(1) since at most 26 distinct keys

"""