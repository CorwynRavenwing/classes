class Solution:

    @cache
    def mergePartialEquality_oneway(self, tuple1: List[str], tuple2: List[str]) -> Tuple[List[str],List[str]]:
        equal = ''.join([
            'Y' if (A == B) else 'n'
            for (A, B) in zip(tuple1, tuple2)
        ])
        while 'nY' in equal:
            # we only want yesses at the beginning, not yesses after some noes:
            equal = equal.replace('nY', 'nn')

        if 'Y' not in equal:
            return (tuple1, tuple2)
        
        (list1, list2) = tuple(map(list, [tuple1, tuple2]))     # make mutable

        while equal and equal[0] == 'Y':
            equal = equal[1:]
            list1 = list1[1:]
            list2 = list2[1:]

        (tuple1, tuple2) = tuple(map(tuple, [list1, list2]))     # make immutable
        return (tuple1, tuple2)

    @cache
    def mergePartialEquality(self, tuple1: List[str], tuple2: List[str]) -> Tuple[List[str],List[str]]:
        REV = lambda x: tuple(reversed(tuple(x)))

        (tuple1, tuple2) = self.mergePartialEquality_oneway(tuple1, tuple2)
        (tuple1R, tuple2R) = map(REV, [tuple1, tuple2])
        (tuple1R, tuple2R) = self.mergePartialEquality_oneway(tuple1R, tuple2R)
        (tuple1, tuple2) = map(REV, [tuple1R, tuple2R])
        return (tuple1, tuple2)

    def pickCountFromList(self, count: int, indexes: List[int]) -> List[int]:
        # print(f'PCFL({count},{indexes}):')
        queue = set([()])
        # the prior line means:
        # "create a set of the following list of things:
        #   1. an empty tuple
        # (end of list)"
        # print(f'  {queue=} {len(queue)=}')
        answers = set()
        for N in indexes:
            # print(f'  {N=}')
            newQ = set()
            for Q in queue:
                # print(f'    {Q=}')
                A = Q + (N,)
                if len(A) == count:
                    # print(f'      Found {A=}')
                    answers.add(A)
                    continue
                newQ.add(A)
            queue |= newQ
        # print(f'...{answers=}')
        return answers

    def TEST_PCFL(self) -> None:
        print(f'TEST: {self.pickCountFromList(1,[1,2,3,4,5])=}')
        print(f'TEST: {self.pickCountFromList(2,[1,2,3,4,5])=}')
        print(f'TEST: {self.pickCountFromList(3,[1,2,3,4,5])=}')
        print(f'TEST: {self.pickCountFromList(3,[1,2,3])=}')
        return

    def deleteLettersAtIndexes(self, source: List[str], indexes: List[int]) -> List[str]:
        answer = list(source)   # make it mutable
        for I in indexes:
            answer[I] = None
        while None in answer:
            answer.remove(None)
        return tuple(answer)    # make it immutable again

    def TEST_DLAI(self) -> None:
        print(f'TEST: {self.deleteLettersAtIndexes([0,1,2,3,4,5,6],[1])=}')
        print(f'TEST: {self.deleteLettersAtIndexes([0,1,2,3,4,5,6],[1,3,5])=}')
        print(f'TEST: {self.deleteLettersAtIndexes([0,1,2,3,4,5,6],[0,5])=}')
        print(f'TEST: {self.deleteLettersAtIndexes([0,1,2,3,4,5,6],[])=}')
        return

    @cache
    def deleteCountLettersAtIndexes(self, source: List[str], letter: str, count: int, indexes: List[int]) -> List[List[str]]:
        print(f'deleteCountLetters():')
        setsOfCountIndexes = self.pickCountFromList(count, indexes)
        # print(f'  {setsOfCountIndexes=}')
        print(f'  I={"".join(source)}')
        answer = {
            self.deleteLettersAtIndexes(source, indexList)
            for indexList in setsOfCountIndexes
        }
        # JOIN = lambda x: "".join(x)
        # for A in answer:
        #     print(f'  A={JOIN(A)}')
        print(f'  A={len(A)}')
        return answer

    @cache
    def allIndexes(self, source: List[str], letter: str) -> List[int]:
        return tuple([
            index
            for index, L in enumerate(source)
            if L == letter
        ])

    @cache
    def minDistTuple(self, tuple1: List[str], tuple2: List[str]) -> int:
        (origT1, origT2) = (tuple1, tuple2)
        if tuple1 == tuple2:
            return 0
        (tuple1, tuple2) = self.mergePartialEquality(tuple1, tuple2)
        print()
        print(f'({"".join(origT1)})->({"".join(tuple1)})')
        print(f'({"".join(origT2)})->({"".join(tuple2)})')
        print()
        if tuple1 == tuple2:
            return 0
        
        count1 = Counter(tuple1)
        count2 = Counter(tuple2)
        count1Only = Counter()
        for (letter, count) in count1.items():
            if letter not in count2:
                count1Only[letter] += count
        # print(f'{count1Only=}')
        count2Only = Counter()
        for (letter, count) in count2.items():
            if letter not in count1:
                count2Only[letter] += count
        # print(f'{count2Only=}')
        if count1Only or count2Only:
            # remove ALL letters only found in tuple1 or tuple2 AT ONCE:
            del1 = []
            del2 = []
            answer = 0
            for letter, count in count1Only.items():
                answer += count
                del1.append(f'{count} {letter}')
                indexes = self.allIndexes(tuple1, letter)
                tuple1 = self.deleteLettersAtIndexes(tuple1, indexes)
            for letter, count in count2Only.items():
                answer += count
                del2.append(f'{count} {letter}')
                indexes = self.allIndexes(tuple2, letter)
                tuple2 = self.deleteLettersAtIndexes(tuple2, indexes)
            if answer > 1:
                print(f'MASS DELETE {answer}: {", ".join(del1)} / {", ".join(del2)}')
            else:
                print(f'Delete {", ".join(del1)} / {", ".join(del2)}')
            return answer + self.minDistTuple(tuple1, tuple2)

        count1minus2 = count1 - count2
        count2minus1 = count2 - count1
        if count1minus2:
            for (letter, count) in count1minus2.most_common(1):
                indexes = self.allIndexes(tuple1, letter)
                print(f'  {letter=} {count=} {indexes=}')
                # remove every combination of "count" sets of this letter
                newTuple1List = self.deleteCountLettersAtIndexes(
                    tuple1,
                    letter,
                    count,
                    indexes
                )
                answers = [
                    count + self.minDistTuple(
                        newTuple1,
                        tuple2
                    )
                    for newTuple1 in newTuple1List
                ]
                print(f'{answers=}')
                return min(answers)

        elif count2minus1:
            for (letter, count) in count2minus1.most_common(1):
                indexes = self.allIndexes(tuple2, letter)
                print(f'  {letter=} {count=} {indexes=}')
                # remove every combination of "count" sets of this letter
                newTuple2List = self.deleteCountLettersAtIndexes(
                    tuple2,
                    letter,
                    count,
                    indexes
                )
                answers = [
                    count + self.minDistTuple(
                        tuple1,
                        newTuple2
                    )
                    for newTuple2 in newTuple2List
                ]
                print(f'{answers=}')
                return min(answers)
        
        else:
            # print(f'Counts are equal.  Strings are not.')
            for i, T1, T2 in zip(itertools.count(), tuple1, tuple2):
                # print(f'  {i=} {T1=} {T2=}')
                if T1 == T2:
                    # print(f'    (equal)')
                    continue
                else:
                    print(f'  Try {T1=}/{T2=}:')
                return min([
                    1 + self.minDistTuple(
                        tuple1[:i] + tuple1[i + 1:],
                        tuple2
                    ),
                    1 + self.minDistTuple(
                        tuple1,
                        tuple2[:i] + tuple2[i + 1:],
                    ),
                ])

        return -999

    def minDistance(self, word1: str, word2: str) -> int:
        # self.TEST_PCFL()
        # self.TEST_DLAI()

        tuple1 = tuple(word1)
        tuple2 = tuple(word2)
        return self.minDistTuple(tuple1, tuple2)

# NOTE: works for small inputs, times out for large inputs.
