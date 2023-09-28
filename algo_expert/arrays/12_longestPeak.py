



def longestPeak(array) -> int:
    
    longest_peak = 0
    idx = 1

    while idx < len(array) - 1:
        is_peak = array[idx] > array[idx-1] and array[idx] > array[idx+1]

        if not is_peak:
            idx += 1
            continue

        left_idx = idx - 2
        while left_idx >= 0 and array[left_idx+1] > array[left_idx]:
            left_idx -= 1

        right_idx = idx + 2
        while right_idx < len(array) and array[right_idx-1] > array[right_idx]:
            right_idx += 1

        current_peak_len = right_idx - left_idx -1

        longest_peak = max(longest_peak, current_peak_len)
        idx = right_idx
    
    return longest_peak
        

arr  = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
res = longestPeak(arr)

print(f"longestPeak {res}")