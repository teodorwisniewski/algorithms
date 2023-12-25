

def nonConstructibleChange(coins):
    
    coins.sort()

    total = 0
    for coin in coins:
        if total + 1 < coin:
            return total + 1
        total += coin
    return total+1



coins = [5, 7, 1, 1, 2, 3, 22]

res = nonConstructibleChange(coins)
print(f"nonConstructibleChange {res}")

coins = [1, 1, 3]

res = nonConstructibleChange(coins)
print(f"nonConstructibleChange {res}")