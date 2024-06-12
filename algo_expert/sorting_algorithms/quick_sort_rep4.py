

def swap(lst, idx1, idx2):
    lst[idx1], lst[idx2] = lst[idx2], lst[idx1]


def partition(lst, left, right) -> int:

    swap_idx = left
    pivot_idx = right
    pivot = lst[pivot_idx]
    right -= 1
    while True:

        while lst[left] < pivot:
            left += 1

        while lst[right] > pivot:
            right -= 1

        if left >= right:
            break
        else:
            swap(lst, left, right)
            left += 1

    swap(lst, pivot_idx, left)
    return left


def quick_sort(lst):
    quick_sort_helper(lst, 0, len(lst)-1)


def quick_sort_helper(lst, start, end):
    if start >= end:
        return
    pivot_idx = partition(lst, start, end)
    quick_sort_helper(lst, start, pivot_idx-1)
    quick_sort_helper(lst, pivot_idx+1, end)




if __name__ == "__main__":

    lst = [3, 14 ,5, 2, -4, 10, 1, 4]
    print(f"Before sorting {lst}")
    print(partition(lst, 0, len(lst)-1))
    print(f"After running a partition {lst}")
    quick_sort(lst)
    print(f"After sorting {lst}")