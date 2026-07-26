class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Y-axis pointers
        start_y = 0
        end_y = len(matrix) - 1

        # X-axis pointers
        start_x = 0
        end_x = len(matrix[0]) - 1

        # Find the row `target` is on
        while start_y <= end_y:

            # Find mid point of y-axis
            mid_y = ((end_y - start_y) // 2) + start_y

            # Check if target is in the current row
            if target < matrix[mid_y][start_x]:
                end_y = mid_y - 1
            elif target > matrix[mid_y][end_x]:
                start_y = mid_y + 1
            # We have found the correct row
            else:
                # Iterate over x-axis
                while start_x <= end_x:
                    # Find mid point of x-axis
                    mid_x = ((end_x - start_x) // 2) + start_x
                    if target < matrix[mid_y][mid_x]:
                        end_x = mid_x - 1
                    elif target > matrix[mid_y][mid_x]:
                        start_x = mid_x + 1
                    else:
                        return True
                return False
        return False