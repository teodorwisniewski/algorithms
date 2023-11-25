



class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(nums)
        prefix = [0] * (n+1)
        postfix = [0] * (n+1)

        for idx in range(1, n+1):
            if customers[idx-1] == "N":
                prefix[idx] += 1

        for idx in range(n+1, -1, 1):
            if customers[idx] == "Y":
                postfix[idx] += 1    

        penalty_idx, penalty = 0, float("inf")       

        for      

        return penalty_idx

        


        



sol = Solution()
customers = "YYNY"
res = sol.bestClosingTime(customers)
print(f"bestClosingTime is {res}")
assert res == 2