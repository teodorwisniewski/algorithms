


from typing import List


def can_be_read(newspapers_read_times: List[int], num_coworkers: int, upper_read_time_limit: int) -> bool:

    need_coworkers_cnt = 1
    worker_read_time = 0
    for read_time in newspapers_read_times:

        if (worker_read_time+read_time) > upper_read_time_limit:
            need_coworkers_cnt += 1
            worker_read_time = 0
        # worker reads another newspaper
        worker_read_time += read_time

    return need_coworkers_cnt <= num_coworkers


# Time complexity: O(n log m)
# m = sum(newspapers_read_times)
# n = len(newspapers_read_times)
def newspapers_split(newspapers_read_times: List[int], num_coworkers: int) -> int:
    
    low, high = max(newspapers_read_times), sum(newspapers_read_times)
    min_read_time = high
    while low <= high:
        read_time_to_check = (low+high)//2
        if can_be_read(newspapers_read_times, num_coworkers, read_time_to_check):
            min_read_time = read_time_to_check
            high = read_time_to_check - 1
        else:
            low = read_time_to_check + 1
            
    return min_read_time

if __name__ == '__main__':
    newspapers_read_times = [7,2,5,10,8]
    num_coworkers = 2
    res = newspapers_split(newspapers_read_times, num_coworkers)
    print(res)
