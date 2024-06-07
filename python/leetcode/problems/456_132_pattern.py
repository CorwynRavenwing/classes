class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        mins = []
        maxs = []
        for N in nums:
            # print(f'{mins=}')
            # print(f'{maxs=}')
            # first, check for wins:
            for (A, B) in zip(mins, maxs):
                # print(f'  check {A} {N} {B}')
                if A < N < B:
                    print(f'    YES!')
                    return True
            # possibly add to mins list
            if not mins:
                print(f'found first min {N}')
                mins.append(N)
                continue
            elif N < min(mins):
                if len(maxs) != len(mins):
                    print(f'overwrite newest min with {N}')
                    mins[-1] = N
                    continue
                else:
                    print(f'found new lowest min {N}')
                    mins.append(N)
                    continue
            # possibly add to maxs list
            if len(maxs) < len(mins):
                maxs.append(None)
            updated_min = None
            updated_i_list = []
            for i, Min in enumerate(mins):
                Max = maxs[i]
                if Min < N:
                    if Max is None or Max < N:
                        # print(f'  update max[{i}]: {Min=} {Max=} -> {N}')
                        maxs[i] = N
                        updated_i_list.append(i)
                        updated_min = (
                            min(updated_min, Min)
                            if updated_min is not None
                            else Min
                        )
            if len(updated_i_list) > 1:
                print(f'updated {len(updated_i_list)} maxs: combining')
                for i in updated_i_list:
                    if mins[i] > updated_min:
                        # print(f'  overwrite [{i}] {mins[i]} {maxs[i]}')
                        mins[i] = None
                        maxs[i] = None
                while None in mins:
                    mins.remove(None)
                while None in maxs:
                    maxs.remove(None)
            # else:
            #     print(f'only updated {len(updated_i_list)} maxs')
            if maxs[-1] is None:
                del maxs[-1]

        # print(f'{mins=}')
        # print(f'{maxs=}')
        return False

