class Codec:
    def __init__(self):
        self.alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
        self.dict1 = {} # translate long to short
        self.dict2 = {} # translate short to long

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while longUrl not in self.dict1:
            
            combination = "".join(choices(self.alphabet,k=8))
            
            if combination not in self.dict2:
                
                self.dict1[longUrl] = combination
                self.dict2[combination] = longUrl
                
        return "http://tinyurl.com/"+str(combination)
            
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.dict2[shortUrl[-8:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
