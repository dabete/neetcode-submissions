class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        max_length = 0

        for number in nums:
            # check that a number is the start of a sequence
            if (number - 1) not in numsSet:
                length = 0
                while (number + length) in numsSet:
                    length += 1
                    
                max_length = max(length, max_length)

        return max_length
            

            



