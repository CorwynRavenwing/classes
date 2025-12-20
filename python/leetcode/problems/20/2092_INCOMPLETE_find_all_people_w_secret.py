class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        # NOTE: because the secret is shared in any number of
        # simultaneous meetings, all people with a meeting
        # at the same time, that includes any shared people,
        # are all effectively in the same meeting.

        # second returned parameter is the getGroup() function
        def UnionFind(nodes: List[int], edges: List[List[int]]) -> Tuple[Dict[int,List[int]],any]:
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
            return [
                nodeGroupMembers(),
                getGroup
            ]

        meetings.append([0, firstPerson, 0])
        sortByTime = lambda L: L[2]
        meetings.sort(key=sortByTime)
        meetingGroupsAtTime = {}
        for (X, Y, Time) in meetings:
            meetingGroupsAtTime.setdefault(Time, [])
            meetingGroupsAtTime[Time].append( (X,Y) )
        # print(f'{meetingGroupsAtTime=}')

        times = sorted(meetingGroupsAtTime.keys())
        # print(f'{times=}')

        nodes = range(n)
        has_secret = {0}
        for Time in times:
            meetingsThen = meetingGroupsAtTime[Time]
            (groupMembers, getGroup) = UnionFind(nodes, meetingsThen)
            print(f'  {Time=}')
            # print(f'    {groupMembers=}')
            # print(f'    {getGroup=}')

            groupMembers = {
                group_id: in_group
                for (group_id, in_group) in groupMembers.items()
                if len(in_group) > 1
            }
            # print(f'    {groupMembers=}')

            groups_with_members = set(groupMembers.keys())

            new_secret = set()
            for P in has_secret:
                p_group = getGroup(P)
                if p_group not in groups_with_members:
                    continue
                try:
                    p_met = groupMembers[p_group]
                except KeyError:
                    continue
                # print(f'    {P=} {p_group=} {p_met=}')
                new_secret |= p_met
                # print(f'      {new_secret=}')
            has_secret |= new_secret
            # print(f'    {has_secret=}')

        return tuple(has_secret)

# NOTE: Acceptance Rate 45.6% (HARD)

# NOTE: Incomplete: Time Limit Exceeded for large inputs
