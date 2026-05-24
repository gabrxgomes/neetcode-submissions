class Solution:
    def isPalindrome(self, s: str) -> bool:
        #if not s: return False

        res = "".join(c for c in s.lower() if c.isalnum())

        #hasher = {}
        #for idx, i in enumerate(res):
            #if hasher.get(i) is not None:
                #return [hasher.get(i), idx]
            #hasher[]
        return res == res[::-1]

