class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word)) + '#' + word
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        while i < len(s):
            j = s.find('#', i)        # find next # starting from i
            length = int(s[i:j])      # number between i and #
            word = s[j+1:j+1+length]  # slice exactly length chars after #
            decoded_list.append(word)
            i = j + 1 + length        # advance past the word
        return decoded_list