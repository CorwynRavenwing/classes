class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:

        goal -= sum(nums)
        goal = abs(goal)
        print(f'new {goal=}')

        answer = sum([
            goal // limit,                      # == floor(G/L)
            (0 if (goal % limit == 0) else 1),  # add 1 if ceil(G/L) is different
        ])

        return answer

