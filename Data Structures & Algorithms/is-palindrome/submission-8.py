class Solution:
    def isPalindrome(self, s: str) -> bool:
        #if not s: return False

        res = "".join(c for c in s.lower() if c.isalnum())

        return res == res[::-1]

