class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:

        maxHeight = sum(rods) // 2

        # @functools.lru_cache
        def ST(A: int, B: int):
            nonlocal maxHeight
            if A <= B <= maxHeight:
                pair = (A, B)
            elif B < A <= maxHeight:
                pair = (B, A)
            else:
                # print(f'      too tall! ({A},{B}) > {maxHeight}')
                pair = None
            return pair
        
        # @functools.lru_cache
        def add_rod(pair: Tuple[int,int], rod: int) -> Set[Tuple[int,int]]:
            # print(f'    add_rod({pair},{rod}):')
            (A, B) = pair
            add_to_A = ST(A + R, B)
            add_to_B = ST(A, B + R)
            answer = {add_to_A, add_to_B}
            # print(f'      {answer=}')
            while None in answer:
                answer.remove(None)
            return answer

        # @functools.lru_cache
        def add_rod_multiple(pair: Tuple[int,int], rod: int, count: int) -> Set[Tuple[int,int]]:
            # print(f'    add_rod_multiple({pair},{rod},{count}):')
            (A, B) = pair
            answer = set()
            for i in range(count + 1):
                for j in range(count - i + 1):
                    if (i, j) == (0, 0):
                        continue
                    add_to_both = ST(A + R * i, B + R * j)
                    answer.add(add_to_both)
            # print(f'      {answer=}')
            if None in answer:
                answer.remove(None)
            return answer

        height_diffs = {}
        height_diffs[0] = 0
        # HD[Y] == X means there is a pair (X, X+Y)
        # and that this is the largest such pair known.

        rodCount = Counter(rods)
        for (R, count) in sorted(rodCount.items(), reverse=True):
            if count:
                print(f'  {R=} {count=}')
            else:
                print(f'  {R=}')
            if R > maxHeight:
                print(f'    too tall, > {maxHeight}')
                continue
            with_this_rod = set()
            for (Y, X) in height_diffs.items():
                (A, B) = (X, X + Y)
                pair = (A, B)
                if A == B == maxHeight:
                    print(f'SHORT CIRCUIT ANSWER!')
                    return maxHeight
                if count == 1:
                    with_this_rod |= add_rod(pair, R)
                else:
                    with_this_rod |= add_rod_multiple(pair, R, count)
            for (A, B) in with_this_rod:
                (Y, X) = (B - A, A)
                height_diffs.setdefault(Y, 0)
                Z = height_diffs[Y]
                if X > Z:
                    print(f'    HD[{Y}] new max {X}')
                    height_diffs[Y] = X

        best_height = height_diffs[0]
        return best_height
# NOTE: six hard testcases, old version of this program: 1030 ms
# NOTE: same six testcases, this version: 52 ms
# NOTE: == 20x improvement!

# NOTE: Runtime 583 ms; Beats 46.84%
# NOTE: Memory 18.25 MB; Beats 49.37%
