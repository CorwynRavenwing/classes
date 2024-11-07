class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:

        # sort and make hashable
        stones = tuple(sorted(stones))

        def first_hole(stones: List[int]) -> int:
            stoneSet = set(stones)
            for i in range(stones[0], stones[-1]):
                if i not in stoneSet:
                    return i
            return None

        def last_hole(stones: List[int]) -> int:
            stoneSet = set(stones)
            for i in reversed(range(stones[0], stones[-1])):
                if i not in stoneSet:
                    return i
            return None

        def all_stones_by_group(stones: List[int]) -> List[List[int]]:
            # returns e.g. ((3, 5), (7, 7)) to mean there are stones at 3, 4, 5, and 7
            computed = [
                (A, A, (B - A)==1)
                for (A, B) in pairwise(stones + (0,))
            ]
            for i in range(1, len(computed)):
                (Aprev, Bprev, Qprev) = computed[i - 1]
                (Athis, Bthis, Qthis) = computed[i]
                if Qprev:
                    computed[i - 1] = None
                    computed[i] = (Aprev, Bthis, Qthis)
            while None in computed:
                computed.remove(None)
            clean = tuple([
                (A, B)
                for (A, B, Q) in computed
            ])
            return clean
        
        # print(f'TEST: {all_stones_by_group(stones)=}')

        def all_holes_by_group(stones: List[int]) -> List[List[int]]:
            # returns e.g. ((3, 5), (7, 7)) to mean there are stones at 2, 6 and 8
            answer = tuple([
                (A + 1, B - 1)
                for (A, B) in pairwise(stones)
            ])
            answer = tuple(
                (A, B)
                for (A, B) in answer
                if A <= B
            )
            return answer
        
        def four_holes_from_hole_group(group: Tuple[int,int]) -> Set[int]:
            (A, B) = group
            return {
                X
                for X in (A, A+1, B-1, B)
                if A <= X <= B
            }

        def four_holes_per_group(stones: List[int]) -> Set[int]:
            # For example, given stones at positions 12 and 25, and
            # therefore holes at 13 through 24, returns {13, 14, 23, 24}
            # (the first two and last two).  More groups of holes
            # implies more groups of four.  Groups with fewer than 4 holes
            # will return all the holes, even though that's fewer than 4 answers.
            # print(f'DEBUG: 4HPG({stones})')
            answer = set()
            if consecutive(stones):
                return answer
            all_holes_list = all_holes_by_group(stones)
            for group in all_holes_list:
                answer |= four_holes_from_hole_group(group)
            return answer

        def four_holes_sorted(group: Tuple[int,int]) -> List[int]:
            return tuple(sorted(
                four_holes_from_hole_group(
                    group
                )
            ))
            
        def first_four_holes(stones: List[int]) -> Set[int]:
            all_hole_groups = all_holes_by_group(stones)
            group = all_hole_groups[0]
            return four_holes_sorted(group)
        
        def last_four_holes(stones: List[int]) -> Set[int]:
            all_hole_groups = all_holes_by_group(stones)
            group = all_hole_groups[-1]
            return four_holes_sorted(group)
        
        def hole_count(stones: List[int]) -> int:
            length = len(stones)
            span = stones[-1] - stones[0]
            return (span + 1) - length
            
        def consecutive(stones: List[int]) -> bool:
            return hole_count(stones) == 0
        
        MIN_FAIL = float('+inf')
        
        def minMoves(stones: List[int]) -> int:
            if consecutive(stones):
                return 0
            
            stones_count = len(stones)
            stones_span = stones[-1] - stones[0]

            seen = set()
            queue = [(0, stones_span, stones)]
            while queue:
                if len(queue) > 100:
                    print(f'Overflow')
                    break
                (moves_so_far, stones_span, stones) = queue.pop(0)
                if len(stones) <= 4:
                    print(f'MM {moves_so_far},{stones_span}: {stones}')
                else:
                    print(f'MM {moves_so_far},{stones_span}: {stones[:2]}..{stones[-2:]}')
                print(f'  ({len(queue)=})')
                if stones in seen:
                    print(f'  (seen)')
                    continue
                else:
                    seen.add(stones)

                all_stone_groups = all_stones_by_group(stones)
                all_hole_groups = all_holes_by_group(stones)

                assert len(all_hole_groups) + 1 == len(all_stone_groups)

                if len(all_stone_groups) == 2:
                    # two groups of stones: either (ABC, Z), (A, XYZ), or (ABC, XYZ)
                    (group_A, group_B) = all_stone_groups
                    (start_A, end_A) = group_A
                    (start_B, end_B) = group_B
                    length_A = (end_A - start_A + 1)
                    length_B = (end_B - start_B + 1)
                    gap_AB = (start_B - end_A - 1)
                    min_length = min(length_A, length_B)
                    if (length_B == 1):
                        # move first of first group to after other end with gap of 1
                        # move singleton into that gap
                        # ABC,Z -> BC,E,Z -> BCDE
                        tester = list(stones)
                        first = tester.pop(0)
                        last = tester.pop(-1)
                        new_last = tester[-1]
                        tester = tester + [new_last + 1, new_last + 2]
                        tester_span = tester[-1] - tester[0]
                        newQ = (moves_so_far + 2, tester_span, tuple(tester))
                        print(f'DEBUG: {newQ=}')
                        bisect.insort(queue, newQ)
                        continue
                    if (length_A == 1):
                        # move last of last group to before other end with gap of 1
                        # move singleton into that gap
                        # A,XYZ -> A,V,XY -> VWXY
                        tester = list(stones)
                        first = tester.pop(0)
                        last = tester.pop(-1)
                        new_first = tester[0]
                        tester = [new_first - 2, new_first - 1] + tester
                        tester_span = tester[-1] - tester[0]
                        newQ = (moves_so_far + 2, tester_span, tuple(tester))
                        print(f'DEBUG: {newQ=}')
                        bisect.insort(queue, newQ)
                        continue
                    if min_length < gap_AB:
                        # ABC,YZ -> ABCDE
                        index_second_group = tester.index(start_B)
                        tester = list(stones[:index_second_group])
                        tester += list(range(end_A + 1, end_A + length_B))
                        print(f'DEBUG: {tester=}')
                        assert len(stones) == len(tester)
                        tester_span = tester[-1] - tester[0]
                        newQ = (moves_so_far + min_length, tester_span, tuple(tester))
                        print(f'DEBUG: {newQ=}')
                        bisect.insort(queue, newQ)
                        continue
                    else:
                        # ABCD,GHIJ -> ABCDEFGH
                        index_second_group = tester.index(start_B)
                        tester = list(stones[:index_second_group])
                        tester += list(range(end_A + 1, end_A + gap_AB))
                        tester += list(stones[index_second_group:index_second_group + length_B - gap_AB])
                        print(f'DEBUG: {tester=}')
                        assert len(stones) == len(tester)
                        tester_span = tester[-1] - tester[0]
                        newQ = (moves_so_far + gap_AB, tester_span, tuple(tester))
                        print(f'DEBUG: {newQ=}')
                        bisect.insort(queue, newQ)
                        continue
                
                for i in range(1, len(all_stone_groups)):
                    group_A = all_stone_groups[i - 1]
                    group_B = all_stone_groups[i]
                    hole_group_AB = all_hole_groups[i - 1]
                    (start_A, end_A) = group_A
                    (start_B, end_B) = group_B
                    (start_hole_AB, end_hole_AB) = hole_group_AB
                    length_A = (end_A - start_A + 1)
                    length_B = (end_B - start_B + 1)
                    gap_AB = (end_hole_AB - start_hole_AB + 1)
                    stones_AB = length_A + length_B
                    outside_AB = stones_count - stones_AB
                    print(f'{i=} {stones_AB=} {gap_AB=} {stones_count=} {outside_AB=}')
                    index_start_A = stones.index(start_A)
                    index_end_A = stones.index(end_A)
                    index_start_B = stones.index(start_B)
                    index_end_B = stones.index(end_B)
                    before_A = list(stones[:index_start_A])
                    A = list(stones[index_start_A:index_end_A + 1])
                    assert index_end_A + 1 == index_start_B
                    B = list(stones[index_start_B:index_end_B + 1])
                    after_B = list(stones[index_end_B + 1:])
                    # print(f'Checking assertion:')
                    # print(f'{stones=}')
                    # print(f'{before_A=} + {A=} + {B=} + {after_B=}')
                    assert list(stones) == before_A + A + B + after_B
                    count_before_A = len(before_A)
                    count_after_B = len(after_B)

                    stones_filling_gap = list(range(start_hole_AB, start_B))

                    # 1: move stones from before_A to this gap
                    if count_before_A > gap_AB:
                        # 1a: there are stones left over
                        new_before_A = before_A[gap_AB:]
                        tester = new_before_A + A + stones_filling_gap + B + after_B
                        print(f'DEBUG: {tester=}')
                        assert len(stones) == len(tester)
                        tester_span = tester[-1] - tester[0]
                        newQ = (moves_so_far + gap_AB, tester_span, tuple(tester))
                        print(f'DEBUG: {newQ=}')
                        bisect.insort(queue, newQ)
                    elif 0 == count_before_A:
                        # nothing to move from before_A
                        pass
                    elif 0 < count_before_A < gap_AB:
                        # 1b: there are holes left over
                        stones_partially_filling_gap = list(range(start_hole_AB, start_hole_AB + count_before_A))
                        tester = [] + A + stones_partially_filling_gap + B + after_B
                        print(f'DEBUG: {tester=}')
                        # print(f'Checking assertion:')
                        # print(f'{stones=}')
                        # print(f'{[]} + {A=} + {stones_partially_filling_gap=} + {B=} + {after_B=}')
                        assert len(stones) == len(tester)
                        tester_span = tester[-1] - tester[0]
                        newQ = (moves_so_far + count_before_A, tester_span, tuple(tester))
                        print(f'DEBUG: {newQ=}')
                        bisect.insort(queue, newQ)
                    elif count_before_A == gap_AB:
                        # 1c: they are equal
                        tester = [] + A + stones_filling_gap + B + after_B
                        print(f'DEBUG: {tester=}')
                        assert len(stones) == len(tester)
                        tester_span = tester[-1] - tester[0]
                        newQ = (moves_so_far + gap_AB, tester_span, tuple(tester))
                        print(f'DEBUG: {newQ=}')
                        bisect.insort(queue, newQ)
                    else:
                        raise Exception(f'cannot compare {count_before_A=} <=> {gap_AB=}')

                    # 2: move stones from after_B to this gap
                    if count_after_B > gap_AB:
                        # 2a: there are stones left over
                        new_after_B = after_B[:-gap_AB]
                        tester = before_A + A + stones_filling_gap + B + new_after_B
                        print(f'DEBUG: {tester=}')
                        assert len(stones) == len(tester)
                        tester_span = tester[-1] - tester[0]
                        newQ = (moves_so_far + gap_AB, tester_span, tuple(tester))
                        print(f'DEBUG: {newQ=}')
                        bisect.insort(queue, newQ)
                    elif 0 == count_after_B:
                        # nothing to move from after_B
                        pass
                    elif 0 < count_after_B < gap_AB:
                        # 2b: there are holes left over
                        stones_partially_filling_gap = list(range(start_hole_AB, start_hole_AB + count_after_B))
                        tester = before_A + A + stones_partially_filling_gap + B + []
                        print(f'DEBUG: {tester=}')
                        # print(f'Checking assertion:')
                        # print(f'{stones=}')
                        # print(f'{before_A=} + {A=} + {stones_partially_filling_gap=} + {B=} + {[]}')
                        assert len(stones) == len(tester)
                        tester_span = tester[-1] - tester[0]
                        newQ = (moves_so_far + count_after_B, tester_span, tuple(tester))
                        print(f'DEBUG: {newQ=}')
                        bisect.insort(queue, newQ)
                    elif count_after_B == gap_AB:
                        # 2c: they are equal
                        tester = before_A + A + stones_filling_gap + B + []
                        print(f'DEBUG: {tester=}')
                        assert len(stones) == len(tester)
                        tester_span = tester[-1] - tester[0]
                        newQ = (moves_so_far + gap_AB, tester_span, tuple(tester))
                        print(f'DEBUG: {newQ=}')
                        bisect.insort(queue, newQ)
                    else:
                        raise Exception(f'cannot compare {count_after_B=} <=> {gap_AB=}')



                break   # temp



            print(f'ERROR: we should not ever get here.')
            return -99999

        def maxMovingFirst(stones: List[int]) -> int:
            stone_1 = stones[0]
            remainder = stones[1:]
            if consecutive(remainder):
                # no such move
                return 0
            all_hole_groups = all_holes_by_group(stones)
            hole_group_1 = all_hole_groups[0]
            hole_1 = hole_group_1[0]
            group_1_last_stone = hole_1 - 1
            # print(f'DEBUG: {stone_1=} {group_1_last_stone=} {hole_group_1=} {hole_1=}')
            if stone_1 != group_1_last_stone:
                # there is a group of stones at the front
                group_2_stone_1 = hole_group_1[1] + 1
                last_group_begin_index = stones.index(group_2_stone_1)
                old_first_group = stones[:last_group_begin_index]
                old_remainder = stones[last_group_begin_index:]
                print(f'MOVING large group up:')
                # print(f'  INIT: {stones=}')
                print(f'  {old_first_group=}')
                assert consecutive(old_first_group)
                print(f'  {old_remainder=}')
                print(f'  start of second group: {group_2_stone_1}')
                new_first_group_start = group_2_stone_1 - len(old_first_group)
                print(f'  start of new first group: {new_first_group_start}')
                new_first_group = tuple(range(new_first_group_start, group_2_stone_1))
                print(f'  {new_first_group=}')
                moved_by = group_2_stone_1 - hole_1
                print(f'  {moved_by=}')
                tester = new_first_group + old_remainder
                # print(f'  END: {tester=}')
                return moved_by + maxMoves(tester)

            # instead, move stone to the last possible hole
            new_position = last_hole(remainder)
            tester = list(remainder)
            bisect.insort(tester, new_position)
            return 1 + maxMoves(tuple(tester))

        def maxMovingLast(stones: List[int]) -> int:
            stone_N = stones[-1]
            remainder = stones[:-1]
            if consecutive(remainder):
                # no such move
                return 0
            all_hole_groups = all_holes_by_group(stones)
            hole_group_N = all_hole_groups[-1]
            hole_N = hole_group_N[1]
            group_N_first_stone = hole_N + 1
            print(f'DEBUG: {stone_N=} {group_N_first_stone=} {hole_group_N=} {hole_N=}')
            if stone_N != group_N_first_stone:
                # there is a group of stones at the end
                print(f'MOVING large group down:')
                # print(f'  INIT: {stones=}')
                group_penultimate_stone_N = hole_group_N[0] - 1
                print(f'  end of second-last group: {group_penultimate_stone_N}')
                last_group_begin_index = stones.index(group_penultimate_stone_N)
                old_last_group = stones[last_group_begin_index + 1:]
                old_remainder = stones[:last_group_begin_index + 1]
                print(f'  {old_last_group=}')
                assert consecutive(old_last_group)
                print(f'  {old_remainder=}')
                new_last_group_end = group_penultimate_stone_N + len(old_last_group)
                print(f'  end of new first group: {new_last_group_end}')
                new_last_group = tuple(range(group_penultimate_stone_N + 1, new_last_group_end + 1))
                print(f'  {new_last_group=}')
                moved_by = hole_N - group_penultimate_stone_N
                print(f'  {moved_by=}')
                tester = old_remainder + new_last_group
                # print(f'  END: {tester=}')
                return moved_by + maxMoves(tester)

            # instead, move stone to the last possible hole
            new_position = first_hole(remainder)
            tester = list(remainder)
            bisect.insort(tester, new_position)
            return 1 + maxMoves(tuple(tester))
        
        def maxMoves(stones: List[int]) -> int:
            if consecutive(stones):
                return 0
            return max([
                maxMovingFirst(stones),
                maxMovingLast(stones),
            ])
        
        return [minMoves(stones), maxMoves(stones)]

# NOTE: Memory Limit Exceeded for large inputs
