from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            characters = [0] * 26 # Index for a -> z
            for char in s:
                characters[ord(char) - ord("a")] += 1
            anagrams[tuple(characters)].append(s)
        
        return list(anagrams.values())

