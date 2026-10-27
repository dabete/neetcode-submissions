class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, best, substring = 0, 0, 0, 0
        for r in range(len(s)):
            # z x y z x y z
            substring += 1
            while l <= r and s[r] in s[l:r]:
                l += 1
                substring -= 1
            best = max(best, substring)

        return best



            
      



