

# O(low * high * n) time | SC O(low*high)
def ambiguousMeasurements(measuringCups, low, high):
    dp = {}
    return can_measure_in_range(measuringCups, low, high, dp)


def can_measure_in_range(measuringCups, low, high, dp) -> bool:
    hash_key = (low, high)
    if hash_key in dp:
        return dp[hash_key]
    
    if low < 0 and high < 0:
        return False
    
    can_measure = False
    for low_cup, high_cup in measuringCups:
        if low_cup >= low and high_cup <= high:
            return True
        new_low = low - low_cup
        new_high = high - high_cup
        can_measure = can_measure_in_range(measuringCups, new_low, new_high, dp)
        if can_measure:
            return can_measure
        
    dp[hash_key] = can_measure
    return can_measure


# measuringCups = [
#   [200, 210],
#   [450, 465],
#   [800, 850],
# ] 

# low  = 2100
# high = 2300

# res = ambiguousMeasurements(measuringCups, low, high)
# print(f"ambiguousMeasurements {res}")

# assert res

# low  = 100
# high = 120
# [
#     [1, 3],
#     [2, 4],
#     [5, 6]
#   ]

# res = ambiguousMeasurements(measuringCups, low, high)
# print(f"ambiguousMeasurements {res}")
# assert res

high = 1050
low  = 1000
measuringCups = [
    [50, 60],
    [100, 120],
    [20, 40],
    [400, 500]
]

res = ambiguousMeasurements(measuringCups, low, high)
print(f"ambiguousMeasurements {res}")
assert not res