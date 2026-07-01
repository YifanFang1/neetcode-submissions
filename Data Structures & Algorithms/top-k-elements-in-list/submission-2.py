class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}

        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        pairs = []
        for num in dict:
            pairs.append([dict[num], num])
        
        for i in range(len(pairs)):
            for j in range(len(pairs) - 1):
                if pairs[j][0] < pairs[j+1][0]:
                    pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
        
        output = []
        for i in range(k):
            output.append(pairs[i][1])
        
        return output
        
