class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:

        # SHORTCUT: to maximize the total rewards, we want Mouse 1 to eat
        # the K specific types of cheese for which the difference in rewards
        # is most greatly in his favor.

        data = [
            (R1 - R2, R1, R2)
            for R1, R2 in zip(reward1, reward2)
        ]
        data.sort(reverse=True)
        # print(f'{data=}')
        mouse1 = [
            R1
            for diff, R1, R2 in data[:k]
        ]
        mouse2 = [
            R2
            for diff, R1, R2 in data[k:]
        ]
        print(f'{mouse1=}')
        print(f'{mouse2=}')
        
        return sum(mouse1) + sum(mouse2)
# NOTE: Runtime 729 ms Beats 56.10%
# NOTE: Memory 34.25 MB Beats 60.31%
