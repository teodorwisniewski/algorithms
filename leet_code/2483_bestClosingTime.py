



class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        n = len(customers)
        prefix = [0] * (n+1)
        postfix = [0] * (n+1)

        for idx in range(1, n+1):
            prefix[idx] = prefix[idx-1]
            if customers[idx-1] == "N":
                prefix[idx] += 1
        
        for idx in range(n-1, -1, -1):
            postfix[idx] = postfix[idx+1]
            if customers[idx] == "Y":
                postfix[idx] += 1        

        penalty_idx, min_pentalty = 0, float("inf")
        for idx in range(n+1):
            penalty = prefix[idx] + postfix[idx]
            if penalty < min_pentalty:
                min_pentalty = penalty
                penalty_idx = idx

        return penalty_idx

        


        



sol = Solution()
customers = "YYNY"
res = sol.bestClosingTime(customers)
print(f"bestClosingTime is {res}")
assert res == 2