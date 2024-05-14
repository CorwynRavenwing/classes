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

