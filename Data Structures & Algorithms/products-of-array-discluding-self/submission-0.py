class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # input - integer array 'nums'
        # what we need to do:
        # return an array 'output' where output[i] is the product of all the elements of nums except nums[i]

        # the hard part is doing this in o(n) time, without using the division operation

        # come back to this question later using prefix and postfix stuff

        # for this we need a prefix sum and a postfix sum

        postfix_product = []
        prefix_product = []

        #prefix_product[i]  = nums[1] * nums[2] * ... * nums[i]
        current_number = 1
        for i in range(len(nums)):
            current_number *= nums[i]
            prefix_product.append(current_number)

        current_number = 1
        for i in range(len(nums) - 1, -1, -1):
            current_number *= nums[i]
            postfix_product.append(current_number)
        
        # reverse prefix_product
        postfix_product_reversed = []
        while len(postfix_product) > 0:
            postfix_product_reversed.append(postfix_product.pop())

        postfix_product = postfix_product_reversed

        output = [0]*len(nums)

        # we need to come up with a formula

        for i in range(len(nums)):
            if i == 0:
                output[i] = postfix_product[1]
            elif i == len(nums) - 1:
                output[i] = prefix_product[i - 1]
            else: 
                output[i] = prefix_product[i - 1] * postfix_product[i + 1]

        return output