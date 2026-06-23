class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {")": "(", "}": "{", "]": "["}

        for br in s:
            if br in close_to_open:
                if stack and stack[-1] == close_to_open[br]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(br)

        return False if stack else True
