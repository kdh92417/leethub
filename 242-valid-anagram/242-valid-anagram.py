class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = collections.Counter(s)
        t_dict = collections.Counter(t)
        
        for k, v in s_dict.items():
            if v != t_dict[k]:
                return False
        
        return sum(s_dict.values()) == sum(t_dict.values())