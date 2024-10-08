class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:

        def subtractItems(original: List[int], items: List[int]) -> List[int]:
            # print(f'SI():')
            # print(f'   {original}')
            # print(f'  -{items}')
            answer = tuple([
                A - B
                for A, B in zip(original, items)
            ])
            # print(f'  ={answer}')
            retVal = (
                answer
                if min(answer) >= 0
                else None
            )
            # print(f'  ={retVal}')
            return retVal

        availableDeals = set()
        N = len(price)
        for item_id, P in enumerate(price):
            # print(f'price ${P} for 1 * #{item_id}')
            itemList = [0] * N
            itemList[item_id] = 1
            availableDeals.add(
                (P, tuple(itemList))
            )
        # print(f'{availableDeals=}')

        for S in special:
            # print(f'({S=})')
            P = S[-1]   # price is last element
            S = S[:-1]  # all other elements are quantities of products

            # print(f'deal: ${P} for {S}')
            availableDeals.add(
                (P, tuple(S))
            )
        # print(f'{availableDeals=}')

        queue = {(0, tuple(needs))}
        # print(f'{queue=}')
        answers = set()
        for P, itemList in availableDeals:
            newQ = set()
            for (origPrice, Q) in queue:
                # print(f'{Q}:')
                if sum(Q) == 0:
                    # print(f'  DONE (${origPrice})')
                    answers.add(origPrice)
                    # don't try subtracting from zero
                    continue
                totalPrice = origPrice
                itemsRemaining = Q
                multi = 0
                while itemsRemaining:
                    itemsRemaining = subtractItems(itemsRemaining, itemList)
                    if itemsRemaining is None:
                        break
                    multi += 1
                    totalPrice += P
                    # print(f'  {multi} * deal ${P} {itemList}')
                    newQ.add(
                        (totalPrice, itemsRemaining)
                    )
            queue |= newQ

        # now deal with anything that zeroed out during the final deal
        # print(f'Cleanup:')
        for (origPrice, Q) in queue:
            # print(f'{Q}:')
            if sum(Q) == 0:
                # print(f'  DONE (${origPrice})')
                answers.add(origPrice)
                # don't try subtracting from zero
                continue
        
        print(f'{answers=}')
        return min(answers)

# NOTE: works for small inputs, Time Limit Exceeded for large inputs
