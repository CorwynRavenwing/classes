class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        mod = 10 ** 9 + 7

        def power_mod(base: int, power: int) -> int:
            # print(f'power_mod({base},{power}):')
            if power > 10:
                # A^((B*C) + D) == A^(B*C) * A^D == (A^B)^C * A^D
                A = base
                B = 10
                C = power // 10
                D = power % 10
                # print(f'  {A=} {B=} {C=} {D=}')
                AtoB = power_mod(A, B)
                AtoBC = power_mod(AtoB, C)
                AtoD = power_mod(A, D)
                answer = AtoBC * AtoD
                # print(f'  A^B={AtoB}, ^C={AtoBC}, A^D={AtoD}')
                return answer % mod
            else:
                # print(f'  simple')
                return (base ** power) % mod

        indexesByValue = {}
        for index, value in enumerate(nums):
            indexesByValue.setdefault(value, [])
            indexesByValue[value].append(index)
        # print(f'{indexesByValue=}')

        # print(f'{k}: [-]-=>- {nums}')

        while k:
            if multiplier == 1:
                break
            keys = indexesByValue.keys()
            X = min(keys)
            Y = max(keys)
            new_X = X * multiplier

            last_loop = False

            if (new_X > Y):
                print(f'  X>Y')
                last_loop = True
                kDiv, kMod = divmod(k, len(nums))
                if kMod == 0:
                    print(f'  YES {k=} {kDiv=} {kMod=}')
                    # nums[index] = X     # undo work from prior section
                    mult_pow_k = power_mod(multiplier, kDiv)    # mod is a global
                    nums = [
                        N * mult_pow_k
                        for N in nums
                    ]
                    break   # exit the "while K" loop
            
            batch_size = len(indexesByValue[X])

            if last_loop or batch_size == 1 or batch_size > k:
                # one at a time
                print(f'  {k=}: one ({batch_size} > k)')
                index = indexesByValue[X].pop(0)    # consume first such index
                if not indexesByValue[X]:
                    del indexesByValue[X]   # no empty lists
                k -= 1
                indexesByValue.setdefault(new_X, [])
                bisect.insort(indexesByValue[new_X], index)

                nums[index] = new_X
            else:
                # do a batch of indexes together
                print(f'  {k=}: BATCH of {batch_size} (< k)')
                indexList = indexesByValue[X]
                del indexesByValue[X]   # no empty lists
                k -= len(indexList)
                indexesByValue.setdefault(new_X, [])
                if len(indexesByValue[new_X]) == 0:
                    indexesByValue[new_X] = indexList
                else:
                    indexesByValue[new_X].extend(indexList)
                    indexesByValue[new_X].sort()

                for index in indexList:
                    nums[index] = new_X
                
            # print(f'{k}: [{index}]{X}=>{new_X} {nums}')
            # print(f'{k}: [{index}]')

        nums = [N % mod for N in nums]
        return nums

# NOTE: Acceptance Rate 10.8% (HARD)
# NOTE: still not working for large inputs.
# NOTE: testcase 670, "100000000" + 999 * "1"
# NOTE: needs to grab only part of a batch, to land on k % len == 0.
