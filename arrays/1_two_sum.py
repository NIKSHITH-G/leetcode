class Solution(object):
    def twoSum(self, nums, target):

        hashmap = {}

        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[nums[i]] = i


"""
Approach:
- Use a hashmap to store number -> index
- For each number, calculate the complement needed
- Check if complement already exists in hashmap
- If yes, return both indices
- Otherwise store current number

Example:
nums = [2,7,11,15]
target = 9

2 needs 7
7 already found -> return [0,1]

Time Complexity: O(n)
Space Complexity: O(n)
"""