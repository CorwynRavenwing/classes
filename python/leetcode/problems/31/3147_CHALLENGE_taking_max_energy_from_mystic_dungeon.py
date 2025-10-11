class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:

        n = len(energy)
        print(f'{k=} {n=} {energy=}')
        answers = energy[:]
        print(f'{answers=}')
        
        for i in reversed(range(n-k)):
            # span answers from right to left
            # starting with the highest that has an "i + k" to its right
            # print(f'{i=} ({answers[i]}) add answers[{i + k}] ({answers[i + k]})')
            answers[i] += answers[i + k]
        
        print(f'{answers=}')
        return max(answers)

# NOTE: Acceptance Rate 44.3% (medium)

# NOTE: re-ran for challenge:
# NOTE: Runtime 1183 ms Beats 43.13%
# NOTE: Memory 30.75 MB Beats 92.50%
