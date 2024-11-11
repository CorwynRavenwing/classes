class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        
        answer = []
        A = 0
        B = 0
        for char in seq:
            print(f'{A=} {B=}\n\t{char=}')
            match char:
                case '(':
                    if A <= B:
                        print(f'\t\t+A')
                        answer.append(0)
                        A += 1
                    else:
                        print(f'\t\t+B')
                        answer.append(1)
                        B += 1

                case ')':
                    if A > B:
                        print(f'\t\t-A')
                        answer.append(0)
                        A -= 1
                    else:
                        print(f'\t\t-B')
                        answer.append(1)
                        B -= 1

                case _:
                    raise Exception(f'ERROR: invalid {char=}')
        print(f'{A=} {B=}\n\tend')

        return answer

# NOTE: Accepted on second Run (first was function-name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 23 ms Beats 16.67%
# NOTE: Memory 16.95 MB Beats 79.55%
