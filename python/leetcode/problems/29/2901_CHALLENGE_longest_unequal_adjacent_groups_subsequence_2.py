class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        def hamming(s1: str, s2: str) -> int:
            if len(s1) != len(s2):
                return 0
            return sum([
                (0 if (c1 == c2) else 1)
                for c1, c2 in zip(s1, s2)
            ])
        
        def allowed(index1: int, index2: int) -> bool:
            return (
                (
                    groups[index1] != groups[index2]
                ) and (
                    hamming(words[index1], words[index2]) == 1
                )
            )
        
        longest_ss_ending_at = [1] * len(words)         # each could be start of new seq
        longest_ss_prior_index = [None] * len(words)    # ... with no prior value

        for j in range(len(words)):
            print(f'[{j=}]')
            currentI = longest_ss_ending_at[j] + 1
            for i in range(j + 1, len(words)):
                # print(f'  [{i=}]')
                if not allowed(j, i):
                    # print(f'    not allowed')
                    continue
                priorI = longest_ss_ending_at[i]
                if currentI > priorI:
                    # print(f'    New best length {currentI} > {priorI}')
                    longest_ss_ending_at[i] = currentI
                    longest_ss_prior_index[i] = j
        answer_length = max(longest_ss_ending_at)
        print(f'{answer_length=}')
        answer_index = [
            index
            for index, length in enumerate(longest_ss_ending_at)
            if length == answer_length
        ]
        print(f'{answer_index=}')
        K = answer_index[0]
        answer = []
        # print(f'Composing answer:')
        while K is not None:
            # print(f'  {K=} {words[K]}')
            answer.append(words[K])
            K = longest_ss_prior_index[K]

        return reversed(answer)

# NOTE: Accepted first Submit
# NOTE: Runtime 1741 ms Beats 24.19%
# NOTE: Memory 17.07 MB Beats 59.68%

# NOTE: re-ran for challenge:
# NOTE: Accepted on second Run (output type mismatch)
# NOTE: Accepted on first Submit
# NOTE: Runtime 1735 ms Beats 19.32%
# NOTE: Memory 17.96 MB Beats 93.18%
