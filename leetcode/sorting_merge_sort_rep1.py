def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort[:mid]
    right = merge_sort[mid:]

    return merge(left, right)


def merge(lst1, lst2):

    merged_lst = []

    p1 = 0
    p2 = 0
    while p1 < len(lst1) and p2 < len(lst2):

        if lst1[p1] < lst2[p2]:
            merged_lst.append(lst1[p1])
            p1 += 1
        else:
            merged_lst.append(lst2[p2])
            p2 += 1

    if p1 < len(lst1):
        merged_lst.extend(lst1[p1:])

    if p2 < len(lst2):
        merged_lst.extend(lst2[p2:])

    return merged_lst      
        

if __name__ == "__main__":

    ...
