class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #  input - string 's'
        # dynamic sliding window:
        # expands to find a valid state, and contracts from the left to optimise or maintain validity

        left = 0
        longest = 0
        seen_chars = set()

        for right in range(len(s)):
            while s[right] in seen_chars:
                seen_chars.remove(s[left])
                left += 1

            seen_chars.add(s[right])
            longest = max(longest, right - left + 1)

        return longest


            

      



