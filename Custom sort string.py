class Solution:
    def customSortString(self, order: str, s: str) -> str:
        key = ""
        for ch in order:
            a = s.count(ch)
            for i in range(a):
                key += ch
        
        for ch in s:
            if ch not in order:
                key += ch
        
        return key