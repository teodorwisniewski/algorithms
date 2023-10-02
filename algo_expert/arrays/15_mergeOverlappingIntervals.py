

# TC O(nlongn) SC O(n)
def mergeOverlappingIntervals(intervals):
    
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    merged_intervals = []
    curr_interval = sorted_intervals[0]
    merged_intervals.append(curr_interval)
    for next_interval in sorted_intervals:
        _, end_current = curr_interval
        next_start, next_end = next_interval
        if end_current >= next_start:
            curr_interval[1] = max(end_current, next_end)
        else:
            curr_interval = next_interval
            merged_intervals.append(next_interval)
    
    return merged_intervals


intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
res = mergeOverlappingIntervals(intervals)

print(f"mergeOverlappingIntervals {res}")