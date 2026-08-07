class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # given: 'nums' and 'k'
        # return the k most frequent elements in the array

        # bucket sort is the most efficient way of solving apparently

        dictionary = {}

        for number in nums:
            if number not in dictionary:
                dictionary[number] = 1
            else:
                dictionary[number] += 1

        bucket = [[] for _ in range(len(nums) + 1)] # index represents frequency

        for number in dictionary:
            frequency = dictionary[number]
            bucket[frequency].append(number)

        counter = 0

        output = []

        for i in range(len(bucket) - 1, -1, -1):
            for number in bucket[i]:
                output.append(number)
                if len(output) == k:
                    return output

        return output




