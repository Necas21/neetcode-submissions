from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = dict(Counter(s))
        c2 = dict(Counter(t))

        for k in c1:
            if c1.get(k, 0) != c2.get(k, 0):
                return False

        for k in c2:
            if c1.get(k, 0) != c2.get(k, 0):
                return False
        return True



        