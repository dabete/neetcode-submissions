class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # input - array of integers 'numbers' sorted in non-decreasing order (ascending)

        # return the indices of two numbers [index1, index2] such that they add up to a given target number target and index1 < index2.
        # Note that the two indexes cannot be equal

        # the solution must use O(1) space

        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        