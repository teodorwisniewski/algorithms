from typing import List, Union



def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def findMinEl(array: List, starting_index: int) -> List[Union[int, float]]:
    minValue = float("+inf")
    minIdx = starting_index
    for j in range(starting_index, len(array)):
        if minValue > array[j]:
            minValue = array[j]
            minIdx = j
    return minIdx

# O(n^2) SC O(1)
def selectionSort(array):
    for i in range(len(array)):
        minIdx = findMinEl(array, i)
        swap(array, i, minIdx)
    return array


input_arr = [4, 54, 1, 0, -4, 9]
print(f"Input array goes as follows {input_arr}")
print(f"Sorted array {selectionSort(input_arr)}")


input_arr = [2, 1]
print(f"\n\n Input array goes as follows {input_arr}")
print(f"Sorted array {selectionSort(input_arr)}")