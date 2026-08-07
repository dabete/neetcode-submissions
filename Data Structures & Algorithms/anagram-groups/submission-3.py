class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input - an array of strings 'strs'
        # what we need to do:
        # group all anagrams together into sublists
        # you may return the output in any order

        strs_sorted = [""]*len(strs)

        for i in range(len(strs)):
            strs_sorted[i] = "".join(sorted(strs[i]))

        dictionary = {}

        for i in range(len(strs_sorted)):
            if strs_sorted[i] not in dictionary:
                dictionary[strs_sorted[i]] = [strs[i]]
            else:
                array_modify = dictionary[strs_sorted[i]]
                array_modify.append(strs[i])
                dictionary[strs_sorted[i]] = array_modify

        output_array = []

        for anagram in dictionary:
            output_array.append(dictionary[anagram])

        return output_array