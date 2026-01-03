class Solution:
    def numOfWays(self, n: int) -> int:
        
        mod = 10 ** 9 + 7

        colors_2 = [ 'ABA', 'BAB', 'ACA', 'CAC', 'BCB', 'CBC' ]
        colors_3 = [ 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA' ]

        all_possible = colors_2 + colors_3
        print(f'{all_possible=}')

        JOIN = lambda L: ''.join(L)

        matches = lambda A, B: [x for (x, y) in zip(A, B) if (x == y)]
        # print(f'{matches("ABCDE","xBCxE")=}')

        def can_follow(prior: str) -> List[str]:
            answer = [
                row
                for row in all_possible
                if not matches(row, prior)
            ]
            return tuple(sorted(answer))

        all_follows = {
            row: can_follow(row)
            for row in all_possible
        }
        print(f'all_follows:')
        for row, follows in all_follows.items():
            print(f'{row}: {follows}')

        # The initial options for row #1 are six of 2 colors and six of 3 colors.
        # For each two-color option, there are three 2's and two 3's available as the next row:
        # ABA(2) -> BAB(2) BCB(2) CAC(2) BAC(3) CAB(3)
        # For each three-color option, there are two 2's and two 3's available as the next row:
        # ABC(3) -> BAB(2) BCB(2) BCA(3) CAB(3)

        def Answer(index: str) -> Tuple[int,int]:
            if index == 1:
                return (6,6)
            else:
                (A1, B1) = Answer(index - 1)
                A2 = (A1 * 3 + B1 * 2) % mod
                B2 = (A1 * 2 + B1 * 2) % mod
                return (A2, B2)

        (A, B) = Answer(n)

        return (A + B) % mod

# NOTE: Acceptance Rate 66.6% (HARD)

# NOTE: Accepted on third Run (cleaning up logic)
# NOTE: Accepted on first Submit
# NOTE: Runtime 18 ms Beats 43.90%
# NOTE: Memory 17.98 MB Beats 37.20%
