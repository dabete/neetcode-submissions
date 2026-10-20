class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric="abcdefghijklmnopqrstuvwxyz1234567890"
        
        l = 0
        
        
        s = s.lower()
        s_list = []
        for char in s:
            if char in alphanumeric:
                s_list.append(char)

        new_s = ""
        for char in s_list:
            new_s += char

        s = new_s
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
            
            
        return True

