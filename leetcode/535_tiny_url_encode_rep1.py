
class Codec:

    def __init__(self):
        self.encoded_urls = {}
        self.decoded_urls = {}
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        hash_key = str(len(self.encoded_urls) + 1)
        short_url = self.base + hash_key
        if longUrl not in self.encoded_urls:
            self.encoded_urls[longUrl] = short_url
            self.decoded_urls[short_url] = longUrl
        return short_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decoded_urls[shortUrl]
     






url = "https://leetcode.com/problems/design-tinyurl"

codec = Codec()
encoded_url = codec.encode(url)
print(f"encoded_url {encoded_url}")
decoded_url = codec.decode(encoded_url)
print(f"decoded_url {decoded_url}")