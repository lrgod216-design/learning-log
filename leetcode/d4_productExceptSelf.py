"""
#238. Product of Array Exept Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

# Solution:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        # prefix of the first item of nums is 1
        prefix = 1
        # result first store the prefix of each item in array
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i] # prefix(num) = product of numbers before it

        # then the result stores the product of prefix and postfix
        postfix = 1 # postfix of the last item is 1
        for i in range(len(nums) - 1, -1, -1): # starting from the last item
            result[i] *= postfix # result already the prefix, just multiply the postfix with it
            postfix *= nums[i] # update the postfix, which = the product of number after it
        
        return result
        
        



"""
Here, time complexity O(n), where n is the length of the nums
Space complexity is O(1), result array doesn't count
Potential question can ask in interview:
    1. does result array cost extra space?
    2. can we use division operation?
"""
        