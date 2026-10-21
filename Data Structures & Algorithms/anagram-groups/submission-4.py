class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted not in hashmap:
                hashmap[s_sorted] = []
                hashmap[s_sorted].append(s)
            else:
                hashmap[s_sorted].append(s)

        anagrams = []
        for key in hashmap:
            anagrams.append(hashmap[key])

        return anagrams
            
            