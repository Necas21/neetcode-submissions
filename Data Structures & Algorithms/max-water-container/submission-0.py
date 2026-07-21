class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Store the maximum volume of water
        max_volume: int = 0

        # Initialise left and right pointers to the start and end of heights
        left: int = 0
        right: int = len(heights) - 1

        # While the pointers do not intersect
        while left < right:
            # Calculate the current volume
            current_volume = (right - left) * min(heights[left], heights[right])
            # Set max_volume to max(max_volume, current_volume)
            max_volume = max(max_volume, current_volume)
            # If heights[left] < heights[right] increment left
            if heights[left] < heights[right]:
                left += 1
            # If heights[right] < heights[left] decrement right
            else:
                right -= 1
        return max_volume
