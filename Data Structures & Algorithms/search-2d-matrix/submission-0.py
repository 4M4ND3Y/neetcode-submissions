class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        # 3 x 4 => p = 0 -> 6 -> 12
        00 01 02 03 10 11 12 13 20 21 22 23
        0  1  2  3  4  5  6  7  8  9  10 11

        # 2 x 3 => p = 0 -> 3
        00 01 02 10 11 12
        0  1  2  3  4  5

        # 5 x 2 => p = 0 -> 8 -> 16 -> 24 -> 32
        00 01 10 11 20 21 30 31 40 41
        0  1  2  3  4  5  6  7  8  9

        # 1 x 5 => p = 0
        00 01 02 03 04
        0  1  2  3  4

        # 5 x 1 => p = 0 -> 9 -> 18 -> 27 -> 36
        00 10 20 30 40
        0  1  2  3  4
        """

        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1

        while l <= r:
            mid = (l + r) // 2
            midx = mid // n
            midy = mid % n

            num = matrix[midx][midy]

            if num < target:
                l = mid + 1
            elif num > target:
                r = mid - 1
            else:
                return True

        return False
