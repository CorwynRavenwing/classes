class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness.sort(reverse=True)
        children = happiness[:k]
        print(f"{children}")
        print(f"{len(children)=} {k=}")
        answer = 0
        for i, child in enumerate(children):
            diff = max(0, child - i)
            answer += diff
            print(f"{child=} {i=} {diff=} {answer=}")
            if diff == 0:
                break

        return answer

