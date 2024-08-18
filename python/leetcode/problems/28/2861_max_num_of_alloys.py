class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        
    # this version is for maximizing something.

        def canMakeTargetUnderBudgetOnSomeMachine(target: int) -> bool:
            costOfTargetUnitsOnEachMachine = [
                sum([
                    (
                        0
                        if (target * needI) <= stockI
                        else
                        ((target * needI) - stockI) * costI
                    )
                    for (needI, stockI, costI) in zip(AlloyComponents, stock, cost)
                ])
                for AlloyComponents in composition
            ]
            # print(f'{costOfTargetUnitsOnEachMachine=}')
            return min(costOfTargetUnitsOnEachMachine) <= budget

        # nums.sort()

        L = 0
        left = canMakeTargetUnderBudgetOnSomeMachine(L)
        if not left:
            print(f'Strange, {L=} is false')
            return L
        
        R = 1
        while (right := canMakeTargetUnderBudgetOnSomeMachine(R)):
            R *= 10
        if right:
            print(f'Strange, {R=} is true')
            return -1
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = canMakeTargetUnderBudgetOnSomeMachine(M)
            print(f'[{L},{M},{R}] ({left},{mid},{right})')
            if mid:
                print(f'  True: replace Left')
                (L, left) = (M, mid)
            else:
                print(f'  False: replace Right')
                (R, right) = (M, mid)

        print(f'[{L},{R}] ({left},{right})')
        # L is now the highest possible True value
        return L
# NOTE: This is not actually maximizing the "number of alloys",
#       but rather the "number of units of some alloy".
# NOTE: Runtime 320 ms Beats 87.50%
# NOTE: Memory 17.06 MB Beats 40.62%
