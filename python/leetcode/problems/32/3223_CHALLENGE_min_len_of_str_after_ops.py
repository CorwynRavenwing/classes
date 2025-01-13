class Solution:
    def minimumLength(self, s: str) -> int:
        
        counts = Counter(s)
        print(f'{counts =}')
        answers = {
            letter: (
                count
                if (count <= 2)
                else
                2
                if (count % 2 == 0)
                else
                1
            )
            for letter, count in counts.items()
        }
        print(f'{answers=}')
        return sum(answers.values())

# NOTE: Accepted on second Run (fencepost error)
# NOTE: Accepted on second Submit (edge case)
# NOTE: Runtime 138 ms Beats 56.19%
# NOTE: Memory 18.74 MB Beats 52.38%
