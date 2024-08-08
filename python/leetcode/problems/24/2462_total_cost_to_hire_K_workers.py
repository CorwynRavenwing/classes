class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        leftHeap = costs[:candidates]
        del costs[:candidates]
        rightHeap = costs[-candidates:]
        del costs[-candidates:]

        leftHeap.sort()
        rightHeap.sort()
        answer = 0
        while k:
            # print(f'{k=} {answer=} {leftHeap=} {costs=} {rightHeap=}')
            print(f'{k=} {answer=} {len(leftHeap)} {len(costs)} {len(rightHeap)}')
            k -= 1
            leftBest = (leftHeap[0] if leftHeap else float('+inf'))
            rightBest = (rightHeap[0] if rightHeap else float('+inf'))
            if leftBest <= rightBest:
                answer += leftHeap.pop(0)
                if costs:
                    newGuy = costs.pop(0)   # take leftmost one
                    bisect.insort(leftHeap, newGuy)
            else:
                answer += rightHeap.pop(0)
                if costs:
                    newGuy = costs.pop(-1)  # take rightmost one
                    bisect.insort(rightHeap, newGuy)
        # print(f'{k=} {answer=} {leftHeap=} {costs=} {rightHeap=}')
        print(f'{k=} {answer=} {len(leftHeap)} {len(costs)} {len(rightHeap)}')

        return answer
# NOTE: Runtime 2909 ms Beats 5.04%
# NOTE: Memory 27.12 MB Beats 58.05%
