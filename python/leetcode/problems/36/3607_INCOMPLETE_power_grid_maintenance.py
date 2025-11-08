class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        # 0. Union Find the Stations, making connected-power-station Groups.
        #    for each Group, a set of all members is created.
        #    for each Group, a Master is calculated as min(Group Members).

        nodes = tuple(range(1, c + 1))
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

        for (Ui, Vi) in connections:
            mergeGroups(Ui, Vi)
        
        fixGroups()

        groupMembers = nodeGroupMembers()
        # print(f'{groupMembers=}')

        groupMaster = {
            groupID: min(Members)
            for groupID, Members in groupMembers.items()
        }
        # print(f'{groupMaster=}')

        answer = []
        for Q in queries:
            # print(f'{Q=}')
            queryType, Station = Q
            groupID = getGroup(Station)
            Master = groupMaster[groupID]
            # print(f'  {groupID=} {Master=}')
            if queryType == 1:
                # 1. for query type 1,
                if Station in groupMembers[groupID]:
                    #    return either the Station ID (if active)
                    # print(f'    (on: answer {Station=})')
                    answer.append(Station)
                else:
                    #    or the Master of the Group for this Station
                    # print(f'    (off: answer {Master=})')
                    answer.append(Master)
            else:
                assert queryType == 2
                # 2. for query type 2,
                #    remove the Station from it's Group's Member set.
                #    if the Station was its own Master, re-calculate the Master.
                if Station in groupMembers[groupID]:
                    # print(f'    (TURN OFF {Station=})')
                    groupMembers[groupID].remove(Station)
                    if Master == Station:
                        Master = min(
                            groupMembers[groupID],
                            default=-1
                        )
                        # print(f'      new {Master=}')
                        groupMaster[groupID] = Master
                # else:
                #     # print(f'    (already off)')

        return answer

# NOTE: Acceptance Rate 44.8% (medium)

# NOTE: Time Limit Exceeded for large inputs
