class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        node1_distance = {}
        node2_distance = {}
        
        distance = 0
        node1_distance[node1] = 0
        node2_distance[node2] = 0
        if node1 == node2:
            return node1
        node1_set = {node1}
        node2_set = {node2}
        while node1_set or node2_set:
            distance += 1
            print(f'check {distance=}')
            new_node1_set = set()
            new_node2_set = set()
            needs_checked = False
            for n1Node in node1_set:
                next1 = edges[n1Node]
                print(f'  {next1=}')
                if next1 == -1:
                    print(f'    No outgoing edges')
                    break
                if next1 in node1_distance:
                    print(f'    Seen {next1} already')
                    break
                node1_distance[next1] = distance
                new_node1_set.add(next1)
                if next1 in node2_distance:
                    print(f'  Found {next1=} in #2')
                    needs_checked = True
            for n2Node in node2_set:
                next2 = edges[n2Node]
                print(f'  {next2=}')
                if next2 == -1:
                    print(f'    No outgoing edges')
                    break
                if next2 in node2_distance:
                    print(f'    Seen {next2} already')
                    break
                node2_distance[next2] = distance
                new_node2_set.add(next2)
                if next2 in node1_distance:
                    print(f'  Found {next2=} in #1')
                    needs_checked = True
            if needs_checked:
                node1_reachable = set(node1_distance.keys())
                node2_reachable = set(node2_distance.keys())
                both_reachable = node1_reachable & node2_reachable
                print(f'Checking...')
                print(f'  {node1_reachable=}')
                print(f'  {node2_reachable=}')
                print(f'  {both_reachable=}')
                answers = []
                for N in both_reachable:
                    distance1 = node1_distance[N]
                    distance2 = node2_distance[N]
                    max_dist = max(distance1, distance2)
                    print(f'  {N}: {distance1=} {distance2=} {max_dist=}')
                    answers.append((max_dist, N))
                answers.sort()
                print(f'{answers=}')
                (distance, N) = answers[0]
                return N
            node1_set = new_node1_set
            node2_set = new_node2_set

        print(f'No answer found.')
        return -1
# NOTE: Runtime 896 ms Beats 49.86%
# NOTE: Memory 31.37 MB Beats 90.51%
