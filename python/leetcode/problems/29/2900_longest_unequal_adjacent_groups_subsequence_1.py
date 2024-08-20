class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        # we borrow some code from #2901, which I did first:

        def allowed(index1: int, index2: int) -> bool:
            return (
                groups[index1] != groups[index2]
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
# NOTE: Runtime 95 ms Beats 6.33%
# NOTE: Memory 16.64 MB Beats 11.07%
