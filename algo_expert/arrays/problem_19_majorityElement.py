
from collections import Counter



# TC O(n) SC O(n)
# def majorityElement(array):

#     counter = Counter(array)

#     maj_el = None
#     maj_freq = 0
#     for el in array:
#         el_freq = counter[el]
#         if el_freq > maj_freq:
#             maj_el = el
#             maj_freq = el_freq
#     return maj_el


# def majorityElement(array):
#     maj_el = None
#     maj_freq = 0
#     for el in array:
#         if maj_el == el:
#             maj_freq += 1
#         else:
#             maj_freq -= 1

#         if maj_freq < 0:
#             maj_el = el
#             maj_freq = 1

#     return maj_el


def majorityElement(array):
    answer = 0

    for current_bit in range(32):
        current_bit_val = 1 << current_bit
        ones_count = 0
        for num in array:
         
            if (num & current_bit_val) != 0:
                ones_count += 1

        if ones_count > len(array) / 2:
            answer += current_bit_val
    return answer





array = [1, 7, 3, 7, 7, 1, 7]
res = majorityElement(array)
print(f"majorityElement {res}")