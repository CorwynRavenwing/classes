class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        nodes = tuple(range(n))
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

        print(f'init: {NodeGroup=}')

        spare_cables = 0
        for Ai, Bi in connections:
            print(f'{Ai}<->{Bi}')
            if sameGroup(Ai, Bi):
                print(f'  already connected')
                spare_cables += 1
            else:
                mergeGroups(Ai, Bi)

        print(f'aftr: {NodeGroup=}')

        groups = {
            getGroup(N)
            for N in nodes
        }
        
        print(f'conn: {NodeGroup=}')
        print(f'{groups=}')
        
        disconnected = len(groups) - 1
        print(f'{disconnected=} {spare_cables=}')
        if disconnected > spare_cables:
            print(f'  Not enough cables!')
            return -1
        else:
            return disconnected

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 139 ms Beats 5.61%
# NOTE: Memory 34.88 MB Beats 71.62%
