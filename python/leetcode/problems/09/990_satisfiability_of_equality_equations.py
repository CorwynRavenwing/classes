class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        equals = set()
        unequals = set()
        all_variables = set()
        for equation in equations:
            if '==' in equation:
                (A, B) = equation.split('==')
                equals.add((A,B))
                all_variables.add(A)
                all_variables.add(B)
            elif '!=' in equation:
                (A, B) = equation.split('!=')
                unequals.add((A,B))
                all_variables.add(A)
                all_variables.add(B)
            else:
                raise Exception(f'Error!  {equation=} has neither == nor !=')
        print(f'{equals=}')
        print(f'{unequals=}')

        nodes = tuple(all_variables)
        NodeGroup = {
            i: i
            for i in nodes
        }
        def getGroup(i: int) -> int:
            j = NodeGroup[i]
            if i != j:
                j = getGroup(j)
                NodeGroup[i] = j
            return j

        def sameGroup(i: int, j: int) -> bool:
            return getGroup(i) == getGroup(j)

        def mergeGroups(i: int, j: int):
            i = getGroup(i)
            j = getGroup(j)
            if i != j:
                NodeGroup[i] = j
            return

        for (A, B) in equals:
            print(f'{A} == {B}')
            mergeGroups(A, B)
        
        for (A, B) in unequals:
            print(f'{A} != {B}')
            if sameGroup(A, B):
                print(f'  Error! {A} must not equal {B}')
                return False

        return True

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 50 ms Beats 36.58%
# NOTE: Memory 17.10 MB Beats 5.77%
