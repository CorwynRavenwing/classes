class Solution:
    def reorganizeString(self, s: str) -> str:
        
        counts = Counter(s)
        prev = '*'  # guaranteed not to match
        answer = []
        while counts:
            found = False
            for (letter, count) in counts.most_common(2):
                print(f'{letter=} {count=}')
                if prev == letter:
                    print(f'  (skip)')
                    continue

                prev = letter
                answer.append(letter)
                found = True
                counts[letter] -= 1
                if not counts[letter]:
                    del counts[letter]
                break

            if not found:
                print(f'Impossible!')
                return ''

        return ''.join(answer)

# NOTE: Accepted on first Submit
# NOTE: Runtime 54 ms Beats 5.29%
# NOTE: Memory 16.68 MB Beats 33.77%
