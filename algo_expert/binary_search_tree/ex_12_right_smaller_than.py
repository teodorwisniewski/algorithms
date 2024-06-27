


# def rightSmallerThan(array):

#     res = []
#     for i in range(len(array)):
#         smaller_to_right_cnt = 0
#         for j in range(i+1, len(array)):
#             if array[i] > array[j]:
#                 smaller_to_right_cnt += 1
#         res.append(smaller_to_right_cnt)
#     return res

# average O(nlogn)
# worst O(n^2)



def rightSmallerThan(array):
    if not array:
        return []


    right_smaller_arr = [0] * len(array)
    last_idx = len(array) - 1
    bst = SpecialBST(array[-1])
    # start second to last
    for idx in reversed(range(last_idx)):
        bst.insert(array[idx], idx, right_smaller_arr)
    
    return right_smaller_arr


class SpecialBST:

    def __init__(self, val):
        self.val = val
        self.left_subtree_cnt = 0
        self.left = None
        self.right = None

    def insert(self, val, idx: int, right_smaller_arr: list, num_smaller_at_insert_moment=0) -> None:

        # left subtree
        if val < self.val:
            self.left_subtree_cnt += 1
            if self.left is None:
                self.left = SpecialBST(val)
                right_smaller_arr[idx] = num_smaller_at_insert_moment
            else:
                self.left.insert(val, idx, right_smaller_arr, num_smaller_at_insert_moment)
        # right subtree
        else:
            num_smaller_at_insert_moment += self.left_subtree_cnt
            if val > self.val:
                num_smaller_at_insert_moment += 1
            if self.right is None:
                self.right = SpecialBST(val)
                right_smaller_arr[idx] = num_smaller_at_insert_moment
            else:
                self.right.insert(val, idx, right_smaller_arr, num_smaller_at_insert_moment)



if __name__ == "__main__":

    arr  = [8, 5, 11, -1, 3, 4, 2]

    output = rightSmallerThan(arr)
    print(f"rightSmallerThan {output}")
    assert [5, 4, 4, 0, 1, 1, 0] == output