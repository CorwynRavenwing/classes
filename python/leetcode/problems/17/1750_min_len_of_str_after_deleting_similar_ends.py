class Solution:
    def minimumLength(self, s: str) -> int:
        
        if len(s) == 1:
            return 1
        else:
            answer = len(s)

        letters_and_counts = [
            (key, len(tuple(values)))
            for key, values in groupby(s)
        ]
        print(f'{letters_and_counts=}')

        while True:
            (firstLetter, firstCount) = letters_and_counts.pop(0)
            if not letters_and_counts:
                if firstCount == 1:
                    return 1
                else:
                    return 0

            (lastLetter, lastCount) = letters_and_counts.pop(-1)
            
            if firstLetter != lastLetter:
                break
            
            answer -= firstCount
            answer -= lastCount

        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (edge case with "1" in center)
# NOTE: Runtime 539 ms Beats 5.05%
# NOTE: Memory 27.74 MB Beats 7.42%
