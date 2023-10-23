
from collections import Counter



# TC O(n) SC O(n)
def majorityElement(array):

    counter = Counter(array)

    maj_el = None
    maj_freq = 0
    for el in array:
        el_freq = counter[el]
        if el_freq > maj_freq:
            maj_el = el
            maj_freq = el_freq
    return maj_el




array = [1, 2, 3, 2, 2, 1, 2]
res = majorityElement(array)
print(f"majorityElement {res}")