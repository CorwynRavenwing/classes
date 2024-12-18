class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        answer = [None] * len(prices)

        stack = []
        for j, P in enumerate(prices):
            print(f'[{j}]{P}:')
            while stack:
                # print(f'  DEBUG: {stack=}')
                (i, orig_price) = stack[-1]
                if orig_price < P:
                    break
                assert answer[i] is None
                answer[i] = orig_price - P
                _ = stack.pop(-1)
                # print(f'  DEBUG: {answer=}')
            stack.append(
                (j, P)
            )
        print(f'CLEANUP:')
        while stack:
            # print(f'  DEBUG: {stack=}')
            (i, orig_price) = stack.pop(-1)
            print(f'[{i}]{orig_price}:')
            assert answer[i] is None
            answer[i] = orig_price
            # print(f'  DEBUG: {answer=}')
        return answer

# NOTE: Accepted on second Run (</<= error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 5 ms Beats 8.60%
# NOTE: Memory 17.84 MB Beats 10.22%
