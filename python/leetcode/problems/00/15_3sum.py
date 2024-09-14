class Solution:

    # we borrow some code from question #1:        

    def twoSum(self, nums: Set[int], target: int) -> Set[Tuple[int,int]]:
        # original version returned *first* pair of *indexes*
        # this version returns *all* pairs of *numbers*
        answers = set()
        for value in nums:
            # print(f"{value=}")
            remainder = target - value
            # print(f"  {remainder=}")
            if remainder == value:
                # print(f'    dup')
                continue
            if remainder in nums:
                # print(f'    yes')
                answers.add((value, remainder))
        return answers

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        answers = set()
        counts = Counter(nums)
        # print(f'{counts=}')
        if counts[0] >= 3:
            print(f'Found 3 zeros')
            answers.add((0,0,0))
        if counts[0] >= 1:
            any_zeros = True
        else:
            any_zeros = False
        
        Pos = {N: count for (N, count) in counts.items() if N > 0}
        Neg = {N: count for (N, count) in counts.items() if N < 0}
        # print(f'{Pos=}')
        # print(f'{Neg=}')

        for (A_dict, B_dict) in [(Neg, Pos), (Pos, Neg)]:
            print(f'Looping pos/neg')
            A_set = set(A_dict.keys())
            B_set = set(B_dict.keys())
            for A in A_set:
                print(f'  {A=}')
                if any_zeros:
                    if -A in B_set:
                        print(f'    zero + neg')
                        answers.add((A, -A, 0))
                if A % 2 == 0:
                    B = -(A // 2)
                    if (B in B_dict) and (B_dict[B] >= 2):
                        print(f'    {B}, half twice')
                        answers.add((A, B, B))
                BC_set = self.twoSum(B_set, -A)
                if BC_set:
                    print(f'    {len(BC_set)} (B,C)')
                for (B, C) in BC_set:
                    answers.add((A, B, C))
        
        print(f'Found total of {len(answers)} triplets.')

        answers = {
            tuple(sorted(A))
            for A in answers
        }
        print(f'Cleaned: {len(answers)} triplets.')

        return answers

# NOTE: Runtime 630 ms Beats 81.67%
# NOTE: Memory 26.01 MB Beats 5.45%
