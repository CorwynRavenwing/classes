class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # we borrow some code from #954:
        counts = Counter(changed)
        # print(f'{counts=}')
        values = sorted(
            counts,
            key=lambda x: abs(x)   # sort by magnitude
        )
        answer = []
        while values:
            A = values.pop(0)
            numberA = counts[A]
            if numberA == 0:
                print(f'No {A} left')
                continue
            if A == 0:
                # zero is the only number that can be both A and 2A at once
                # ascribe half the values to "A" and half to "2A"
                numberA //= 2
            counts[A] -= numberA
            # print(f'->{counts=}')
            twiceA = 2 * A
            if twiceA in counts:
                number2A = counts[twiceA]
                if number2A < numberA:
                    print(f'error: not enough {twiceA}({number2A}) for {A}({numberA})')
                    return []
                print(f'found {A} {twiceA} * {numberA}')
                counts[twiceA] -= numberA
                # print(f'->{counts=}')
                if counts[A] != 0:
                    print(f'error: not enough {twiceA}({number2A}) for {A}({numberA}) [0]')
                    return []
                answer.extend(
                    [A] * numberA
                )
            else:
                print(f'error: {A} has no double')
                return []
        return answer

