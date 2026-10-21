class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            look_for = target - nums[i]
            if look_for in seen:
                minIndex = min(i, seen[look_for])
                maxIndex = max(i, seen[look_for])
                return [minIndex, maxIndex]

            else:
                seen[nums[i]] = i
            
    