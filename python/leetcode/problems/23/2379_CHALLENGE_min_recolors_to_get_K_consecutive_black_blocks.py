class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        answers = []
        L = 0
        R = k
        frag = blocks[L:R]
        counts = Counter(frag)
        white_blocks = counts['W']
        while L < R <= len(blocks):
            print(f'[{L}:{R}] {white_blocks}')
            answers.append(white_blocks)
            if blocks[L] == 'W':
                white_blocks -= 1
            L += 1
            try:
                if blocks[R] == 'W':
                    white_blocks += 1
            except IndexError:
                print(f'Overrun')
                break
            R += 1

        print(f'{answers=}')

        return min(answers)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.84 MB Beats 38.61%
