class Solution:

    # we borrow some code from question #15:

    def cleanTupleSet(self, tupleSet: Set[List[int]]) -> FrozenSet[List[int]]:
        debug = False
        if not tupleSet:
            # short-circuit calls with no data
            return tupleSet
        if debug:
            print(f'CTS({tupleSet})')
        return frozenset({
            tuple(sorted(T))
            for T in tupleSet
        })

    def associateTuples(self, newTuple: List[int], tupleSet: Set[List[int]]) -> FrozenSet[List[int]]:
        debug = False
        if not tupleSet:
            # short-circuit calls with no data
            return tupleSet

        if debug:
            print(f'AT({newTuple},{tupleSet}):')
        answer = self.cleanTupleSet(
            {
                newTuple + T
                for T in tupleSet
            }
        )
        if debug:
            print(f'  -> {answer}')
        return answer

    def twoSum(self, nums: Set[int], target: int) -> Set[Tuple[int,int]]:
        # original version returned *first* pair of *indexes*
        # this version returns *all* pairs of *numbers*
        debug = False
        answers = set()
        for value in nums:
            if debug:
                print(f"    [2] {value=}")
            remainder = target - value
            if debug:
                print(f"    [2]   {remainder=}")
            if remainder == value:
                if debug:
                    print(f'    [2]     dup')
                continue
            if remainder in nums:
                if debug:
                    print(f'    [2]     yes')
                answers.add((value, remainder))
        return self.cleanTupleSet(answers)

    def twoSumList(self, nums: List[int], target: int) -> Set[Tuple[int,int]]:
        debug = False
        if len(nums) < 2:
            if debug:
                print(f'    [2] twoSumList({nums},{target}): NO')
            return set()
        if debug:
            print(f'    [2] twoSumList({nums[:5]}...,{target})')
        answers = set()
        numCount = Counter(nums)
        numSet = set(numCount.keys())
        for N, count in numCount.items():
            if count >= 2:
                if target == 2 * N:
                    # use 2 copies of N together
                    answers.add(
                        (N, N)
                    )
        answers |= self.twoSum(numSet, target)
        if debug:
            print(f'    [2]   -> {answers=}')
        return self.cleanTupleSet(answers)

    # new version of this function that can have any target, not just 0:
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        print(f'  [3] threeSum({nums[:5]}...,{target=})')

        LINE = lambda : sys._getframe().f_back.f_lineno - 50

        answers = set()
        # print(f'{LINE()=} {answers=}')
        numCount = Counter(nums)
        # print(f'{numCount=}')
        numSet = set(numCount.keys())
        # print(f'{numSet=}')

        if numCount[0] >= 1:
            any_zeros = True
        else:
            any_zeros = False

        Pos = {N: count for (N, count) in numCount.items() if N > 0}
        Neg = {N: count for (N, count) in numCount.items() if N < 0}
        # print(f'{Pos=}')
        # print(f'{Neg=}')

        if target == 0:
            # special code for target of 0

            if numCount[0] >= 3:
                # print(f'Found 3 zeros')
                answers.add((0,0,0))
                # print(f'{LINE()=} {answers=}')

            for (A_dict, B_dict) in [(Neg, Pos), (Pos, Neg)]:
                # print(f'Looping pos/neg')
                A_set = set(A_dict.keys())
                B_set = set(B_dict.keys())
                for A in A_set:
                    # print(f'  {A=}')
                    if any_zeros:
                        if -A in B_set:
                            # print(f'    zero + neg')
                            answers.add((A, -A, 0))
                            # print(f'{LINE()=} {answers=}')
                    if A % 2 == 0:
                        B = -(A // 2)
                        if (B in B_dict) and (B_dict[B] >= 2):
                            # print(f'    {B}, half twice')
                            answers.add((A, B, B))
                            # print(f'{LINE()=} {answers=}')
                    BC_set = self.twoSum(B_set, -A)
                    # if BC_set:
                    #     # print(f'    {len(BC_set)} (B,C)')
                    for (B, C) in BC_set:
                        answers.add((A, B, C))
                        # print(f'{LINE()=} {answers=}')
        else:
            # normal code to target any non-zero number

            numCountItemsFrozen = tuple(numCount.items())
            for i, (N, Ncount) in enumerate(numCountItemsFrozen):
                print(f'  [3] {i=} {N=} {Ncount=}')

                numCountAfterI = numCountItemsFrozen[i + 1:]
                numsAfterI = [
                    N
                    for (N, count) in numCountAfterI
                    for _ in range(count)
                ]

                # one copy of the number:
                T = target - N
                num2 = self.twoSumList(numsAfterI, T)
                print(f'  [3]  {T=} {num2=}')
                answers |= self.associateTuples(
                    (N,), num2
                )
                print(f'  [3] {LINE()=} {answers=}')

                # two copies
                if Ncount >= 2:
                    T = target - 2 * N
                    if (N != T) and (T in numSet):
                        answers.add(
                            (N, N, T)
                        )
                        # print(f'  [3] {LINE()=} {answers=}')
                
                # three copies:
                if Ncount >= 3:
                    if target == 3 * N:
                        answers.add(
                            (N, N, N)
                        )
                        # print(f'  [3] {LINE()=} {answers=}')

        # print(f'Found total of {len(answers)} triplets.')

        return self.cleanTupleSet(answers)

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        # NOTE: the requirement "a, b, c, d are distinct" does NOT mean
        # that repeated numbers are to be ignored.  a, b, c, and d are
        # the *indexes*, not the *values*.  It means if you only have
        # one 3 in the list, you can't use it several times in a quadruplet.
        # On the other hand, the requirements *do* say the produced
        # quadruplets must be unique, so the test case N=[2,2,2,2,2], T=8
        # needs the quadruplet [2,2,2,2] a single time, *NOT* repeated
        # (5 choose 4) times over because of the various possibilities
        # of "which four twos we're using".

        LINE = lambda : sys._getframe().f_back.f_lineno - 50

        nums = tuple(sorted(nums))
        # print(f'[4] {nums=}')
        numCount = Counter(nums)
        # print(f'[4] {numCount=}')
        numSet = set(numCount.keys())
        # print(f'[4] {numSet=}')

        answers = set()
        # print(f'[4] {LINE()=} {answers=}')

        if numCount[0] >= 1:
            any_zeros = True
        else:
            any_zeros = False

        Pos = Counter({N: count for (N, count) in numCount.items() if N > 0})
        Neg = Counter({N: count for (N, count) in numCount.items() if N < 0})
        # print(f'[4] {Pos=}')
        # print(f'[4] {Neg=}')

        # ... or we could have called twoSumList(nums, 0) ...
        def getZeroPairs() -> List[Tuple[int,int]]:
            # returns all pairs that add to zero: (X, -X)
            NEGSET = lambda SetX: {-N for N in SetX}
            NegNumSet = NEGSET(numSet)
            # print(f'{NegNumSet=}')
            PosAndNegSet = numSet & NegNumSet  # set intersect
            if numCount[0] < 2:
                PosAndNegSet -= {0}     # set subtraction
            answers = {(X, -X) for X in PosAndNegSet if X <= 0}
            # it's a set so it's unique, but return a subscriptable tuple
            return tuple(answers)
        
        zeroPairs = getZeroPairs()
        # print(f'{zeroPairs=}')

        if target == 0:
            # special code for targetting zero

            # (0) four zeros, if possible
            if numCount[0] >= 4:
                # print(f'Found 4 zeros ({numCount[0]=})')
                answers.add((0,0,0,0))
                # print(f'[4] {LINE()=} {answers=}')

            # (1) two sets of Zero Pairs
            for i, iP in enumerate(zeroPairs):
                # print(f'[4] {i=} {iP=}')
                (N, negN) = iP

                # if N == negN, they are both == 0;
                # and we've already handled the "there are 4 zeros" case
                if (N != negN) and (numCount[N] >= 2) and (numCount[negN] >= 2):
                    # print(f'[4]   *twice*')
                    answers.add(iP + iP)    # add same tuple twice here
                    # print(f'[4] {LINE()=} {answers=}')

                for j in range(i + 1, len(zeroPairs)):
                    jP = zeroPairs[j]
                    # print(f'[4]   {j=} {jP=}')
                    answers.add(iP + jP)    # yes, we're adding two tuples
                    # print(f'[4] {LINE()=} {answers=}')
            
            posNums = tuple(Pos.elements())
            negNums = tuple(Neg.elements())

            for N in Pos:
                # (2) a single Positive number, plus ...
                if any_zeros:
                    # (2a) .. a zero, and two negative numbers that add up to it
                    neg2 = self.twoSumList(negNums, -N)
                    # print(f'\n***DEBUG***\n[4] {N=} {neg2=}\n{negNums=}\n{Neg=}\n***DEBUG***\n')
                    answers |= self.associateTuples(
                        (N, 0), neg2
                    )
                    # print(f'[4] {LINE()=} {answers=}')
                
                # (2b) ... three negative numbers that add up to it
                neg3 = self.threeSum(negNums, -N)
                answers |= self.associateTuples(
                    (N,), neg3
                )
                # print(f'[4] {LINE()=} {answers=}')

            for N in Neg:
                # (3) a single Negative number, plus ...
                if any_zeros:
                    # (3a) ... a zero, and two positive numbers that add up to it.
                    pos2 = self.twoSumList(posNums, -N)
                    answers |= self.associateTuples(
                        (N, 0), pos2
                    )
                    # print(f'[4] {LINE()=} {answers=}')

                # (3b) ... three positive numbers that add up to it
                pos3 = self.threeSum(posNums, -N)
                answers |= self.associateTuples(
                    (N,), pos3
                )
                # print(f'[4] {LINE()=} {answers=}')

            # (4) two Positive numbers added together,
            #     plus two negative numbers that add up to it.
            for i, iP in enumerate(posNums):
                print(f'[4] {i=} {iP=}')
                if (numCount[iP] >= 2):
                    print(f'[4]   *twice*')
                    N = 2 * iP
                    neg2 = self.twoSumList(negNums, -N)
                    print(f'\n***DEBUG {LINE()=}***\n[4] {N=} {neg2=}\n{negNums=}\n{Neg=}\n***DEBUG***\n')
                    print(f'[4]     {N=}: {neg2=}')
                    answers |= self.associateTuples(
                        (iP, iP), neg2
                    )
                    print(f'[4] {LINE()=} {answers=}')

                for j in range(i + 1, len(posNums)):
                    jP = posNums[j]
                    print(f'[4]   {j=} {jP=}')
                    N = iP + jP
                    neg2 = self.twoSumList(negNums, -N)
                    print(f'\n***DEBUG {LINE()=}***\n[4] {N=} {neg2=}\n{negNums=}\n{Neg=}\n***DEBUG***\n')
                    # print(f'[4]     {N=}: {neg2=}')
                    answers |= self.associateTuples(
                        (iP, jP), neg2
                    )
                    print(f'[4] {LINE()=} {answers=}')
            # because (4) is symmetric (2 pos / 2 neg), we don't need to
            # do an inverted "for every 2 neg find 2 pos" version as well
        else:
            # normal code to target any non-zero number

            numCountItemsFrozen = tuple(numCount.items())
            for i, (N, Ncount) in enumerate(numCountItemsFrozen):
                print(f'[4] {i=} {N=} {Ncount=}')

                numCountAfterI = numCountItemsFrozen[i + 1:]
                numsAfterI = [
                    N
                    for (N, count) in numCountAfterI
                    for _ in range(count)
                ]

                # one copy of the number:
                T = target - N
                num3 = self.threeSum(numsAfterI, T)
                print(f'[4]   {LINE()=} {T=} {num3=}')
                answers |= self.associateTuples(
                    (N,), num3
                )
                print(f'[4] {LINE()=} {answers=}')

                # two copies
                if Ncount >= 2:
                    T = target - 2 * N
                    num2 = self.twoSumList(numsAfterI, T)
                    print(f'[4]   {LINE()=} {T=} {num2=}')
                    answers |= self.associateTuples(
                        (N, N), num2
                    )
                    # print(f'[4] {LINE()=} {answers=}')
                
                # three copies:
                if Ncount >= 3:
                    T = target - 3 * N
                    if (N != T) and (T in numSet):
                        answers.add(
                            (N, N, N, T)
                        )
                        # print(f'[4] {LINE()=} {answers=}')

                # four copies:
                if Ncount >= 4:
                    if target == 4 * N:
                        answers.add(
                            (N, N, N, N)
                        )
                        # print(f'[4] {LINE()=} {answers=}')

        return sorted(
            self.cleanTupleSet(answers)
        )

# NOTE: Runtime 2258 ms Beats 5.01%
# NOTE: Memory 17.96 MB Beats 6.04%
