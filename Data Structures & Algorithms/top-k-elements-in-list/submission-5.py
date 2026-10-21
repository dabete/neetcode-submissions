class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        result = []
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1

        while k > 0:
            k -= 1
            maxValue = None
            maxKey = None
            for key in frequency:
                if maxValue == None:
                    maxValue = frequency[key]
                    maxKey = key
                else:
                    if frequency[key] > maxValue:
                        maxValue = max(frequency[key], maxValue)
                        maxKey = key

            result.append(maxKey)
            frequency[maxKey] = 0

        return result
        






