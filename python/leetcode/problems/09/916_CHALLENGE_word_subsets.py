class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        # counts1 = [Counter(word) for word in words1]
        counts2 = [Counter(word) for word in words2]
        
        sets2 = [set(counter.keys()) for counter in counts2]
        Set2 = reduce(
            lambda x, y: x | y,
            sets2
        )
        print(f'{Set2=}')
        
        required2 = Counter({
            letter: max([
                counter[letter]
                for counter in counts2
            ])
            for letter in Set2
        })
        print(f'{required2=}')

        answer = [
            word
            for word in words1
            if not (required2 - Counter(word))
        ]

        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 595 ms Beats 79.02%
# NOTE: Memory 29.80 MB Beats 5.36%

# NOTE: re-ran for challenge, and received:
# NOTE: Runtime 588 ms Beats 11.56%
# NOTE: Memory 30.95 MB Beats 5.58%
