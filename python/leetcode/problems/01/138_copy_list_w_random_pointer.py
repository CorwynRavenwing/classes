"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # we borrow some code from #133:
        
        if not head:
            return None

        print(f'{head.val=}')
        print(f'{head.next=}')
        print(f'{head.random=}')
        root_id = hash(head)
        random_ids = {}
        orig_nodes = {}
        new_nodes = {}
        N = head
        prev_N = None
        while N:
            id = hash(N)
            if id in orig_nodes:
                print(f'{id}: (seen)')
                N = N.next
                continue
            else:
                print(f'{id=}')
                orig_nodes[id] = N
                if id in new_nodes:
                    raise Exception(f'for {id=}, found in new_nodes but not found in orig_nodes')
                new_N = Node(N.val)         # Clone a copy.  No "next" or "random" yet.
                new_nodes[id] = new_N
                if prev_N:
                    prev_N.next = new_N     # add "next" link
                prev_N = new_N

                if id in random_ids:
                    raise Exception(f'for {id=}, found in random_ids but not found in orig_nodes')
                if N.random:
                    print(f'  N.random -> {N.random.val}')
                    random_ids[id] = hash(N.random)
            N = N.next

        print(f'{random_ids=}')

        for N_id, R_id in random_ids.items():
            N = new_nodes[N_id]
            A = new_nodes[R_id]
            N.random = A            # add "random" link

        return new_nodes[root_id]

# NOTE: Reused quite a bit of the prior version's code
# NOTE: Unlike the prior version, node.val is NOT unique
# NOTE: Accepted on first Submit
# NOTE: Runtime 31 ms Beats 91.61%
# NOTE: Memory 17.66 MB Beats 6.97%
