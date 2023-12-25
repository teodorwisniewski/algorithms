
def numberOfBinaryTreeTopologies(n, dp={0: 1}):

    if n in dp:
        return dp[n]
    
    total_nb = 0
    for right in range(n):
        left = n - 1 - right
        right_nb = numberOfBinaryTreeTopologies(right, dp)
        left_nb = numberOfBinaryTreeTopologies(left, dp)
        total_nb += right_nb * left_nb
    return total_nb



n = 3
res = numberOfBinaryTreeTopologies(n)
print(f"numberOfBinaryTreeTopologies {res}")


n = 4
res = numberOfBinaryTreeTopologies(n)
print(f"numberOfBinaryTreeTopologies {res}")

n = 5
res = numberOfBinaryTreeTopologies(n)
print(f"numberOfBinaryTreeTopologies {res}")