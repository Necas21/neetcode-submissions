from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        c1 = dict(Counter(s))
        c2 = dict(Counter(t))

        return c1 == c2




        