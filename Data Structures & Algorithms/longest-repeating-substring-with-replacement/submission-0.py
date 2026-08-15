class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # input - string 's' , only uppercase english characters
        # input - integer 'k'
        # what we need to do:
        # choose up to k characters of the string and replace them with any other uppercase English character

        # after performing at most k replacements, return the length of the longest substring which contains only one distinct character

        # topics: hashtable, sliding window

        left = 0
        dictionary = {}
        longest_substring = 0

        for right in range(len(s)):
            dictionary[s[right]] = 1 + dictionary.get(s[right], 0)

            while (right - left + 1) - max(dictionary.values()) > k:
                dictionary[s[left]] -= 1
                left += 1

            longest_substring = max(longest_substring, right - left + 1)

        return longest_substring






              