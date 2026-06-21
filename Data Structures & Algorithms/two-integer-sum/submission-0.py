class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}

        for i, num in enumerate(nums):
            data[num] = i

        for i, num in enumerate(nums):
            diff = target - num
            if diff in data and i != data[diff]:
                return [i, data[diff]]
