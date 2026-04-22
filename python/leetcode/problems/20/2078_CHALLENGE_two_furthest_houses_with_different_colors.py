class Solution:
    def maxDistance(self, colors: List[int]) -> int:

        print(f'{colors=}')
        D = {}
        for i, color in enumerate(colors):
            D.setdefault(color, [])
            D[color].append(i)
        print(f'{D=}')

        distances = [
            (abs(Alist[-1] - Blist[0]), (Alist[-1], Blist[0]), (A, B))
            for A, Alist in D.items()
            for B, Blist in D.items()
            if A != B
        ]
        print(f'{distances=}')
        answer = max(distances)
        print(f'{answer=}')
        return answer[0]

# NOTE: Acceptance Rate 66.8% (easy)

# NOTE: re-ran for challenge:
# NOTE: Runtime 3 ms Beats 38.96%
# NOTE: Memory 20.42 MB Beats 6.45%
