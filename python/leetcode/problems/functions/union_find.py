
        nodes = tuple(range(1, len(edges) + 1))
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

        def fixGroups():
            for i in nodes:
                _ = getGroup(i)

        def sameGroup(i: int, j: int) -> bool:
            return getGroup(i) == getGroup(j)

        def mergeGroups(i: int, j: int):
            i = getGroup(i)
            j = getGroup(j)
            if i != j:
                NodeGroup[i] = j
            return


