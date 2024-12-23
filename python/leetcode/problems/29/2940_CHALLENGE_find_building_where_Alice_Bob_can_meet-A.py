class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        
        can_move_to = {
            index: set()
            for index in range(len(heights))
        }
        # print(f'{can_move_to=}')

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                if heights[i] < heights[j]:
                    can_move_to[i].add(j)
        # print(f'{can_move_to=}')

        def doQuery(Q: List[int]) -> int:
            DEBUG = (Q == [612, 147])
            print(f'{Q=}')
            if DEBUG: print(f'  DEBUG')
            (a, b) = Q
            if a == b:
                return a
            A = can_move_to[a] | {a}
            if DEBUG: print(f'  {A=}')
            B = can_move_to[b] | {b}
            if DEBUG: print(f'  {B=}')
            C = A & B
            if DEBUG: print(f'  {C=}')
            answer = min(C, default=-1)
            del A, B, C
            return answer

        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Acceptance Rate 40.6% (HARD)
# NOTE: Memory Limit Exceeded for large inputs
