class Solution:
    def minNonZeroProduct(self, p: int) -> int:

        mod = 10 ** 9 + 7

        def arrayProduct(numberList: List[int]) -> int:
            answer = 1
            for N in numberList:
                answer *= N
            return answer
        
        # print(f'TEST: {arrayProduct([1, 2, 3, 4, 5])=}')
        
        def binary2int(bits: List[int]) -> int:
            answer = 0
            for B in bits:
                answer *= 2
                answer += B
            return answer
        
        def allPossibleNumbersAndRemainingBits(ones: List[int]) -> List[Tuple[int, List[int], List[int]]]:
            possibles = [()]
            for B in ones:
                new_possibles = []
                for P in possibles:
                    new_possibles.append(
                        P + (0,)
                    )
                    if B:
                        new_possibles.append(
                            P + (1,)
                        )
                possibles = new_possibles
            # print(f'{possibles=}')
            answers = []
            for bitsUsed in possibles:
                number = binary2int(bitsUsed)
                bitsRemaining = [
                    A - B
                    for (A, B) in zip(ones, bitsUsed)
                ]
                answers.append(
                    (number, bitsUsed, bitsRemaining)
                )
            return reversed(answers)

        numbersNeeded = (2 ** p) - 1
        onesPerDigit = 2 ** (p - 1)
        digits = p

        print(f'{numbersNeeded=} {onesPerDigit=} {digits=}')

        startingCondition = (
            [onesPerDigit] * digits,    # ones left to distribute
            [],                         # list of numbers created so far: max=numbersNeeded
        )
        # instead, could keep track of "last number created" and "partial product so far"
        # rather than the list of numbers itself

        answers = []
        states = [startingCondition]
        while states:
            # print(f'L={len(states)}')
            (ones, numberList) = states.pop(-1)     # Depth-first search
            # print(f'  {ones=} {numberList=}')
            totalOnes = sum(ones)
            if len(numberList) == numbersNeeded:
                if totalOnes == 0:
                    # print(f'    *** FOUND AN ANSWER ***')
                    product = arrayProduct(numberList)
                    answers.append(
                        (product, numberList)
                    )
                    continue
                else:
                    # print(f'    No room for more numbers!')
                    continue
            if totalOnes == 0:
                # print(f'    Ran out of ones too early!')
                continue
            minAllowedNumber = (numberList[-1] if numberList else 1)
            # print(f'    {minAllowedNumber=}')
            for (number, bitsUsed, remainingBits) in allPossibleNumbersAndRemainingBits(ones):
                # print(f'    {number=} {bitsUsed=} {remainingBits=}')
                if number < minAllowedNumber:
                    # print(f'      Too small')
                    continue
                # print(f'      {number}:{bitsUsed}')
                states.append(
                    (remainingBits, numberList + [number])
                )
        products = []
        print(f'Found {len(answers)} answers:')
        for A in answers:
            print(f'  {A=}')
            (product, numberList) = A
            products.append(product)

        return min(products) % mod
# NOTE: This program is correct, but takes far too long to run.
# Time Limit Exceeded for input "4" :-/
# but it does show us the pattern of the right answer.
# e.g. 3 -> 001 001 001 110 110 110 111 (1 1 1 6 6 6 7)
# e.g. 4 -> 15 * 14^7 * 1^7
# for P=4, M=(2^(P-1))=8, N=(2^P-1)=15, these numbers are:
# 1^(M-1) * (N-1) * (N-2)^(M-1)
