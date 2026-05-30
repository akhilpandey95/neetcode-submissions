class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) >= 1) and len(t) <= ((10**4)*5):
            if s.islower() and t.islower():
                mod_s = list(s)
                mod_t = list(t)
                mod_s.sort()
                mod_t.sort()
                
                return mod_s == mod_t
        
        return False
        