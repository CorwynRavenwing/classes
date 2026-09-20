class Solution:
    def reverseDegree(self, s: str) -> int:
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alpha_pos = lambda C: alphabet.index(C)
        rev_alpha_pos = lambda C: 26 - alpha_pos(C)
        # for C in alphabet:
        #     print(f'{C=} {rev_alpha_pos(C)=}')
        
        answers = [
            (index + 1) * rev_alpha_pos(C)
            for index, C in enumerate(s)
        ]
        print(f'{answers=}')
        
        return sum(answers)

# NOTE: Acceptance Rate 91.6% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 19 ms Beats 5.57%
# NOTE: Memory 19.42 MB Beats 19.13%
