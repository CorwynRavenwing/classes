class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        lastIndex = {}
        for index, C in enumerate(word):
            # always overwrite existing answer with later answers
            lastIndex[C] = index
        # for index, C in reversed(tuple(enumerate(word))):
        #     # in reverse order
        #     if C in lastIndex:
        #         # don't update if we've seen it already
        #         continue
        #     lastIndex[C] = index

        # we borrow some code from #3120
        
        counts = Counter(word)
        # print(f'{counts=}')

        answer = 0
        for C, count in counts.items():
            if not C.islower():
                continue

            U = C.upper()
            N = counts[U]
            print(f'{C=} {U=} {N=}')
            if not N:
                continue

            # print(f'  delete {count-1} "{C}"s')
            # word = word.replace(C, "_", count - 1)
            # # print(f'    {word=}')
            # indexC = word.index(C)
            indexC = lastIndex[C]
            indexU = word.index(U)

            if indexC < indexU:
                print(f'    OK: {indexC} < {indexU}')
                answer += 1
            else:
                print(f'    bad: {indexC} > {indexU}')

        return answer

# NOTE: Accepted on first Submit

# NOTE: Commented-out brute-force version that overwrites the string
# NOTE: Runtime 165ms Beats91.39%
# NOTE: Memory 18.93MB Beats33.02%

# NOTE: New, cleaner version that looks up each character's index
# NOTE: Runtime 243 ms Beats 69.77%
# NOTE: Memory 18.81 MB Beats 49.53%
# NOTE: interesting, this version is *far* worse!

# NOTE: look up each character's index in reverse order
# NOTE: Runtime 483 ms Beats 20.23%
# NOTE: Memory 40.28 MB Beats 5.12%
# NOTE: ... and this is *ridiculously* worse!

# NOTE: The lesson here is: Premature Optimization Considered Harmful
