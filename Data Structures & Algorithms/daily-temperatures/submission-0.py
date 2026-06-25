class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # pair: (temperature, index)
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 1, -1, -1):
            temp = temperatures[i]
            while stack and stack[-1][0] <= temp:
                stack.pop()
            if stack and stack[-1][0] > temp:
                res[i] = stack[-1][-1] - i
            stack.append((temp, i))

        return res
