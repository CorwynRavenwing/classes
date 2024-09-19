"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        
        print(f'{node.val=}')
        # print(f'{node.neighbors=}')
        
        root_id = node.val
        adjacent = {}
        orig_nodes = {}
        new_nodes = {}
        queue = [node]
        while queue:
            N = queue.pop(0)
            id = N.val
            if id in orig_nodes:
                # print(f'  (seen)')
                continue
            else:
                print(f'{id=}')
                orig_nodes[id] = N
                if id in new_nodes:
                    raise Exception(f'for {id=}, found in new_nodes but not found in orig_nodes')
                new_nodes[id] = Node(id)    # Clone a copy.  No neighbors yet.
                if id in adjacent:
                    raise Exception(f'for {id=}, found in adjacent but not found in orig_nodes')
                adjacent[id] = [
                    A.val
                    for A in N.neighbors
                ]
                queue.extend(N.neighbors)

        print(f'{adjacent=}')
        
        for N_id, A_id_list in adjacent.items():
            N = new_nodes[N_id]
            for A_id in A_id_list:
                A = new_nodes[A_id]
                N.neighbors.append(A)
        
        return new_nodes[root_id]

# NOTE: Accepted on first Submit
# NOTE: Runtime 39 ms Beats 66.76%
# NOTE: Memory 17.13 MB Beats 5.53%
