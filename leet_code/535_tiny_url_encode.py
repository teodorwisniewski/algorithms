
class Codec:

    def __init__(self):
        self.encoded_map = {}
        self.decoded_map = {}
        self.base_url = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encoded_map:
            hash_key = str(len(self.encoded_map) + 1)
            short_url = self.base_url + hash_key
            self.encoded_map[longUrl] = short_url
            self.decoded_map[short_url] = longUrl
        return short_url
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decoded_map[shortUrl]
        






url = "https://leetcode.com/problems/design-tinyurl"

codec = Codec()
encoded_url = codec.encode(url)
print(f"encoded_url {encoded_url}")
decoded_url = codec.decode(encoded_url)
print(f"decoded_url {decoded_url}")