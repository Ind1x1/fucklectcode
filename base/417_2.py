# 最长回文子串
# 给你一个字符串 s，找到 s 中最长的 回文 子串。
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        def expand_around_center(left: int, right: int) -> Tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            l1, r1 = expand_around_center(i, i)
            l2, r2 = expand_around_center(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]






