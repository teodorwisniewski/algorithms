



def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    ways = [0 for _ in range(n+1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] += ways[amount-denom]
    return ways[-1]


denoms = [1, 5, 10]
target = 10
res = numberOfWaysToMakeChange(target, denoms)
print(f"donoms {denoms} target={target}")
print(f"numberOfWaysToMakeChange {res}")