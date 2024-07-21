class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        def condition2order(conditions: List[List[int]]) -> List[int]:
            nonlocal k
            prerequisites = {
                value: []
                for value in range(1, k + 1)
            }
            for (prereq, value) in conditions:
                prerequisites[value].append(prereq)
            print(f'{prerequisites=}')

            order = []
            while prerequisites:
                ready = [
                    number
                    for number, prereqs in prerequisites.items()
                    if all([
                        P in order
                        for P in prereqs
                    ])
                ]
                print(f'  {ready=}')
                order.extend(ready)
                for R in ready:
                    del prerequisites[R]
                if not ready:
                    return None
            return order
        
        rowOrder = condition2order(rowConditions)
        colOrder = condition2order(colConditions)
        print(f'{rowOrder=} {colOrder=}')

        if (not rowOrder) or (not colOrder):
            return []
        
        matrix = [
            [
                0
                for j in range(k)
            ]
            for i in range(k)
        ]
        print(f'empty {matrix=}')

        for value in range(1, k + 1):
            row = rowOrder.index(value)
            col = colOrder.index(value)
            matrix[row][col] = value

        print(f'full {matrix=}')

        return matrix

