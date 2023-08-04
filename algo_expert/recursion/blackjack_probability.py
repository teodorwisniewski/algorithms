



#  TC O(t-s) SC O(t-s)
def blackjackProbability(target, startingHand):
    memo = {}
    return rec_helper(target, startingHand, memo)


def rec_helper(target, startingHand, memo):
    if  (target - 4) <= startingHand <= target:
        return 0
    if startingHand in memo:
        return memo[startingHand]
    
    prob = 0.0 
    for card_nb in range(1, 11):
        new_startingHand = startingHand + card_nb
        if new_startingHand < target - 4:
            prob += 0.1 * rec_helper(target, new_startingHand, memo)
        elif new_startingHand > target:
            prob += 0.1
    memo[startingHand] = round(prob, 3)
    return memo[startingHand]



target = 21
startingHand = 15
res = blackjackProbability(target, startingHand)
print(f"taget={target} startingHand={startingHand}")
print(f"blackjackProbability {res}")


target = 100
startingHand = 90
res = blackjackProbability(target, startingHand)
print(f"taget={target} startingHand={startingHand}")
print(f"blackjackProbability {res}")