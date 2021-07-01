class Solution:

    def strStr(self, haystack: str, needle: str) -> int:

        return haystack.index(needle) if needle in haystack else 0 if not needle else -1
