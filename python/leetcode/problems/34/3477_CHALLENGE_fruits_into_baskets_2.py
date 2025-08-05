class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        answer = 0
        for i, F in enumerate(fruits):
            print(f'[{i}]: {F=}')
            found = False
            for j, B in enumerate(baskets):
                if B >= F:
                    print(f'  -> [{j}]: {B=}')
                    baskets[j] = -1
                    found = True
                    break
            if not found:
                answer += 1
                print(f'  => NOPE {answer=}')

        return answer

# NOTE: Acceptance Rate 55.1% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 43 ms Beats 11.73%
# NOTE: Memory 18.13 MB Beats 5.55%
