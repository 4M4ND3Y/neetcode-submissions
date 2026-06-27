# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            gnum = (left + right) // 2
            res = guess(gnum)
            if res == 0:
                return gnum
            elif res == -1:
                right = gnum - 1
            else:
                left = gnum + 1
