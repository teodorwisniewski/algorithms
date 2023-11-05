


class Solution:
    def maxProduct(self, s: str) -> int:
        # nb of letters
        N = len(s)
        # hash map
        palidromes = {}  # mask: nb of letter in the palidrome

        # 2**N == 1 << N
        for bit_mask in range(1, 1 << N): 
            subseq = self.extract_subseq(s, bit_mask, N)
            if subseq == subseq[::-1]:
                palidromes[bit_mask] = len(subseq)
        
        res = 0
        for m1 in palidromes:
            for m2 in palidromes:
                # check if palidromes are disjonted
                if not (m1 & m2):
                    res = max(res, palidromes[m1] * palidromes[m2])
        return res

    def extract_subseq(self, s, mask, N) -> str:
        new_subseq = ""
        for i in range(N):
            #  bitwise left shift operation
            if (mask & 1 << i):
                new_subseq += s[i]
        
        return new_subseq


sol = Solution()
s = "leetcodecom"
res = sol.maxProduct(s)
print(f"maxProduct {res}")