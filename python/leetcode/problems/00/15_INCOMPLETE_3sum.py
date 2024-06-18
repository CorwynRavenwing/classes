class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        answers = []
        nums.sort()
        (neg, zero, pos) = (None, None, None)

        for i, A in enumerate(nums):
            # print(f'{i=} {A=}')
            # should use binary sort here instead
            if neg is None:
                if A < 0:
                    continue
                neg = nums[:i]
                print(f'loop: set {neg[:10]=}')
            if zero is None:
                if A == 0:
                    continue
                zero = nums[len(neg):i]
                print(f'loop: set {zero[:10]=}')
            break
        if neg is None:
            neg = nums[:]
            print(f'after: set {neg[:10]=}')
        if zero is None:
            zero = nums[len(neg):]
            print(f'after: set {zero[:10]=}')
        if pos is None:
            pos = nums[len(neg)+len(zero):]
            print(f'after: set {pos[:10]=}')

        neg = list(reversed(neg))
        print(f'reverse: {neg[:10]=}')

        max_pos = pos[-1] if pos else 0
        print(f'{max_pos=}')

        # case 0: three zeros together
        if len(zero) >= 3:
            answers.append(
                (0, 0, 0)
            )
        
        # case 1. zero, neg == pos
        for A in neg:
            # print(f'{A}')
            if not zero:
                print(f'FAIL CASE 1: no zeros')
                break

            if -A > max_pos:
                print(f'FAIL CASE 1: {-A} > {max_pos}')
                break

            if -A in pos:
                answers.append(
                    (A, 0, -A)
                )

        # print("die after case 1")
        # return answers

        # case 2. neg * 2, pos
        for i, A in enumerate(neg):
            # print(f'{A}')
            if not pos:
                print(f'FAIL CASE 2: no positives')
                break

            if -A > max_pos:
                print(f'FAIL CASE 2: {-A} > {max_pos}')
                break

            for j in range(i+1, len(neg)):
                B = neg[j]
                # print(f'{A} {B}')
                C = -(A + B)
                if C > max_pos:
                    print(f'FAIL CASE 2: -({A} + {B}) ({-(A+B)}) > {max_pos}')
                    break

                if C in pos:
                    # print(f'{i} {j} {k}: {A+B+C}')
                    answers.append(
                        (A, B, C)
                        # tuple(sorted([A, B, C]))
                    )

        # print("die after case 2")
        # return answers

        # case 3. neg, pos * 2
        for A in neg:
            # print(f'{A}')
            if not pos:
                print(f'FAIL CASE 3: no positives')
                break

            if -A > 2 * max_pos:
                print(f'FAIL CASE 3: {-A} > 2 * {max_pos}')
                break
                
            for j, B in enumerate(pos):
                # print(f'{A} {B}')
                C = -(A + B)
                if C < B:
                    print(f'FAIL CASE 3: -A < 2B: {-A} < {2 * B}')
                    # all later B will fail for this A
                    break
                if C in pos[j+1:]:
                    # print(f'{i} {j} {k}: {A+B+C}')
                    answers.append(
                        (A, B, C)
                        # tuple(sorted([A, B, C]))
                    )

            # return [[00000]]
            
        # print(f'dups: {answers=}')
        answers = list(set(answers))
        # print(f'uniq: {answers=}')
        return answers

# TODO: this is still timing out for large data-sets
# timeout happens during case 2

