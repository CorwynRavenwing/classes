class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:

        sequenceLength = 2 * n - 1  # === 2 * (n - 1) + 1
        sequence = (0,) * sequenceLength
        numbers = tuple(reversed(range(1, n + 1)))
        print(f'{sequenceLength=} {sequence=}')
        possible = [(sequence, numbers)]
        while possible:
            possible.sort()
            P = possible.pop(-1)    # largest partial
            print(f'{P=}')
            (S, N) = P
            # if S < sequence:
            #     print(f'  skip: < {sequence}')
            #     continue
            # N is always sorted descending
            if 0 not in S:
                # this sequence is complete
                if sequence < S:
                    sequence = S
                    print(f'  new maximum!')
                continue
            index = S.index(0)
            if sequence[:index] > S[:index]:
                print(f'  skip: {index=}, {sequence[:index]} > {S[:index]}')
                continue
            for num in N:
                if num == 1:
                    print(f'  Try {num} at {index}')
                    newSeq = S[:index] + (num,) + S[index + 1:]
                else:
                    otherIndex = index + num
                    print(f'  Try {num} at {index},{otherIndex}')
                    if otherIndex >= len(sequence):
                        print(f'    OOB')
                        continue
                    otherNum = S[otherIndex]
                    if otherNum != 0:
                        print(f'    Blocked ({otherNum})')
                        continue
                    newSeq = S[:index] + (num,) + S[index + 1:otherIndex] + (num,) + S[otherIndex + 1:]
                print(f'    -> S={newSeq}')
                newNums = tuple([
                    nn
                    for nn in N
                    if nn != num
                ])
                print(f'    -> N={newNums}')
                possible.append(
                    (newSeq, newNums)
                )
        return sequence

