"""
#347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2 --> Output: [1,2]

Example 2:

Input: nums = [1], k = 1 --> Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2 --> Output: [1,2]

 
Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 
Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

# Solution 1:

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {} 
        
        # Map each numer with their corresponding counts
        for num in nums:
            seen[num] = seen.get(num, 0) + 1 # .get() method has O(1), so here O(n)
            
        # sort the dictionary in descending order by the values(x[1] is value, x[0] is key)
        # sort has O(nlogm)
        seen_sorted = dict(sorted(seen.items(), key = lambda x:x[1], reverse = True))

        result = list(seen_sorted.keys())
        return result[0:k]
"""
Here, time complexity is O(n) + O(nlogn) = O(nlogn). 
Space complexity is O(n). 
"""

# Solution 2:
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} 
        
        # bucket_sort list, where index is frequency and freq[i] holds number that appear i times
        freq = [[] for i in range(len(nums)+ 1)] # O(n)

        # mapping numbers with their counts
        for num in nums:
            count[num] = count.get(num, 0) + 1 # O(n)
        
        # fill the bucket array by frequency
        for n,c in count.items():
            freq[c].append(n) #O(n)
        
        # creating result array for the top k number
        result = []
        #starting from the most frequent num
        for i in range(len(freq) - 1, 0, -1): # entire nested loop is O(n) because two loops visit each number exactly once
            for n in freq[i]:                 
                result.append(n) # append each number in freq[i]
                if len(result) == k: # if find the top k, return result
                    return result
"""
Here, time complexity is O(n) + O(n) + O(n) + O(n) = O(n). 
The reason that the last nested loop is also O(n) is that
the two loops together visit each number exactly once even in the worst case.

E.g. count = {1:1, 2:1, 3:1, 4:1, 5:1}
freq = [[], [], [], [], [], []]      # 6 buckets (n+1)
# every number appeared once, so they all go into freq[1]:
freq[1] = [1, 2, 3, 4, 5]            # ALL n numbers in one bucket
freq[2..5] = []                       # all empty

for i in range(5, 0, -1):    # walks buckets 5,4,3,2,1
    for n in freq[i]:
        result.append(n)

Buckets 5,4,3,2: empty → inner loop runs 0 times each
Bucket 1: has all n numbers → inner loop runs n times

Count the total inner-body executions: 0+0+0+0+n = n times. Still n instead of n*n times.

Space complexity is O(n). 
"""
        