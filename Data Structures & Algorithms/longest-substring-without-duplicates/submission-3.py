class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # If the string length is <= 1, the max_substring is equal to its length
        if len(s) <= 1:
            return len(s)

        # Set of substring for O(1) lookups
        substring_set: list[str] = []
        substring_max: int = 1

        # Iterate over string
        for i in range(0, len(s)):
            print(substring_set)
            # If s[i] is not part of the substring_set, add it
            if not s[i] in substring_set:
                substring_set.append(s[i])
            else:
                # If s[i] is already in substring_set, update the substring_max value
                # Start new substring_set with characters after duplicate
                substring_max = max(substring_max, len(substring_set))
                index = substring_set.index(s[i])
                substring_set = substring_set[index + 1:]
                substring_set.append(s[i])
        
        return max(substring_max, len(substring_set))