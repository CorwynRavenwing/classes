class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        # sort and hashable
        stones = tuple(sorted(stones))

        @cache
        def DP(DPstones: List[int]) -> int:

            DEBUG = False

            if len(DPstones) == 0:
                if DEBUG: print(f'DP({DPstones}): {0=}')
                return 0

            if len(DPstones) == 1:
                (A,) = DPstones
                if DEBUG: print(f'DP({DPstones}): {A=}')
                return A
            
            if len(DPstones) == 2:
                (A, B) = DPstones
                if DEBUG: print(f'DP({DPstones}): {abs(A-B)=}')
                return abs(A - B)

            if DEBUG: print(f'DP({DPstones}): ?')
            answer = set()
            for i, A in enumerate(DPstones):
                for j, B in enumerate(DPstones):
                    if i >= j:
                        continue
                    remaining = list(DPstones)
                    remaining.remove(A)
                    remaining.remove(B)
                    C = abs(A - B)
                    if DEBUG: print(f'  {A}x{B} -> {C}')
                    if C:
                        bisect.insort(remaining, C)
                    answer.add(
                        DP(tuple(remaining))
                    )
            if DEBUG: print(f'DP({DPstones}): {answer=}')
            if DEBUG: print(f'DP({DPstones}): {min(answer)=}')
            return min(answer)

        return DP(stones)

# NOTE: Time Limit Exceeded for large inputs
