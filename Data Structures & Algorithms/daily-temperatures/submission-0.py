class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        # Iterate over each item
        for i in range(len(temperatures)):
            # Iterate over each item from i
            for j in range(i, len(temperatures)):
                # If temperatures[j] > temperatures[i], append j - i to result and break
                if temperatures[j] > temperatures[i]:
                    print(i, temperatures[i], j, temperatures[j], j - i)
                    result[i] = j - i
                    break
        return result