class Solution:
    def hIndex(self, citations: List[int]) -> int:

        def H(i: int) -> int:
            val = citations[i]
            here_to_end = len(citations) - i
            answer = val - here_to_end
            # print(f'{i=} {here_to_end=} {val=}: {answer=}')
            return answer

        # Aiches = [
        #     H(i)
        #     for i in range(len(citations))
        # ]
        # print(f'{Aiches=}')
        # return -7777

        L = 0
        R = len(citations) - 1
        left = H(L)
        right = H(R)
        print(f'0 [{L},{R}] = ({left},{right}) T={0}')
        while L + 1 < R:
            M = (L + R) // 2
            mid = H(M)
            print(f'B [{L},{M},{R}] = ({left},{mid},{right}) T={0}')
            if mid < 0:
                print('  remove left')
                (L, left) = (M, mid)
                continue
            if mid > 0:
                print('  remove right')
                (R, right) = (M, mid)
                continue
            if mid == 0:
                here_to_end = len(citations) - M
                print(f'  found value {M=} {here_to_end=} {mid=}')
                return here_to_end
        
        print(f'Z [{L},{R}] = ({left},{right}) T={0}')

        if right < 0:
            print(f'no good answers')
            return 0
        if left < 0:
            here_to_end = len(citations) - R
            print(f'found value {R=} {here_to_end=} {right=}')
            return here_to_end
        if left == 0:
            here_to_end = len(citations) - L
            print(f'found value {L=} {here_to_end=} {left=}')
            return here_to_end
        if left > 0:
            here_to_end = len(citations) - L
            print(f'found value {L=} {here_to_end=} {left=}')
            return here_to_end

        return -9999

# 107 ms: Beats 94.98% of users with Python3

