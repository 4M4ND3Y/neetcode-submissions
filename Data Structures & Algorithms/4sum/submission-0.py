class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            while j < n:
                l = j + 1
                r = n - 1

                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]

                    if total < target:
                        l += 1
                    elif total > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                j += 1
                while j < n and nums[j] == nums[j - 1]:
                    j += 1

        return res
