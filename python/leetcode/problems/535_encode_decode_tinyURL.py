class Codec:

    rootURL = 'http://tinyurl.com/'
    URLs = {}
    index = 0

    def encode(self, longUrl: str) -> str:
        answer = format(self.index, '08x')
        self.index += 1
        self.URLs[answer] = longUrl
        return self.rootURL + answer
        """Encodes a URL to a shortened URL.
        """
        
    def decode(self, shortUrl: str) -> str:
        if not shortUrl.startswith(self.rootURL):
            raise Exception(f'{shortUrl=} must begin with "{self.rootURL}"')
        hexCode = shortUrl[len(self.rootURL):]
        print(f'--> {hexCode=}')
        return self.URLs[hexCode]
        """Decodes a shortened URL to its original URL.
        """
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
