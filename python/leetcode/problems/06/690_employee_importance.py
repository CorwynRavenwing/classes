"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        employeeDataByID = {}
        for E in employees:
            employeeDataByID[E.id] = E
        
        def getImportanceRecursive(id: int) -> int:
            E = employeeDataByID[id]
            subordinateImporances = [
                getImportanceRecursive(subordinate_id)
                for subordinate_id in E.subordinates
            ]
            print(f'GIR({id}): {E.importance} + {subordinateImporances}')
            return E.importance + sum(subordinateImporances)
        
        return getImportanceRecursive(id)

# NOTE: Accepted on third Run (first two were variable-name typos)
# NOTE: Accepted on first Submit
# NOTE: Runtime 116 ms Beats 45.48%
# NOTE: Memory 17.98 MB Beats 24.49%
