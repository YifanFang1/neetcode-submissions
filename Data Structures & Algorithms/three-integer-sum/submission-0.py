class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            goal = -nums[i]
            start = i + 1
            end = len(nums) - 1
            while start < end:
                value = nums[start] + nums[end]
                if value == goal:
                    result.append([nums[i], nums[start], nums[end]])
                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    while start < end and nums[end] == nums[end-1]:
                        end -= 1
                    start += 1
                    end -= 1
                elif value < goal:
                    start += 1
                else:
                    end -= 1
        return result