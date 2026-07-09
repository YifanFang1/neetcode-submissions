class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_f = 0
        char_count = {}
        max_len = 0

        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            max_f = max(max_f, char_count[s[right]])

            if (right - left + 1) - max_f > k:
                char_count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len