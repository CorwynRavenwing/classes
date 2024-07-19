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
            while None in answer:
                answer.remove(None)
            return answer

        height_pairs = {(0,0)}  # Set[Tuple[int,int]]: each number is a height; A < B
        rodCount = Counter(rods)
        for (R, count) in sorted(rodCount.items(), reverse=True):
            print(f'  {R=} {count=}')
            if R > maxHeight:
                print(f'    too tall, > {maxHeight}')
                continue
            with_this_rod = set()
            for pair in height_pairs:
                (A, B) = pair
                if A == B == maxHeight:
                    print(f'SHORT CIRCUIT ANSWER!')
                    return maxHeight
                if count == 1:
                    with_this_rod |= add_rod(pair, R)
                else:
                    with_this_rod |= add_rod_multiple(pair, R, count)
            height_pairs |= with_this_rod
        # print(f'{height_pairs=}')
        equal_pairs = {
            (A, B)
            for (A, B) in height_pairs
            if A == B
        }
        # print(f'{equal_pairs=}')
        best_pair = max(equal_pairs)
        (best_height, this_will_be_equal) = best_pair

        return best_height
# NOTE: this works in general, but fails for large data.
