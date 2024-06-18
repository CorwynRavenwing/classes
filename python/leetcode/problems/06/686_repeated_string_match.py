class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        fraction = len(b) // len(a)
        print(f'b={len(b)} / a={len(a)} = {fraction}')
        min_answer = fraction
        max_answer = fraction + 2
        for answer in range(min_answer, max_answer + 1):
            attempt = a * answer
            if b in attempt:
                print(f'{answer}: "{b}" is in "{attempt}"')
                return answer
            else:
                print(f'{answer}: "{b}" is NOT in "{attempt}"')
        print(f'impossible')
        return -1

