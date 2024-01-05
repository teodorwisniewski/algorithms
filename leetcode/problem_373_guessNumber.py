




# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:

        left, right = 1, n

        while left <= right:

            num = (left+right) // 2
            res = guess(num)
            if res < 0:
                right = num - 1
            elif res > 0:
                left = num + 1
            else:
                return num


        