class Solution:
    def clearStars(self, s: str) -> str:

        if '*' not in s:
            return s
        
        stack = []
        seen = Counter()
        emptySeen = 'zZz'  # guaranteed > any character, even one single 'z'
        minSeen = emptySeen
        for C in s:
            if C != '*':
                # normal character: insert.
                stack.insert(0, C)
                seen[C] += 1
                if minSeen > C:
                    minSeen = C
                # print(f'{C} -> push')
            else:
                # asterisk: pop nearest minimum character
                C = minSeen
                # print(f'(*) -> pop {C}')
                index = stack.index(C)
                check = stack.pop(index)
                if check != C:
                    print(f'  ERROR!  {index=} {check=} {C=}')
                    return -77777
                seen[C] -= 1
                if not seen[C]:
                    print(f'  No more {C} in stack.')
                    del seen[C]
                    minSeen = min(seen, default=emptySeen)
                # print(f'  {stack=}')
        answer = [
            C
            for C in reversed(stack)
        ]
        # print(f'{answer=}')
        return ''.join(answer)

# NOTE: time limit exceeded for large inputs
