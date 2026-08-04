class Solution:
    def smallestPalindrome(self, s: str) -> str:
        
        counts = Counter(s)
        # print(f'{counts=}')

        center = []
        pairs = list(sorted(counts.items()))
        lefthalf = []
        while pairs:
            # print(f'{lefthalf=} {center=} {pairs=}')
            (letter, count) = pairs.pop(0)
            # print(f'  {letter=} {count=}')
            leftcount = count // 2
            # print(f'    A {leftcount=} {count=}')
            lefthalf.append(
                letter * leftcount
            )
            count -= (leftcount * 2)
            # print(f'    B {leftcount=} {count=}')
            if count == 1:
                center.append(letter)
                count -= 1
                # print(f'    C {leftcount=} {count=}')
            if count:
                print(f'  CANNOT GET HERE LOGICALLY')
                # print(f'{lefthalf=} {center=} {pairs=}')
                # print(f'  {count=}')
                raise Exception('DIE #1')

        # print(f'{lefthalf=} {center=} {pairs=}')
        if len(center) > 1:
            print(f'  CANNOT GET HERE EITHER')
            raise Exception('DIE #2')
        
        answer = lefthalf + center + list(reversed(lefthalf))
        return ''.join(answer)

# NOTE: Acceptance Rate 64.6% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 163 ms Beats 86.64%
# NOTE: Memory 20.92 MB Beats 51.15%
