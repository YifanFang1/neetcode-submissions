class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for num in nums:
            # some check here
            if num in hashset:
                return True
            hashset.add(num)

        return False