class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # inputs - strings 's' and 't'

        # we are going to need hashmaps

        left = 0

        output = ""

        t_dict = {}
        s_dict = {}

        # populate t_dict
        for char in t:
            t_dict[char] = 1 + t_dict.get(char, 0)

        
        for right in range(len(s)):

            compare = True

            # add s[right] to s_dict 
            s_dict[s[right]] = 1 + s_dict.get(s[right], 0)

            # compare dictionaries
            valid = True
            for key in t_dict:
                if t_dict[key] > s_dict.get(key, 0):
                    valid = False
                    compare = False
            
            # if the substring is valid - minimise
            while valid:
                s_dict[s[left]] -= 1
                left += 1
                
                # check whether still valid
                for key in t_dict:
                    if t_dict[key] > s_dict.get(key, 0):
                        valid = False

            if compare:
                if output == "":
                    output = s[left - 1: right + 1]

                elif len(output) > len(s[left - 1: right + 1]):
                    output = s[left - 1: right + 1]

                
        return output

                




            


