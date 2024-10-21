class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        @cache
        def DP(s: str, used: Set[int]) -> int:

            DEBUG = False

            if DEBUG: print(f'DP("{s}",{used})')
            if s == '':
                return 0
            answers = []
            for i in range(1, len(s) + 1):
                frag = s[:i]
                rest = s[i:]
                if DEBUG: print(f'  {i}: "{frag}|{rest}"')
                if frag in used:
                    if DEBUG: print(f'    (nope)')
                    continue
                this_answer = 1 + DP(rest, frozenset(used | {frag}))
                if DEBUG: print(f'    -> {this_answer}')
                answers.append(this_answer)

            answer = max(answers,default=0)
            if DEBUG: print(f'  => {answer}: {answers}')
            return answer

        return DP(s, frozenset())

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 766 ms Beats 5.16%
# NOTE: Memory 63.06 MB Beats 5.16%
