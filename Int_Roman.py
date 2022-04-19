class Solution:
    def intToRoman(self, n: int) -> str:
        d = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
        sum, r = 0,''        
        while n != 0:
            if n in d.keys():        
                r+=d[n]
                n -= n
                continue
            ndig = 1
            for k in d.keys():
                if k < n:
                    ndig = k
                else:
                    break
            n -= ndig
            r += d[ndig]
        return r