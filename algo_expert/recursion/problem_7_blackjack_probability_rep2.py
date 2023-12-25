

#  TC O(t-s) SC O(t-s)
def blackjackProbability(target, startingHand):
    cache = {}
    return round(
        calculate_prob(target, startingHand, cache),
        3
    )


def calculate_prob(target, currentHand, cache):

    if currentHand in cache:
        return cache[currentHand]
    
    # if currentHand > target:
    #     return 1

    if currentHand + 4 >= target:
        return 0
    
    total_prob = 0
    for drawn_hand in range(1, 11):
        cs = drawn_hand + currentHand
        if cs < target-4:
            total_prob += 0.1 * calculate_prob(target, cs, cache)
        elif cs > target:
            total_prob += 0.1

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