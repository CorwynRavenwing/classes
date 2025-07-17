class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        
        coins.sort()
        
        # we borrow some code from #330:
        # rename nums -> coins
        # rename n -> target

        max_reachable = 0
        answer = 0

        for num in coins:
            next_int = max_reachable + 1
            while num > next_int:
                if next_int > target:
                    print(f'All numbers from {1} to {target} are reachable: STOP')
                    return answer
                print(f'{max_reachable}: [{next_int}] ADD')
                answer += 1
                max_reachable += next_int
                next_int = max_reachable + 1
            print(f'{max_reachable}: [{num}] in original array')
            # don't add to answer here: original array members are free
            max_reachable += num

        while max_reachable < target:
            i = max_reachable + 1
            print(f'[{i}] not reachable: add')
            answer += 1
            max_reachable += i

        return answer

# NOTE: Acceptance Rate 56.9% (medium)
# NOTE: ... but it's a duplicate of a Hard ?!?

# NOTE: used entire prior version, renamed vars, sort input array
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 281 ms Beats 5.56%
# NOTE: Memory 28.72 MB Beats 10.42%
