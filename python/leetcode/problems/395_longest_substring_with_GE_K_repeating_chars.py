class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        # strategy:
        # count the freq of all letters in the entire string.
        # if all letters are freq >= k, return length of string
        # if all letters are freq < k, return zero!
        # if some >=k and some <k:
        # NO correct answer will contain any letter with freq <k!
        # therefore split this string at those positions
        # and return the max, of calling this function on each substrings
        # Memoize these in case we get the same string twice.

        cache = {}
        def recurse(S: str, depth=0) -> int:
            nonlocal k
            margin = "  " * depth
            if S in cache:
                answer = cache[S]
                print(margin + f'"{S}": cache hit {answer}')
                return answer
            
            print(margin + f'"{S}":')
            letterCounts = Counter(S)
            print(margin + f'{letterCounts=}')
            (enough, short) = ([], [])
            for letter, count in letterCounts.items():
                if count >= k:
                    enough.append(letter)
                else:
                    short.append(letter)
            print(margin + f'{enough=}')
            print(margin + f'{short=}')
            if not enough:
                answer = 0
                cache[S] = answer
                print(margin + f'{answer=}')
                return answer
            if not short:
                answer = len(S)
                cache[S] = answer
                print(margin + f'{answer=}')
                return answer
            to_split = S[:]
            for char in short:
                to_split = to_split.replace(char, ' ')
                print(margin + f'  short:{char=}')
            substrings = to_split.split(' ')
            print(margin + f'  {substrings=}')
            answers = [
                recurse(SS, depth + 1)
                for SS in substrings
            ]
            answer = max(answers)
            cache[S] = answer
            print(margin + f'{answer=}')
            return answer

        return recurse(s)

# NOTE: 34 ms; Beats 93.67% of users with Python3
