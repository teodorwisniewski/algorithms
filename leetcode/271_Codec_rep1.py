from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
        """
        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word)) + "#" + word
        return encoded_str
        
    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string to a list of strings.
        """

        idx = 0
        res = []
        while idx < len(s):
            j = idx
            while s[j] != "#":
                j += 1
            word_len = int(s[idx:j])
            word = s[j+1:j+1+word_len]
            res.append(word)
            idx = j+1+word_len
        return res




codec = Codec()
dummy_input = ["Hello","World"]
encoded_str = codec.encode(dummy_input)
print(f"encoded_str {encoded_str}")
dencoded_str = codec.decode(encoded_str)
print(f"dencoded_str {dencoded_str}")