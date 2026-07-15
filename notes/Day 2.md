# Day 1 — [2026/7/15]

**Week:** 1 · **Focus today:** Harvard Python Class week1, CS50P PS0, 

## What I did
- Read the AIE article on lantent.space

## What I actually understood (in my own words)
- input automatically returns a string, no need to have a **str** around it
- ### Ways to professionalize code:
    - use pure functions: same input -> same output, no side effects like print or input
    - use dictionaries for mapping questions; dictionary is a hash table with lookup time O(1)
- Code core: hand-written programs control the flow of the project; LLM called as a tool in this program
- LLM core: LLM controls the workflow, decides which hand-written tools to be called
- ### My openclaw projects
    - Mix of code core and LLM core
    - Most of the project: code core. The programs decides when to call LLM
    - Team-leader orchestration: LLM core. LLM decides which agent to delegate to; my code is the constraint: whether the session-spawn or the deny of the tools such as ```web-search``` or ```web-fetch```

## What confused me / still don't get
- 

## LeetCode today
- Tried #1 Two Sum. Didn't get it correct the first time and here's the code:
```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            numbers = nums[i]
            seen[numbers] = i
            desired = target - numbers
            if desired in seen:
                return [i,seen[desired]]
        return null
```
- This is wrong because the number is stored before checking the desired. if [3,2,4], target = 6, then {3:0} stored first and after checking 3+3=6, it will return [0,0] instead of [1,2]. Should check seen first then store it. Also null doesn't exist in python, should be None. The correct code is:
```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            numbers = nums[i]
            desired = target - numbers
            if desired in seen:
                return [i,seen[desired]]
            seen[numbers] = i
    return None
```

## Tomorrow's first task
-
