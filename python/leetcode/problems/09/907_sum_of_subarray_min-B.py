class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        mod = 10 ** 9 + 7
        size = len(arr)

        def NiP_to_NextTE_indexed_pairs(NiP: List[Tuple[int,int]]) -> List[Tuple[int,Tuple[int,int]]]:
            if NiP == []:
                return []
            
            # print(f'{NiP=}')
            minElement = min(NiP)
            # print(f'{minElement=}')
            # index = bisect_right(NiP, minElement)
            # NOPE, bisect only works on sorted lists
            index = NiP.index(minElement)
            # print(f'{index=} {len(NiP)=}')

            (first_N, first_index) = NiP[0]
            (last_N, last_index) = NiP[-1]
            (min_N, min_index) = minElement
            # we are ignoring the N's by design
            this_answer = (min_index, (first_index, last_index))
            # print(f'{this_answer=}')
            left_query = NiP[:index]
            right_query = NiP[index+1:]
            # print(f'=> {left_query} [{minElement}] {right_query}')
            left_group = NiP_to_NextTE_indexed_pairs(left_query)
            right_group = NiP_to_NextTE_indexed_pairs(right_query)

            return left_group + [this_answer] + right_group

        # NOTE: new version of this function:
        # keep list of (N, i) in "i" order
        # in loop: pick lowest by N
        # find location of that tuple in the list (bisect left)
        # answer for that "i" is (lowest "i" in list, highest "i")
        # SPLIT LIST into (before "i", after "i") sections
        # process each section SEPARATELY in this same way
        # after loop, recombine answers into an array by "i" value.

        def get_NextTE_pairs() -> List[Tuple[int,int]]:
            nonlocal arr
            num_index_pairs = [
                (N, index)
                for (index, N) in enumerate(arr)
            ]

            IP = NiP_to_NextTE_indexed_pairs(num_index_pairs)
            print(f'{IP=}')

            NTE_dict = {
                index: pair
                for (index, pair) in IP
            }
            print(f'{NTE_dict=}')

            NTE = [
                NTE_dict[i]
                for i in range(len(arr))
            ]
            print(f'{NTE=}')

            return NTE

        NLE_pairs = get_NextTE_pairs()
        print(f'{NLE_pairs=}')

        answers = []
        for i, A in enumerate(arr):
            (L, R) = NLE_pairs[i]
            # print(f'{i=} {A=} {L=} {R=}')
            subarrays_where_i_am_minimum = (
                (i - L + 1) * (R - i + 1)
            )
            print(f'+ {A} * {subarrays_where_i_am_minimum}')
            answers.append(
                (A * subarrays_where_i_am_minimum) % mod
            )
        print(f'{answers=}')
        return sum(answers) % mod

# This version works much better, but has a Memory Limit Exceeded
# for very large inputs
