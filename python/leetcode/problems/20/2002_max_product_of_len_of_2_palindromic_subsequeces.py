class Solution:
    def maxProduct(self, s: str) -> int:

        def find_all_indexes(char: str, s: str) -> List[int]:
            answers = []
            startIndex = 0
            while True:
                try:
                    index = s.index(char, startIndex)
                except ValueError:
                    break
                answers.append(index)
                startIndex = index + 1
            return answers
        
        def truncate_at_last_index(char: str, s: str) -> str:
            indexes = find_all_indexes(char, s)
            last_index = indexes[-1]
            return s[:last_index]

        @cache
        def find_all_palindromes(s: str, largest_only=False) -> Set[str]:
            # print(f'FP({s})')
            if len(s) <= 1:
                return {s, ''}
            first = s[0]
            rest = s[1:]
            answerWithoutFirst = find_all_palindromes(rest, largest_only)
            if first in rest:
                center = truncate_at_last_index(first, rest)
                answerWithFirst = {
                    first + P + first
                    for P in find_all_palindromes(center, largest_only)
                }
            else:
                answerWithFirst = {first}
            all_answers = answerWithFirst | answerWithoutFirst
            if largest_only:
                # print(f'  Pruning {len(all_answers)} answers:')
                max_len = max([len(A) for A in all_answers])
                all_answers_List = [
                    A
                    for A in all_answers
                    if len(A) == max_len
                ]
                # print(f'    -> Found {len(all_answers)} of length {max_len}')
                all_answers = set(all_answers_List[:1])
                # print(f'    -> Trim to just {len(all_answers)}')
            return all_answers
        
        def remove_characters_in_order(chars: str, s: str) -> Set[str]:
            # print(f'RCIO({chars},{s}):')
            answers = set()
            queue = set()
            queue.add(
                ('', s)
            )
            for C in chars:
                # print(f'{C=}')
                newQ = set()
                for (answer, stringToCheck) in queue:
                    # print(f'->("{answer}","{stringToCheck}")')
                    indexes = find_all_indexes(C, stringToCheck)
                    if not indexes:
                        # print(f'  Char "{C}" not found in "{stringToCheck}"')
                        continue
                    for index in indexes:
                        # print(f'  Divide {stringToCheck} at {index=}:')
                        first = stringToCheck[:index]
                        restOfString = stringToCheck[index + 1:]
                        # print(f'    {first=} {restOfString=}')
                        newQ.add(
                            (answer + first, restOfString)
                        )
                        # print(f'      Q={(answer + first, restOfString)}')
                queue = newQ
            for (answer, stringToCheck) in queue:
                answers.add(answer + stringToCheck)
            return answers
        
        answers = []
        paindromes = find_all_palindromes(s, False)
        print(f'Found {len(paindromes)} palindromes:')
        for P in paindromes:
            L1 = len(P)
            print(f'  {L1=}: "{P}"')
            if L1 == 0:
                print(f'    (skip)')
                continue
            tOptions = remove_characters_in_order(P, s)
            print(f'    Found {len(tOptions)} complements:')
            for t in tOptions:
                print(f'    -> "{t}"')
                other_palindromes = find_all_palindromes(t, True)
                print(f'      Found {len(other_palindromes)} palindromes:')
                for Q in other_palindromes:
                    L2 = len(Q)
                    product = L1 * L2
                    print(f'        {L2=}: "{Q}"')
                    print(f'          {product=}')
                    answers.append(product)
        print(f'{answers=}')
        return max(answers)
# NOTE: Runtime 149 ms Beats 98.97%
# NOTE: Memory 18.52 MB Beats 16.92%
