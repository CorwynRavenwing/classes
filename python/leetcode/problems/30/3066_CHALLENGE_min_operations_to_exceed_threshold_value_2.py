class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        # we borrow some code from #3065

        # SHORTCUT: we're removing two numbers at a time, A and B.
        # case 1: A == B.
        #   min(A,B)*2 + max(A,B)
        #   == A*2 + A
        #   == 3A
        # case 2: A != B.
        #   define B = A + d
        #   min(A,B)*2 + max(A,B)
        #   == A*2 + B
        #   == A*2 + A+d
        #   == 3A + d

        counts = Counter(nums)
        # print(f'{counts=}')

        def next_working_groups() -> Tuple[int,int,int]:
            nonlocal counts, k

            def next_working_groups_generate() -> Tuple[int,int,int]:
                nonlocal counts, k
                # working = [
                #     (N, count)
                #     for (N, count) in sorted(counts.most_common())
                #     if count > 0
                # ]
                counts = +counts
                working = list(sorted(counts.most_common()))
                # print(f'{working[:5]=}')
                # i = 0
                firstC = None
                # while i < len(working):
                while working:
                    (A, Acount) = (None, 0)
                    while not Acount:
                        # if A is not None:
                        #     # print(f'  del {A=}')
                        #     del counts[A]
                        if not working:
                            # print(f'End loop: ran out of "working" for A')
                            return
                        (A, Acount) = working.pop(0)
                        # print(f'{A=} {Acount=} {working[:5]=}')
                        # i += 1
                    if A >= k:
                        # print(f'End loop: next element >= {k}')
                        # print(f'  :yield {None}') 
                        yield None
                        return
                    if firstC is not None and A >= firstC:
                        # print(f'End loop.  {A=} >= {firstC=}')
                        # print(f'  ... re-insert {A=} {Acount=}')
                        working.insert(0, (A, Acount))
                        return
                    if Acount > 1:
                        pairs = Acount // 2
                        # C = A * 2 + A     # A,B are equal
                        C = A * 3           # A,B are equal
                        if firstC is None:
                            firstC = C
                        answer = (A, A, C, pairs)
                        # print(f'  :yield {answer}')
                        yield answer
                        if pairs * 2 != Acount:
                            newAcount = Acount - 2 * pairs
                            # print(f'  ... re-insert {A=} {newAcount=}')
                            working.insert(0, (A, newAcount))
                    else:
                        (B, Bcount) = (None, 0)
                        while not Bcount:
                            # if B is not None:
                            #     # print(f'  del {B=}')
                            #     del counts[B]
                            if not working:
                                # print(f'End loop: ran out of "working" for B')
                                return
                            (B, Bcount) = working.pop(0)
                            # print(f'  {B=} {Bcount=} {working[:5]=}')
                            # i += 1
                        if firstC is not None and B >= firstC:
                            # print(f'End loop.  {B=} >= {firstC=}')
                            # print(f'  ... re-insert {B=} {Bcount=}')
                            working.insert(0, (B, Bcount))
                            return
                        C = A * 2 + B       # A,B are min,max respectively
                        if firstC is None:
                            firstC = C
                        answer = (A, B, C, 1)
                        # print(f'  :yield {answer}')
                        yield answer
                        if Bcount > 1:
                            newBcount = Bcount - 1
                            # print(f'  ... re-insert {B=} {newBcount=}')
                            working.insert(0, (B, newBcount))

            answer = tuple(next_working_groups_generate())
            if answer == (None,):
                return None
            else:
                return answer
        
        answer = 0
        while (working_groups := next_working_groups()):
            print(f'Got {len(working_groups)} working groups:')
            for working_group in working_groups:
                # print(f'  {working_group=}')
                if working_group is None:
                    break
                (A, B, C, count) = working_group
                # # C = min(A,B) * 2 + max(A,B)
                # C = A * 2 + B   # A,B are min,max respectively
                counts[A] -= count
                counts[B] -= count
                answer += count
                counts[C] += count
                # print(f'    {count}: -{A} -{B}, +{C}')
                # print(f'    ->{counts=}')

        return answer

# NOTE: Runtime 6135 ms Beats 5.12%
# NOTE: Memory 70.85 MB Beats 10.26%

# NOTE: re-ran for challenge:
# NOTE: Runtime 5620 ms Beats 5.04%
# NOTE: Memory 72.86 MB Beats 12.18%
