class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        CLEAN = lambda x: tuple(sorted(x, reverse=True))
        
        queue = {
            (0,) * k    # a tuple containing K zeros
        }
        print(f'{queue=}')

        for C in CLEAN(cookies):
            print(f'{C=}')
            newQ = set()
            for distrib in queue:
                for i in range(k):
                    new_distrib = list(distrib)     # make it mutable
                    new_distrib[i] += C
                    new_distrib = CLEAN(new_distrib)
                    print(f'  [{i}]: {new_distrib}')
                    newQ.add(new_distrib)
            queue = newQ
        
        print(f'\n{queue=}')

        unfairness = tuple(map(max, queue))
        print(f'\n{unfairness=}')

        return min(unfairness)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 56 ms Beats 57.95%
# NOTE: Memory 19.38 MB Beats 5.30%
