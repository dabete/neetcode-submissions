class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [0]*len(nums)
        r = [0]*len(nums)
        
        # populate l and r arrays
        for i in range(len(nums)):
            if i == 0:
                l[i] = nums[i]
            else:
                l[i] = nums[i] * l[i-1]
            
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                r[i] = nums[i]
            else:
                r[i] = nums[i] * r[i+1]

        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(r[i + 1])
            elif i == len(nums) - 1:
                output.append(l[i - 1])
            else:
                output.append(l[i - 1] * r[i + 1])

        return output

