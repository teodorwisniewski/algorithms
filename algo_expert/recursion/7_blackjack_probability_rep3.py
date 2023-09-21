

#  TC O(t-s) SC O(t-s)
def blackjackProbability(target, startingHand):
    cache = {}
    return round(calculate_prob(target, startingHand, cache), 3)


def calculate_prob(target, currentHand, cache):
    
    if currentHand in cache:
        return cache[currentHand]
    
    if currentHand > target:
        return 1
    
    if currentHand + 4 >= target:
        return 0
    
    total_prob = 0
    for current_drawn in range(1, 11):
        total_prob += 0.1 * calculate_prob(target, currentHand + current_drawn, cache)

    cache[currentHand] = total_prob
    return total_prob


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