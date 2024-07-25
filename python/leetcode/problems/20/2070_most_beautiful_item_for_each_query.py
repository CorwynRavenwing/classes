class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        beautyByPrice = sorted(map(tuple, items))
        # print(f'{beautyByPrice=}')
        while True:
            for i in range(1, len(beautyByPrice)):
                (thisPrice, thisBeauty) = beautyByPrice[i]
                (prevPrice, prevBeauty) = beautyByPrice[i - 1]
                if thisPrice == prevPrice:
                    beautyByPrice[i - 1] = None
                    beautyByPrice[i] = (thisPrice, max(thisBeauty, prevBeauty))
                    # print(f'Merge {i}')
            if None in beautyByPrice:
                while None in beautyByPrice:
                    beautyByPrice.remove(None)
                # print(f'{beautyByPrice=}')
            else:
                # print(f'Done updating beautyByPrice')
                break
        print(f'{beautyByPrice=}')
        priceList = [P for (P, B) in beautyByPrice]
        beautyList = [B for (P, B) in beautyByPrice]
        print(f' {priceList=}')
        print(f'{beautyList=}')
        beautyMaxLeft = list(itertools.accumulate(beautyList, max))
        print(f'{beautyMaxLeft=}')

        def doQuery(query: int) -> int:
            index = bisect_right(priceList, query)
            if index > 0:
                index -= 1
            print(f'Q({query}): {index=} {priceList[index]}')
            if priceList[index] > query:
                print(f'  Too high')
                return 0
            print(f'  {beautyList[index]} {beautyMaxLeft[index]}')
            return beautyMaxLeft[index]
        
        return [
            doQuery(Q)
            for Q in queries
        ]
# NOTE: accepted upon first submission :-)
