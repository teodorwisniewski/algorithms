



class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mappint_s = {}
        mapping_t = {}

        for ch_s, ch_t in zip(s, t):

            if (
                (ch_s in mappint_s and mappint_s[ch_s] != ch_t) or
                (ch_t in mapping_t and mapping_t[ch_t] != ch_s)
            ):
                return False
        
            mappint_s[ch_s] = ch_t
            mappint_s[ch_t] = ch_s

        return True

sol = Solution()


s = "paper"
t = "title"
res = sol.isIsomorphic(s, t)
print(f"s={s} t={t} isIsomorphic {res}")
assert res


s = "foo"
t = "bar"
res = sol.isIsomorphic(s, t)
print(f"s={s} t={t} isIsomorphic {res}")
assert not res
