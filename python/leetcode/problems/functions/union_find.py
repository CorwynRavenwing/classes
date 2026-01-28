
        # nodes = tuple(range(1, len(edges) + 1))

	def UnionFind(nodes: List[int], edges: List[List[int]]) -> Tuple[Dict[int,List[int]],any]:
            # note: edges may be a generator
	    # note: second return value is getGroup() fn
            # note: third return value is sameGroup() fn

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
    
            def nodeGroupMembers() -> Dict[int,List[int]]:
                NodeGroupMembers = {}
                for i, nodeName in NodeGroup.items():
                    NodeGroupMembers.setdefault(nodeName, set())
                    NodeGroupMembers[nodeName].add(i)
                return NodeGroupMembers

            for (A, B) in edges:
                mergeGroups(A, B)

            fixGroups()
            NodeGroupMembers = nodeGroupMembers()

            return (NodeGroupMembers, getGroup, sameGroup)

