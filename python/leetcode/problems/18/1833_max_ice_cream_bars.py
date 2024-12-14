class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        def countingSort(input: List[int]) -> List[int]:
            # return list(sorted(input))      # cheat
            value_upper_limit = (10 ** 5)
            counts = [0] * (value_upper_limit + 1)
            maxVal = -1
            for I in input:
                counts[I] += 1
                maxVal = max(I, maxVal)
            del counts[maxVal + 1:]
            print(f'{counts=}')
            answer = []
            for I, count in enumerate(counts):
                if count == 0:
                    continue
                answer.extend(
                    [I] * count
                )
            return answer
        
        costs = countingSort(costs)
        answer = 0
        while costs and costs[0] <= coins:
            answer += 1
            coins -= costs.pop(0)
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 792 ms Beats 5.06%
# NOTE: Memory 29.10 MB Beats 20.06%
