"""
#128 Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

# Solution:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # First, turn the list to set
        num_set = set(nums)
        longest = 0 # keep track of the longest sequence so far

        for n in num_set:
            if n-1 not in num_set: # check if the number is the start of a sequence; i.e. no left neighbot
                length = 0 # if it is, check how long is the sequence
                while n+length in num_set: # start with the current number, and update the length/number by adding 1
                    length += 1
                longest = max(length, longest) # update the longest sequence
        
        return longest


        

"""
Here, time complexity is O(n). The worst case for the nested loop is visiting every number twice.
i.e., if there's no sequence > 1; e.g.[1,3,5], no number have left neighbor but also they don't 
form a sequence > 1. So for each number, the "if" statement satisfy and the while loop will run.

Or a long sequence [1,2,3,4], for num = 1 it runs every other number through the while loop, and when 
visiting other number it only run through the outer loop. So worst case O(2n) = O(n)

Space also O(n) since we create a new set.

n is the length of input array.
"""
        