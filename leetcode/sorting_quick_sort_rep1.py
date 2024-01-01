



# def quick_sort(arr):

#     if len(arr) <= 1:
#         return arr
    
#     pivot = arr[0]

#     left_partition = [
#         el
#         for el in arr
#         if el < pivot
#     ]
#     middle = [
#         el
#         for el in arr
#         if el == pivot
#     ]
#     right_partition = [
#         el
#         for el in arr
#         if el > pivot
#     ]
#     return (
#         quick_sort(left_partition) +
#         middle +
#         quick_sort(right_partition)
#     )


def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left_part, right_part = partition(arr, pivot)

    left_sorted = quick_sort(left_part)
    right_sorted = quick_sort(right_part)

    return (
        left_sorted +
        [pivot] +
        right_sorted
    )


def partition(arr, pivot):

    left_part = []
    right_part = []

    for el in arr:
        if pivot < el:
            left_part.append(el)
        elif pivot > el:
            right_part.append(el)
    return left_part, right_part




if __name__ == "__main__":

    my_list = [4, 6, 1, 7, 3, 2, 5]
    # print(pivot(my_list))
    print(my_list)
    print(quick_sort_concise(my_list))

    # my_list = [2, 3, 4]
    # print(pivot(my_list))
    # print(my_list)

    # my_list = [4, 3, 2]
    # print(pivot(my_list))
    # print(my_list)
