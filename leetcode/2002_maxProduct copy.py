


class Solution:
    def maxProduct(self, s: str) -> int:
        N = len(s)
        hash_map_bit_mask_len = {}
        # 2**N
        for bit_mask in range(1, 1 << N):
            subseq = ""
            for i in range(N):
                if bit_mask & (1 << i):
                    subseq += s[i]
            
            if subseq == subseq[::-1]:
                hash_map_bit_mask_len[bit_mask] = len(subseq)
        
        res = 0
        for m1 in hash_map_bit_mask_len:
            for m2 in hash_map_bit_mask_len:
                if (m1 & m2) == 0:
                    res = max(res, hash_map_bit_mask_len[m1] * hash_map_bit_mask_len[m2])
        
        return res



 
sol = Solution()
s = "leetcodecom"
res = sol.maxProduct(s)
print(f"maxProduct {res}")