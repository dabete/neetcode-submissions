class Solution:
    def isPalindrome(self, s: str) -> bool:
        # input - string 's'

        # what we need to do:
        # return true if palindrome, else false

        # case insensitive - convert to upper or lower
        # ignores all non-alphanumeric characters

        s_parsed = ""
        alphanumeric = "abcdefghijklmnopqrstuvwxyz1234567890"

        s = s.lower()


        for char in s:
            if char in alphanumeric:
                s_parsed += char

      

        left = 0
        right = len(s_parsed) - 1

        while left < right:
            if s_parsed[left] != s_parsed[right]:
                return False
            left += 1
            right -= 1

        return True