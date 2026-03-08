class Solution:
    def minFlips(self, s: str) -> int:
        
        def minOperations(s: str) -> int:
            # print(f'MO({s}):')

            pairs = tuple(enumerate(s))
            # print(f'  {pairs=}')

            data = [
                (I + int(N)) % 2
                for (I, N) in pairs
            ]
            # print(f'  {data=}')

            counts = Counter(data)
            counts[0] += 0
            counts[1] += 0
            # print(f'  {counts=}')

            answers = counts.values()
            answer = min(answers)
            # print(f'  {answer} <- {tuple(answers)}')
            # print(f'MO({s}): {answer} <- {tuple(answers)}')
            return answer

        answers = [
            minOperations(
                s[i:] + s[:i]
            )
            for i in range(len(s))
        ]
        # print(f'{answers=}')

        return min(answers)

# NOTE: Acceptance Rate 41.2% (medium)

# NOTE: Time Limit Exceeded for large inputs
