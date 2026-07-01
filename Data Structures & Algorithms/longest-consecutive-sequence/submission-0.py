class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        startSet = set()
        
        for num in nums:
            numSet.add(num)

        for num in numSet:
            if num - 1 not in numSet:
                startSet.add(num)

        max = 0
        for start in startSet:
            for start in startSet:
                length = 1
                while start + length in numSet:
                    length += 1
                if length > max:
                    max = length

        return max