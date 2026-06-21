class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        data_s, data_t = dict(), dict()

        for ch in s:
            data_s[ch] = data_s.get(ch, 0) + 1
            
        for ch in t:
            data_t[ch] = data_t.get(ch, 0) + 1
        
        return data_s == data_t