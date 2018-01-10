import time
from hashlib import sha1

class Codec:
    counting = 0
    digits = 6
    encoded = {}#long->short
    decoded = {}#short->long
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        while longUrl not in self.encoded:
            if self.counting > 999:
                self.counting = 0
                self.digits += 1
            else:
                self.counting += 1
            timestamp = time.asctime(time.localtime(time.time()))
            shortKey = sha1(longUrl+timestamp).hexdigest()[:self.digits]
            if shortKey not in self.decoded:
                self.encoded[longUrl] = shortKey
                self.decoded[shortKey] = longUrl
        self.counting = 0
        return "http://tinyurl.com/"+shortKey

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        shortKey = shortUrl.split('/')[-1]
        if shortKey in self.decoded:
            return self.decoded[shortKey]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))