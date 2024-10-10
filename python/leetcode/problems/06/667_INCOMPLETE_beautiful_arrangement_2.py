class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        
        # we don't use any code from #526, because the
        # algorithms needed are too different.

        allNumbers = set(range(1,n+1))
        print(f'{allNumbers=}')

        queue = [
            (
                (),         # the arranged array so far
                set(),      # the |a1-a2| differences found
                allNumbers, # the numbers left to place
            )
        ]
        # print(f'{queue=}')

        while queue:
            # print(f'L={len(queue)}')
            (arraySoFar, differences, numbersLeft) = queue.pop()
            # print(f'  arr={len(arraySoFar)} diff={len(differences)} num={len(numbersLeft)}')
            if not numbersLeft:
                if len(differences) == k:
                    print(f'Success!')
                    return arraySoFar
                else:
                    # print(f'No: complete, but with too few differences')
                    continue
            if not arraySoFar:
                # nothing to compare to: no differences created.
                for N in numbersLeft:
                    newArray = arraySoFar + (N,)
                    newDifferences = differences
                    newNumbersLeft = numbersLeft - {N}
                    queue.append(
                        (
                            newArray,
                            newDifferences,
                            newNumbersLeft,
                        )
                    )
            else:
                # add new value and new difference, if allowed
                Prev = arraySoFar[-1]
                for N in numbersLeft:
                    diff = abs(N - Prev)
                    # print(f'  try {N=}: {diff=}')
                    if diff not in differences:
                        if len(differences) >= k:
                            # we can't use this number here
                            print(f'    No: too many differences')
                            continue
                    newArray = arraySoFar + (N,)
                    newDifferences = differences | {diff}
                    newNumbersLeft = numbersLeft - {N}
                    queue.append(
                        (
                            newArray,
                            newDifferences,
                            newNumbersLeft,
                        )
                    )

        print(f'Failure')
        return (0,0)

# NOTE: Time Limit Exceeded on test case 15: n=92, k=80
