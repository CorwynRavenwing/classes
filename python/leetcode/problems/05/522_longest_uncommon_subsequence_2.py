class Solution:
    def findLUSlength(self, strs: List[str]) -> int:

        cache = {}
        def hasSS(s: str, sub: str) -> bool:
            T = (s, sub)
            if T in cache:
                answer = cache[T]
                # print(f'cache hit {T}: {answer}')
                return answer
            if len(sub) == 0:
                answer = True
            else:
                (firstSub, restSub) = (sub[0], sub[1:])
                if firstSub not in s:
                    # print(f'no, "{firstSub}" not in "{s}"')
                    answer = False
                else:
                    index = s.index(firstSub)
                    (firstStr, restStr) = (s[:index+1], s[index+1:])
                    # print(f'found "{firstSub}" in "{s}" at {index=}')
                    answer = hasSS(restStr, restSub)
            # print(f'cache miss {T}: {answer}')
            cache[T] = answer
            return answer

        # shortcut: since any string is a subsequence of itself,
        # and since if A is a subsequence of B, then any subsequence of A
        # must *also* be a subsequence of B,
        # we check the root level members of "strs" for being SS of any other member.
        # if we find one that isn't a SS of any others: return the maximum such.
        # if we *don't* find one, i.e. each "strs" is a SS of all other "strs":
        # then give up, because we won't find a better answer.

        answers = []
        for i, S in enumerate(strs):
            is_SS = [
                hasSS(other, S)
                for j, other in enumerate(strs)
                if i != j
            ]
            print(f'{i}, {S}, {is_SS}')
            if not any(is_SS):
                print(f'  match')
                answers.append(len(S))
        
        print(f'{answers=}')
        return max(answers) if answers else -1

