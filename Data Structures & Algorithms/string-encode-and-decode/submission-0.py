class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        # i need a way to differentiate between different words

        tilde = "ñ" 

        for string in strs:
            encoded_string += string + tilde

        return encoded_string


    def decode(self, s: str) -> List[str]:
        # we are using a tilde as a delimiter
        tilde = "ñ" 

        output_array = []
        building_string = ""

        for char in s:
            if char == tilde:
                output_array.append(building_string)
                building_string = ""
            else:
                building_string += char

        return output_array
