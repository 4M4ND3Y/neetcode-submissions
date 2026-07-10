class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0
        left = 0
        right = n - 1
        left_max = heights[left]
        right_max = heights[right]

        while left < right:
            left_max = max(left_max, heights[left])
            right_max = max(right_max, heights[right])

            width = right - left
            height = min(left_max, right_max)
            area = width * height
            ans = max(ans, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return ans
