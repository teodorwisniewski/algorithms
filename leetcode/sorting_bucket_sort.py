




def bucket_sort(arr):
    if not arr:
        return arr
    
    min_val = min(arr)
    max_val = max(arr)
    nb_buckets = (max_val - min_val) + 1
    buckets = [0] * nb_buckets

    for el in arr:
        mapped_idx = el - min_val
        buckets[mapped_idx] += 1

    arr_idx = 0
    for mapped_idx, occurences in enumerate(buckets):
        bucket_val = mapped_idx + min_val
        for _ in range(occurences):
            arr[arr_idx] = bucket_val
            arr_idx += 1
    return arr
