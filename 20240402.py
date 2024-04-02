class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = {c:s.index(c) for c in set(list(s))}
        map_t = {c:t.index(c) for c in set(list(t))}
        new_s = [map_s[c] for c in s]
        new_t = [map_t[c] for c in t]
        return new_s==new_t
        