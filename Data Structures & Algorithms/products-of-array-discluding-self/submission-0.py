class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        suff = [1] * n
        res = []

        for i in range(1, n):
            j = n - i - 1
            pref[i] = pref[i - 1] * nums[i - 1]
            suff[j] = suff[j + 1] * nums[j + 1]

        for i in range(n):
            res.append(pref[i] * suff[i])

        return res
