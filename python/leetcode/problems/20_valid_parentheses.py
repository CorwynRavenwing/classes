class Solution:
    def isValid(self, s: str) -> bool:

        states = {
            '(': 'p',
            '{': 'p',
            '[': 'p',
            ')': '(',
            '}': '{',
            ']': '[',
        }

        stack = []
        for c in s:
            # print(f"{stack=}")
            state = states[c]
            # print(f"{c=} {state=}")
            if state == 'p':
                stack.append(c)
            else:
                if not stack:
                    print(f"FAIL stack empty")
                    return False
                matching = stack.pop()
                if matching != state:
                    print(f"FAIL '{state}' != '{matching}'")
                    return False
        # print(f"{stack=}")
        if stack:
            print(f"FAIL {stack} != []")
            return False
        return True

