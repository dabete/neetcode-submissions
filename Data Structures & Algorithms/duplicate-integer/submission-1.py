class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for num in nums:
            if num not in duplicate:
                duplicate[num] = 1
            else:
                duplicate[num] += 1

        for num in duplicate:
            if duplicate[num] > 1:
                return True

        return False