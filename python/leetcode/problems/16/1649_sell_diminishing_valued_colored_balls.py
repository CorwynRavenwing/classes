class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:

        mod = 10 ** 9 + 7

        def triangle_number(N: int) -> int:
            return N * (N + 1) // 2

        # special case for one color of balls:
        if len(inventory) == 1:
            INV = inventory[0]
            if INV == orders:
                # if we're selling all of them:
                profit = triangle_number(orders)
                return profit % mod
            else:
                # we're selling less than that:
                profit = triangle_number(INV) - triangle_number(INV - orders)
                return profit % mod

        invCount = Counter(inventory)
        # print(f'{invCount=}')
        invCountLevels = sorted(invCount.keys())
        # print(f'{invCountLevels=}')
        maxCount = invCountLevels.pop()
        print(f'{maxCount=}')

        profit = 0
        while orders:
            maxAvail = invCount[maxCount]
            if invCountLevels:
                secondHighestCount = invCountLevels.pop()
            else:
                secondHighestCount = 0
            batchSize = maxAvail * (maxCount - secondHighestCount)
            if batchSize > orders:
                print(f'Not enough orders for entire batch ({batchSize} > {orders})')
                # undo the pop() from above:
                invCountLevels.append(secondHighestCount)
                # the following is the previous equation inside-out:
                batchFraction = (orders // maxAvail)
                if not batchFraction:
                    print(f'{batchFraction=}: quit batch')
                    break
                secondHighestCount = maxCount - batchFraction
                print(f'Try new {secondHighestCount=}')
                # repeat this work and verify we're correct:
                batchSize = maxAvail * (maxCount - secondHighestCount)
                if batchSize > orders:
                    print(f'STILL not enough orders for entire batch ({batchSize} > {orders})')
                    break
            print(f'{batchSize=} {orders=}')
            buying = batchSize
            if buying == 0:
                print(f'batch {buying=}: quit batch')
                break
            price = maxAvail * (triangle_number(maxCount) - triangle_number(secondHighestCount))
            print(f'sell batch {buying} @T({maxCount}) = {price}')
            profit += price
            orders -= buying
            print(f'{profit=} {orders=}')
            invCount[maxCount] -= maxAvail
            assert invCount[maxCount] == 0
            del invCount[maxCount]
            invCount[secondHighestCount] += maxAvail
            maxCount = secondHighestCount
            # print(f'{invCount=}')

        print(f'singleton section: {profit=} {orders=} {maxCount=}')
        # print(f'{invCount=}')
        while orders:
            maxAvail = invCount[maxCount]
            if maxAvail <= 0:
                # print(f'No more with inventory={maxCount}')
                del invCount[maxCount]
                maxCount -= 1
                continue
            buying = min(maxAvail, orders)
            price = buying * maxCount
            # print(f'sell {buying} @{maxCount} = {price}')
            profit += price
            orders -= buying
            # print(f'{profit=} {orders=}')
            invCount[maxCount] -= buying
            invCount[maxCount - 1] += buying
            # print(f'{invCount=}')

        return profit % mod
# NOTE: 512 ms; Beats 73.33%
