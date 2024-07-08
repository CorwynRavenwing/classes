class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        friends = list(range(1, n + 1))
        it = 0  # 0-based location in list, not friend number
        print(f'{it=} {friends=}')
        while len(friends) > 1:
            it += k - 1         # add K, counting from 1
            it %= len(friends)  # wrap around remaining friends
            friends[it] = None
            del friends[it]
            print(f'{it=} {friends=}')
        return friends[0]

