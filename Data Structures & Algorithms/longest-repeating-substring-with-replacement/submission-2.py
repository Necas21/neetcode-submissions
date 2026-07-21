from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1

        # Sliding window pointers
        left = 0

        # Track substring max length
        max_length = 0

        # Stores counts of characters seen
        counts = defaultdict(int)

        for right in range(len(s)):
            # Add new value to counts dict
            counts[s[right]] += 1

            # Get the most common character in the substring
            most_common = max(counts.values())

            # Move left pointer in
            while (right - left + 1) - most_common > k:
                counts[s[left]] -= 1
                left += 1
                most_common = max(counts.values())
            
            max_length = max(max_length, (right - left + 1))
        
        return max_length