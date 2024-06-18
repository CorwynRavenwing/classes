class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        possible_nodes = list(range(n))
        print(f'{len(possible_nodes)} nodes, {len(edges)} edges')

        edges_by_node = {}
        for E in edges:
            for node in E:
                edges_by_node.setdefault(node, [])
                edges_by_node[node].append(E)

        node_edge_counts = {
            node: len(node_edges)
            for node, node_edges in edges_by_node.items()
        }
        
        while len(possible_nodes) > 2:
            nodes_with_one_edge = [
                node
                for node, count in node_edge_counts.items()
                if count == 1
            ]
            nodes_with_GT_2_edges = [
                node
                for node, count in node_edge_counts.items()
                if count > 2
            ]
            if (nodes_with_GT_2_edges) or (len(possible_nodes) < 10):
                # complex tree OR small tree
                for N in nodes_with_one_edge:
                    E = edges_by_node[N][0]
                    # other_node = (E[0] if (E[1] == N) else E[1])
                    other_node = sum(E) - N     # equivalent but faster
                    edges.remove(E)
                    possible_nodes.remove(N)
                    # next 2 lines might not be needed
                    edges_by_node[N].remove(E)
                    edges_by_node[other_node].remove(E)
                    node_edge_counts[N] -= 1
                    node_edge_counts[other_node] -= 1
            else:
                # print(f'linear mode: {nodes_with_GT_2_edges=} {len(possible_nodes)=}')
                # no nodes with >2 edges === linear case
                # >10 possible nodes === big tree
                # whack off 1/3 of the nodes on each end
                nodes_to_delete = []
                edges_to_delete = []
                nodes_to_check = nodes_with_one_edge
                buffer = 2  # must NOT be greater than half of "10" above
                number_to_prune = min(100, (len(possible_nodes) // 2) - buffer)
                for _ in range(number_to_prune):
                    # print(f'prune: {_} / {number_to_prune}')
                    new_check = []
                    for N in nodes_to_check:
                        if N not in nodes_to_delete:
                            # print(f'  {N=}')
                            nodes_to_delete.append(N)
                            for E in edges_by_node[N]:
                                if E not in edges_to_delete:
                                    edges_to_delete.append(E)
                                    # other_node = (E[0] if (E[1] == N) else E[1])
                                    other_node = sum(E) - N     # equivalent but faster
                                    new_check.append(other_node)
                    nodes_to_check = new_check
                print(f'ended with {nodes_to_check=}')

                for N in nodes_to_delete:
                    # possible_nodes.remove(N)
                    edges_by_node[N] = []
                    node_edge_counts[N] = 0
                
                possible_nodes = list([
                    N
                    for N in possible_nodes
                    if N not in nodes_to_delete
                ])
                
                # not sure we actually care whether 'edges' list is accurate:
                # for E in edges_to_delete:
                #     edges.remove(E)

                for N in nodes_to_check:
                    for E in edges_by_node[N]:
                        other_node = sum(E) - N     # equivalent but faster
                        print(f'cleanup {N=} {E=} {other_node=}')
                        if other_node in nodes_to_delete:
                            print(f'  delete')
                            edges_by_node[N].remove(E)
                            node_edge_counts[N] -= 1
                        # else:
                        #     print(f'  OK')
            
            # print(f'{len(possible_nodes)} nodes, {len(edges)} edges')

        return possible_nodes

