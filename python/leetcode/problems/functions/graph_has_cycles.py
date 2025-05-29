
        def graph_has_cycles(n: int, ChildrenOf: Dict[int,Set[int]]) -> bool:
            print(f'GHC({n}):')
            seen = [False] * n
            loop = [False] * n

            def node_has_cycles(node: int) -> bool:
                print(f'    NHC({node})')
                if loop[node]:
                    print(f'      YES')
                    return True
                else:
                    loop[node] = True
                    for child in ChildrenOf[node]:
                        if node_has_cycles(child):
                            print(f'      YES')
                            return True
                    loop[node] = False
                    print(f'      no')
                    return False

            for i in range(n):
                if seen[i]:
                    print(f'  {i}: seen')
                    continue
                else:
                    seen[i] = True
                print(f'  {i}: check')
                if node_has_cycles(i):
                    return True
            print(f'  No cycles.')
            return False
        
        if graph_has_cycles(n, ChildrenOf):
            print(f'  GRAPH HAS CYCLES')
            return -1

