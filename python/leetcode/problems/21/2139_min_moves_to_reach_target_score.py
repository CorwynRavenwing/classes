class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        print(f'{target=}')
        moves = 0
        while target > 1:
            if not maxDoubles:
                return moves + target - 1
            moves += 1
            if target % 2 == 0:
                # print(f'  {moves=} /2')
                target //= 2
                maxDoubles -= 1
            else:
                # print(f'  {moves=} -1')
                target -= 1
            # print(f'{target=}')
        return moves

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (Output Exceeded, Time Exceeded)
# NOTE: Runtime 3 ms Beats 8.46%
# NOTE: Memory 17.59 MB Beats 99.23%
