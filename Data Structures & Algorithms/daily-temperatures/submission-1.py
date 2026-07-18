class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        # Iterate over temperatures
        for i, temp in enumerate(temperatures):
            # While the stack is not empty
            while stack:
                # If the current temp > last temp in stack
                if temp > stack[-1][1]:
                    # Set the index of result to i - last values index and pop the stack
                    last_temp = stack.pop()
                    result[last_temp[0]] = i - last_temp[0]
                else:
                    break
            # Push current index and temp to the stack
            stack.append((i, temp))
        return result
                