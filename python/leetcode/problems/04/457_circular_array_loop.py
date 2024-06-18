class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        seen = set()
        mod = len(nums)

        for i, N in enumerate(nums):
            print(f'{i=} {N=}')
            if i in seen:
                print(f'  seen i')
                continue
            else:
                seen.add(i)
            positive_N = (N > 0)
            (j, M) = (i, N)
            loop_size = 0
            this_loop = []
            this_loop.append(j)
            while True:
                loop_size += 1
                j = (j + M) % mod
                M = nums[j]
                # print(f'  {j=} {M=} [{len(this_loop)}]')
                if i == j:
                    print(f'    LOOP')
                    if len(this_loop) == 1:
                        print(f'      loop size 1')
                        break
                    else:
                        return True
                if j in this_loop:
                    # i != j but we've seen J before this loop
                    print(f'    jumped into a loop')
                    break
                else:
                    this_loop.append(j)
                positive_M = (M > 0)
                if (positive_N != positive_M):
                    print(f'    +/-')
                    # DO NOT mark j as "seen" yet
                    break
                # if j in seen:
                #     print(f'    seen j')
                #     break
                # else:
                #     seen.add(j)

        return False

