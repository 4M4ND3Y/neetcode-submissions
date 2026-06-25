class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and a and a < 0 and stack[-1] > 0:
                if stack[-1] < abs(a):
                    stack.pop()
                elif stack[-1] == abs(a):
                    stack.pop()
                    a = None
                else:
                    a = None
            if a:
                stack.append(a)

        return stack
