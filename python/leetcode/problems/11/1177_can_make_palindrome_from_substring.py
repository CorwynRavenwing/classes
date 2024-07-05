class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:

        prefixes = [None] * len(s)
        counts = Counter()
        for i, C in enumerate(s):
            counts[C] += 1
            prefixes[i] = counts.copy()
        # print(f'{prefixes=}')

        def onePaliAnswer(Li:int, Ri: int, Ki: int) -> bool:
            # nonlocal prefixes
            # counts = Counter(s[Li:Ri + 1])
            pL = prefixes[Li - 1] if Li else Counter()
            pR = prefixes[Ri]
            counts = pR - pL
            # print(f'{pL=}')
            # print(f'{pR=}')
            # print(f'{counts=}')
            odds = 0
            for letter, count in counts.items():
                # print(f'  "{letter}": {count}')
                if count % 2 != 0:
                    odds += 1
            # each K can turn 2 odds into 2 evens;
            # there may be 1 odd left over
            # print(f'  {odds=}')
            return odds <= 1 + (2 * Ki)

        cache = {}
        def onePaliCached(Li:int, Ri: int, Ki: int) -> bool:
            T = (Li, Ri, Ki)
            if T in cache:
                # print(f'cache hit {T}')
                return cache[T]
            else:
                # print(f'          cache miss {T}')
                result = onePaliAnswer(Li, Ri, Ki)
                cache[T] = result
                return result

        return [
            onePaliCached(Li, Ri, Ki)
            for (Li, Ri, Ki) in queries
        ]

