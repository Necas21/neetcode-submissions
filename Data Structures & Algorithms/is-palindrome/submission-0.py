class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non alpha-numeric characters
        s = "".join([char for char in s if char.isalnum()])
        for i in range(len(s) // 2):
            if s[i].lower() != s[len(s) - 1 - i].lower():
                return False
        return True