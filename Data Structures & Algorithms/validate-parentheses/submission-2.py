class Solution:
    def isValid(self, s: str) -> bool:
        # Mapping to lookup matching parentheses
        mapping = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        # Stack to store open parentheses
        parentheses = []

        for char in s:
            # Push all open parenthese to stack
            if char in "({[":
                parentheses.append(char)
            else:
                if len(parentheses) > 0:
                    # Pop open parentheses and check if char is the corresponding close
                    last_opened = parentheses.pop()
                    if char != mapping.get(last_opened, ""):
                        return False
                # If the length of the stack is 0 there is a parenthese mis-match
                else:
                    return False
        
        # Check the stack is empty to confirm all parentheses matched
        return len(parentheses) == 0

