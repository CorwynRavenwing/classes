class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        
        assert k > 0
        
        M = len(mat)
        N = len(mat[0])
        mat = tuple(map(tuple, mat))

        k = k % N   # cycling all the way around is irrelevant

        def cycle_left(arr: List[int]) -> List[int]:
            # nonlocal k
            left_half = arr[:k]
            right_half = arr[k:]
            return right_half + left_half
        # print(f'TEST: {cycle_left((1,2,3,4,5))=}')

        # def cycle_right(arr: List[int]) -> List[int]:
        #     # nonlocal k
        #     REV = lambda L: tuple(reversed(L))
        #     return REV(
        #         cycle_left(
        #             REV(arr)
        #         )
        #     )
        # # print(f'TEST: {cycle_right((1,2,3,4,5))=}')

        def check_left(arr: List[int]) -> List[int]:
            # nonlocal k
            return arr == cycle_left(arr)

        # def check_right(arr: List[int]) -> List[int]:
        #     # nonlocal k
        #     return arr == cycle_right(arr)
        
        # checks = [
        #     check_left(arr) == check_right(arr)
        #     for arr in mat
        # ]
        # print(f'{checks=}')
        # assert all(checks)
        # # which proves we don't have to alternate left/right for even/odd!

        answers = [
            check_left(arr)
            for arr in mat
        ]
        print(f'{answers=}')
        return all(answers)

# NOTE: Acceptance Rate 74.2% (easy)

# NOTE: Accepted on third Run (list != tuple, print format typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 19.52 MB Beats 9.89%
