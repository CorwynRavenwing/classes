class Solution:
    def specialPerm(self, nums: List[int]) -> int:

        mod = 10 ** 9 + 7

        adjacent = {}
        for i in range(len(nums)):
            adjacent.setdefault(i, set())
        for i, A in enumerate(nums):
            for j, B in enumerate(nums):
                if i >= j:
                    continue
                if (A % B == 0) or (B % A == 0):
                    adjacent[i].add(j)
                    adjacent[j].add(i)
        print(f'{adjacent=}')
        for i in range(len(nums)):
            if len(adjacent[i]) == 0:
                print(f'NO. Nothing adjacent to {i=}')
                return 0
        
        # len(nums) <= 14, therefore we can store used-nums-indexes as a bitmask
        @cache
        def tuple_to_bitmask(S: tuple) -> int:
            answer = 0
            for index in range(15):
                if index in S:
                    # print(f'+{index=} ({2 ** index})')
                    answer += (2 ** index)
            return answer

        # @cache    # sets are an unhashable object
        def set_to_bitmask(S: set) -> int:
            # or, could use frozenset() instead
            return tuple_to_bitmask(tuple(S))
        
        @cache
        def bitmask_to_set(Bitmask: int) -> set:
            bits = tuple(
                reversed(
                    f'{Bitmask:b}'
                )
            )
            # print(f'{Bitmask=} {Bitmask:b} {bits}')
            answer = set()
            for index, bit in enumerate(bits):
                if bit == '1':
                    answer.add(index)
            return answer
        
        # print(f'{set_to_bitmask(bitmask_to_set(10000))=}')
        # print(f'{bitmask_to_set(set_to_bitmask({1, 3, 7, 11}))=}')

        @cache
        def permutations_recursive(BitmaskRemaining: int, priorIndex: int) -> int:
            # print(f'permutations_recursive({BitmaskRemaining},{priorIndex})')
            SetRemaining = bitmask_to_set(BitmaskRemaining)
            if priorIndex is None:
                SetAdjacent = set(adjacent.keys())
            else:
                SetAdjacent = adjacent[priorIndex]
            SetAllowed = SetRemaining.intersection(SetAdjacent)
            # print(f'{SetAllowed=}: {SetRemaining} X {SetAdjacent}')
            if not SetRemaining:
                # success!
                return 1
            elif not SetAllowed:
                # no possible next move
                return 0
            return sum([
                permutations_recursive(
                    set_to_bitmask(
                        SetRemaining - {A}
                    ),
                    A
                )
                for A in SetAllowed
            ])

        SetOfEverything = set(range(len(nums)))
        BitmaskOfEverything = set_to_bitmask(SetOfEverything)
        # print(f'{SetOfEverything=} {BitmaskOfEverything=}')
        answer = permutations_recursive(BitmaskOfEverything, None)

        return answer % mod
# NOTE: Runtime 6921 ms Beats 5.60%
# NOTE: Memory 61.18 MB Beats 72.00%
