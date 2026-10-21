class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = "~"
        built = ""
        for string in strs:
            built += string + delimiter

       
        print(built)
        return built


    def decode(self, s: str) -> List[str]:
        delimiter = "~"
        built = ""
        sentence = []

        for char in s:
            if char != delimiter:
                built += char
            else:
                sentence.append(built)
                built = ""


        return sentence
