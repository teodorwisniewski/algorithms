from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []
        if len(s) > 12:
            return res
        
        def backtrack(idx, dots, curr_ip: str):

            if idx == len(s) and dots == 4:
                res.append(curr_ip[:-1])
                return
            if dots > 4:
                return
            
            for i in range(idx, min(idx+3, len(s))):

                integer = s[idx:i+1]
                if int(integer) < 256 and (len(integer) == 1 or not integer.startswith("0")):
                    backtrack(i+1, dots+1, curr_ip + integer + ".")
                
        backtrack(0, 0, "")
        return res



s = Solution()

# input = "25525511135"
# res = s.restoreIpAddresses(input)
# print(f"restoreIpAddresses {res}")

res = s.restoreIpAddresses("0000")
print(f"restoreIpAddresses {res}")
