"""
#1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


"""

# Solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # dictionary that maps the number with their index

        for i in range(len(nums)):
            number = nums[i]
            desired = target - number #target minus the current number 
            if desired in seen: #if desired number already in seen, return the current index with desired's index
                return [i, seen[desired]]
            seen[number] = i # if first time, add the number with its index to the dic
        
        return None #problems gaurantee a solution

"""
Time: O(n) where n = length of the list
Space: O(n)

"""