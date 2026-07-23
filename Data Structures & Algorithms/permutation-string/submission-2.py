from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # len(s1) must be <= len(s2)
        if len(s1) > len(s2):
            return False

        # Dict to track count of chars in s1 and s2
        s1_count = [0] * 26
        s2_count = [0] * 26

        # Populate counts
        for i in range(len(s1)):
            char_s1 = s1[i]
            s1_count[ord(char_s1) - ord("a")] += 1
            char_s2 = s2[i]
            s2_count[ord(char_s2) - ord("a")] += 1
        
        if s1_count == s2_count:
            return True

        # Left and right pointers
        left = 0
        right = len(s1)

        # Iterate over s2 until end
        while right < len(s2):
            print(s2_count)
            # Update s2_count
            s2_count[ord(s2[left]) - ord("a")] -= 1
            s2_count[ord(s2[right]) - ord("a")] += 1
            # If the counts match we have found a valid substring
            if s1_count == s2_count:
                return True
            else:
                right += 1
                left += 1 
        return False

