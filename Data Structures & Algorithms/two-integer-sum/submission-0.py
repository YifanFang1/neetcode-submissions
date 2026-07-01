class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            goal = target - num

            if goal in hashmap:
                return [hashmap[goal], i]
            
            hashmap[num] = i