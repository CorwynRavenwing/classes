class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        def binary(N: int) -> List[int]:
            if N == 0:
                return [0]
            answer = []
            while N:
                answer.append(N % 2)
                N = N // 2
            return answer
        
        print(f'{start=} {goal=}')
        S = binary(start)
        G = binary(goal)
        while len(S) < len(G):
            S.append(0)
        while len(G) < len(S):
            G.append(0)
        print(f'{S=}')
        print(f'{G=}')
        Z = tuple(zip(S,G))
        print(f'{Z=}')
        flips = list([
            (A, B)
            for (A, B) in Z
            if A != B
        ])
        print(f'{flips=}')
        return len(flips)

# NOTE: Runtime 32 ms Beats 77.00%
# NOTE: Memory 16.70 MB Beats 26.96%
