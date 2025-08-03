class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        totals = count1 + count2
        min_cost = min(totals.keys())
        half = Counter({
            element: count // 2
            for element, count in totals.items()
        })
        ELEM = lambda C: list(sorted(C.elements()))
        diff1 = ELEM(count1 - half)
        diff2 = ELEM(count2 - half)

        print(f'{count1=}')
        print(f'{count2=}')
        print(f'{totals=}')
        print(f'{half=}')
        print(f'{min_cost=}')
        print(f'{diff1=}')
        print(f'{diff2=}')

        for check in totals.values():
            if check % 2 != 0:
                print(f'FAIL')
                return -1
        
        answer = 0
        while diff1 and diff2 and diff1[0] < diff2[-1] and diff1[0] < 2 * min_cost:
            A = diff1.pop(0)
            B = diff2.pop(-1)
            print(f'A: swap {A}, {B}')
            answer += A

        while diff1 and diff2 and diff2[0] < diff1[-1] and diff2[0] < 2 * min_cost:
            A = diff2.pop(0)
            B = diff1.pop(-1)
            print(f'B: swap {A}, {B}')
            answer += A

        while diff1 and diff2 and diff1[0] < diff2[-1]:
            A = diff1.pop(0)
            B = diff2.pop(-1)
            print(f'C: swap {A}, {B} @ {2 * min_cost}')
            answer += 2 * min_cost

        while diff1 and diff2 and diff2[0] < diff1[-1]:
            A = diff2.pop(0)
            B = diff1.pop(-1)
            print(f'D: swap {A}, {B} @ {2 * min_cost}')
            answer += 2 * min_cost

        return answer

# NOTE: Acceptance Rate 35.7% (HARD)

# NOTE: Accepted on second Run (accidentally swapped both directions)
# NOTE: Accepted on first Submit
# NOTE: Runtime 570 ms Beats 5.19%
# NOTE: Memory 63.53 MB Beats 5.19%
