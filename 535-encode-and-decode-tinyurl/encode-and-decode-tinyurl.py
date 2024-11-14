class Codec:

    def __init__(self) -> None:
        self.hm: Dict[str, str] = dict()
        self.urlCounter: int = 0

    def encode(self, longUrl: str) -> str:
        """
        Encodes a URL to a shortened URL.
        """
        encoded = str(self.urlCounter)
        self.hm[encoded] = longUrl
        self.urlCounter += 1

        return encoded
        

    def decode(self, shortUrl: str) -> str:
        """
        Decodes a shortened URL to its original URL.
        """
        return self.hm[shortUrl]
        