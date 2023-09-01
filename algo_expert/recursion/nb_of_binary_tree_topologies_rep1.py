
def numberOfBinaryTreeTopologies(n, dp={0: 1}):
    if n in dp:
        return dp[n]
    
    total = 0
    for left in range(n):
        r = n - 1 - left
        nb_left_trees = numberOfBinaryTreeTopologies(left)
        nb_right_trees = numberOfBinaryTreeTopologies(r)
        total += nb_left_trees * nb_right_trees
    
    return total


n = 3
res = numberOfBinaryTreeTopologies(n)
print(f"numberOfBinaryTreeTopologies {res}")


n = 4
res = numberOfBinaryTreeTopologies(n)
print(f"numberOfBinaryTreeTopologies {res}")

n = 5
res = numberOfBinaryTreeTopologies(n)
print(f"numberOfBinaryTreeTopologies {res}")