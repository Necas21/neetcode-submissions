class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        # Keep looping until left and right pointer meet
        while left < right:
            # Skip all non alphanumeric characters from the left
            while not s[left].isalnum() and left < right:
                left += 1
            # Skip all non alphanumeric characters from the right
            while not s[right].isalnum() and left < right:
                right -= 1
            # Check if characters are not equal, ignore case sensitivity
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True