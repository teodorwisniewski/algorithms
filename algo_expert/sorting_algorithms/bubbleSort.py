

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def bubbleSort(array):
    # Write your code here.
    for i in range(1, len(array)):
        is_sorted = True
        for j in range(0, len(array) - i):
            if array[j] > array[j+1]:
                swap(array, j, j+1)
                is_sorted = False
        if is_sorted:
            break
            
    return array


input_arr = [4, 54, 1, 0, -4, 9]
print(f"Input array goes as follows {input_arr}")
print(f"Sorted array {bubbleSort(input_arr)}")


input_arr = [2, 1]
print(f"\n\n Input array goes as follows {input_arr}")
print(f"Sorted array {bubbleSort(input_arr)}")