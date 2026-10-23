class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        closest = 10000
        closest_row = None
        for i in range(len(matrix)):
            if matrix[i][0] <= target:
                closeness = target - matrix[i][0]
                if closeness < closest:
                    closest = closeness
                    closest_row = i
        mid = closest_row
        if mid == None:
            return False

        l = 0
        r = len(matrix[mid]) - 1

        while l<=r:
            middle = (l + r) // 2
            if matrix[mid][middle] == target:
                return True
            elif matrix[mid][middle] < target:
                l = middle + 1
            else:
                r = middle - 1

        return False

            