class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        @cache
        def allPaths(source: int, target: int) -> List[List[int]]:
            print(f'AP({source},{target})')
            if source == target:
                print(f'  Success')
                return ((target,),)
            downstream = graph[source]
            if not downstream:
                print(f'  Dead end')
                return ()
            return tuple([
                (source,) + path
                for node in downstream
                for path in allPaths(node, target)
            ])
        
        n = len(graph)
        return allPaths(0, n - 1)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 77 ms Beats 35.72%
# NOTE: Memory 19.69 MB Beats 5.50%
