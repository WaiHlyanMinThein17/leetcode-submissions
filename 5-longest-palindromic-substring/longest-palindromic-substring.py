class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, max_len = 0, 0

        for i in range(len(s)):
            len1 = self.expand_from_center(s, i, i)
            len2 = self.expand_from_center(s, i, i + 1)

            current_len = max(len1, len2)
            if current_len > max_len:
                max_len = current_len
                start = i - (current_len - 1) // 2

        return s[start : start + max_len]

    def expand_from_center(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1