class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for word in strs:
            key = "".join(sorted(word))
            if key in dict:
                dict[key].append(word)
            else:
                dict[key] = [word]
        
        return list(dict.values())