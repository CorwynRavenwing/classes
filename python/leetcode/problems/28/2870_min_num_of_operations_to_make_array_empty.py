class Solution:
    def minOperations(self, nums: List[int]) -> int:

        counts = Counter(nums)
        print(f'{counts=}')

        answer = 0
        while counts:
            for N, count in tuple(counts.items()):
                mod = count % 3
                if mod == 0:
                    D = count // 3
                    if D:
                        print(f'Delete {D} groups of 3 "{N}"')
                        answer += D
                        counts[N] -= 3 * D
                    if not counts[N]:
                        print(f'All out of "{N}"')
                        del counts[N]
                elif mod == 2:
                    D = count // 3
                    if D:
                        print(f'Delete {D} groups of 3 "{N}"')
                        answer += D
                        counts[N] -= 3 * D
                    if counts[N] == 2:
                        D = 1
                        print(f'Delete {D} groups of 2 "{N}"')
                        answer += D
                        counts[N] -= 2 * D
                    if not counts[N]:
                        print(f'All out of "{N}"')
                        del counts[N]
                elif mod == 1:
                    D = (count // 3) - 1
                    if D > 0:
                        print(f'Delete {D} groups of 3 "{N}"')
                        answer += D
                        counts[N] -= 3 * D
                    if counts[N] == 4:
                        D = 2
                        print(f'Delete {D} groups of 2 "{N}"')
                        answer += D
                        counts[N] -= 2 * D
                    if counts[N] == 2:
                        print(f'SHOULD NOT HAPPEN')
                        return -99999
                        D = 1
                        print(f'Delete {D} groups of 2 "{N}"')
                        answer += D
                        counts[N] -= 2 * D
                    if not counts[N]:
                        print(f'All out of "{N}"')
                        del counts[N]
                    if counts[N] == 1:
                        print(f'Exactly {1} "{N}": FAIL')
                        return -1
        
        return answer
# NOTE: Accepted on first Submit
# NOTE: Runtime 660 ms Beats 8.14%
# NOTE: Memory 34.14 MB Beats 5.15%
