


def is_single_element(arr, idx):

    return (
        (idx == 0 or arr[idx] != arr[idx-1]) and
        (idx == len(arr)-1 or arr[idx] != arr[idx+1])
    )


def is_single_to_the_left(arr,idx):
    # we are at the even idx
    if (
        (idx == 0 or arr[idx] == arr[idx-1]) and
        idx % 2 == 0
    ):
        return True


    # we are at the odd idx
    if (
        (idx == (len(arr)-1) or arr[idx] == arr[idx+1]) and
        idx % 2 == 1
    ):
        return True
    
    if (
        (idx == 0 or arr[idx] != arr[idx-1]) and
        (idx == len(arr)-1 or arr[idx] != arr[idx+1])
    ):
        return True
    
    return False



def singleNonDuplicate(nums) -> int:
        l, r = 0, len(nums)-1
        ans = -1
        while l <= r:
            mid = l + (r-l)//2

            if is_single_to_the_left(nums, mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
        

arr = [1,1,2,3,3,4,4,8,8]
res = singleNonDuplicate(arr)
print(res)

print(f"[3,3,7,7,10,11,11] {singleNonDuplicate([3,3,7,7,10,11,11])}")