class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        strings = list(map(str, nums))
        print(f'{strings=}')
        best = {
            0: ""
        }
        possibles = [
            ("", 0, strings)
        ]
        while possibles:
            # print(f'{possibles=}')
            length = min([
                L
                for (N, L, S) in possibles
            ])
            print(f"{length=}")
            that_length = [
                (N, L, S)
                for (N, L, S) in possibles
                if L == length
            ]
            best.setdefault(length, "")
            for (N, L, S) in that_length:
                best[length] = max(N, best[length])
            for (N, L, S) in that_length:
                possibles.remove((N, L, S))
                if N < best[length]:
                    # print(f'  Trash {N} < {best[length]}')
                    continue
                # print(f'trying {len(S)} ({len(set(S))}) ideas:')
                for str_idea in set(S):
                    # print(f'  Try {str_idea}')
                    S_remaining = S.copy()
                    S_remaining.remove(str_idea)
                    new_N = N + str_idea
                    new_L = L + len(str_idea)

                    while new_N[0] == '0' and len(new_N) > 1:
                        # print(f'  delete leading 0')
                        new_N = new_N[1:]
                        new_L -= 1
                    
                    new_poss = (
                        new_N,
                        new_L,
                        S_remaining,
                    )
                    if new_poss not in possibles:
                        possibles.append(new_poss)
        # print(f'{possibles=}')
        answer = best[length]
        # while answer[0] == '0' and len(answer) > 1:
        #     print(f'  delete leading 0')
        #     answer = answer[1:]
        return answer

# NOTE: Runtime 943 ms Beats 5.31%
# NOTE: Memory 18.73 MB Beats 32.99%
