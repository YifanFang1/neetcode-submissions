class Solution:
    def encode(self, strs: List[str]) -> str:
        coded = ""
        for s in strs:
            coded = coded + s + '/'
        return coded

    def decode(self, s: str) -> List[str]:
        list = []
        word = ""
        for c in s:
            if c == '/':
                list.append(word)
                word = ""
            else:
                word += c
        return list

