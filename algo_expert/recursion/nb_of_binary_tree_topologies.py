
def numberOfBinaryTreeTopologies(n, dp=None):
    if dp is None:
        dp = {}
    if n in dp:
        return dp[n]
    if n == 0:
        return 1
    total_nb_of_trees = 0
    for l in range(n):
        r = n - 1 - l
        nb_left = numberOfBinaryTreeTopologies(l)
        nb_right = numberOfBinaryTreeTopologies(r)
        total_nb_of_trees += nb_left * nb_right
    dp[n] = total_nb_of_trees
    return total_nb_of_trees


n = 3
res = numberOfBinaryTreeTopologies(n)
print(f"numberOfBinaryTreeTopologies {res}")


n = 4
res = numberOfBinaryTreeTopologies(n)
print(f"numberOfBinaryTreeTopologies {res}")

n = 5
res = numberOfBinaryTreeTopologies(n)
print(f"numberOfBinaryTreeTopologies {res}")