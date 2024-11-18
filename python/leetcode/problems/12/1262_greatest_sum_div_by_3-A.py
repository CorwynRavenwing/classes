class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        def hashify_NBM(NBM: Dict[int,List[int]]) -> Tuple[int,List[int]]:
            return tuple([
                (
                    mod,
                    tuple(numberList)
                )
                for mod, numberList in NBM.items()
            ])

        def unhashify_NBM_tuple(NBM_tuple: Tuple[int,List[int]]) -> Dict[int,List[int]]:
            return {
                mod: list(numberTuple)
                for mod, numberTuple in NBM_tuple
            }

        def GSD3_three(NBM: Tuple[int,List[int]]) -> int:
            NBM_copy = unhashify_NBM_tuple(NBM)
            # take groups of 3 with mod 1 or 2:
            answer = 0
            for i in [1, 2]:
                if len(NBM_copy[i]) >= 3:
                    answer += sum(NBM_copy[i][-3:])
                    del NBM_copy[i][-3:]
            
            if not answer:
                return 0
            else:
                return answer + GSD3(hashify_NBM(NBM_copy))

        def GSD3_pairs(NBM: Tuple[int,List[int]]) -> int:
            NBM_copy = unhashify_NBM_tuple(NBM)
            # take pairs from mod=1 and mod=2 together:
            answer = 0
            if len(NBM_copy[1]) and len(NBM_copy[2]):
                answer += NBM_copy[1][-1]
                answer += NBM_copy[2][-1]
                del NBM_copy[1][-1]
                del NBM_copy[2][-1]

            if not answer:
                return 0
            else:
                return answer + GSD3(hashify_NBM(NBM_copy))

        @cache
        def GSD3(NBM: Tuple[int,List[int]]) -> int:
            if not NBM:
                return 0
            else:
                return max([
                    GSD3_three(NBM),
                    GSD3_pairs(NBM),
                ])
        
        nums_by_mod3 = {}
        for i in range(3):
            nums_by_mod3[i] = []
        for N in nums:
            i = N % 3
            nums_by_mod3[i].append(N)
        for i in range(3):
            nums_by_mod3[i].sort()
        print(f'initial: {nums_by_mod3=}')

        # take all values with mod 0:
        answer = sum(nums_by_mod3[0])
        del nums_by_mod3[0]

        return answer + GSD3(hashify_NBM(nums_by_mod3))

# NOTE: first version: time limit exceeded for large inputs.
