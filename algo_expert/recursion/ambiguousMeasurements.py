

# O(low * high * n) time | SC O(low*high)
def ambiguousMeasurements(measuringCups, low, high):
    dp = {}
    return can_measure_in_range(measuringCups, low, high, dp)


def can_measure_in_range(measuringCups, low, high, dp) -> bool:
    hashable_key = (low, high)
    if hashable_key in dp:
        return dp[hashable_key]
    
    if low < 0 and high < 0:
        return False
    
    can_measure = False
    for cup_low, cup_high in measuringCups:
        if low <= cup_low and cup_high <= high:
            can_measure = True
            break

        new_low = low - cup_low
        new_high = high - cup_high
        can_measure = can_measure_in_range(measuringCups, new_low, new_high, dp)
        if can_measure:
            break

    dp[hashable_key] = can_measure
    return can_measure






measuringCups = [
  [200, 210],
  [450, 465],
  [800, 850],
] 

low  = 2100
high = 2300

res = ambiguousMeasurements(measuringCups, low, high)
print(f"ambiguousMeasurements {res}")

assert res