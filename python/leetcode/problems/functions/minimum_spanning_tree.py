
        # edges_with_weights = [ (weight, (A, B)), ... ]
        # Minimum Spanning Tree:
        # (0) #include union_find
        # (1) sort all edges by weights in increasing order
        edges_with_weights.sort()
        total_weight = 0
        # (2) pick the smallest edge
        for (weight, edge) in edges_with_weights:
            # (3) see if this edge would make a cycle
            (A, B) = edge
            if sameGroup(A, B):
                continue
            # (4) if it doesn't, then include it in the MST
            mergeGroups(A, B)
            total_weight += weight
        
        return total_weight

