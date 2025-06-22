class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:

        def set_of_words_w_one_star(word: str) -> Set[str]:
            STAR = '*'
            answer = set()
            # zero stars
            answer.add(word)
            for i in range(len(word)):
                mutable = list(word)
                # one star
                mutable[i] = STAR
                answer.add(
                    ''.join(mutable)
                )
                for j in range(i + 1, len(word)):
                    mutable = list(word)
                    # two stars
                    mutable[i] = STAR
                    mutable[j] = STAR
                    answer.add(
                        ''.join(mutable)
                    )
            return answer
        
        set_of_reachable_words = set()
        for word in dictionary:
            word_set = set_of_words_w_one_star(word)
            # print(f'DICT {word}: {word_set}')
            set_of_reachable_words |= word_set
        
        # print(f'\n{sorted(set_of_reachable_words)}\n')

        reachable_sets_per_query = {
            query: set_of_words_w_one_star(query)
            for query in queries
        }
        # print(f'{reachable_sets_per_query=}')

        found_words_per_query = {
            query: set_of_reachable_words & reachable_set
            for query, reachable_set in reachable_sets_per_query.items()
        }
        # print(f'{found_words_per_query=}')

        allow_per_query = {
            query: len(found_words) > 0
            for query, found_words in found_words_per_query.items()
        }
        # print(f'{allow_per_query=}')

        answer = [
            query
            for query in queries
            if allow_per_query[query]
        ]
        return answer

# NOTE: Acceptance Rate 61.2% (medium)

# NOTE: Accepted on second Run (logic error)
# NOTE: Accepted on second Submit (edge case: repeated query)
# NOTE: Runtime 6408 ms Beats 5.71%
# NOTE: Memory 252.85 MB Beats 6.43%
