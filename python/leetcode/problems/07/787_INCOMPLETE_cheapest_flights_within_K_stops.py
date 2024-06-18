class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        states = [
            ([], src, 0)     # 0 prior cities, in Src, cost 0 dollars
        ]
        answer = None
        while states:
            print(f'L={len(states)}')
            S = states.pop()
            print(f'  {S=}')
            (prior_cities, current_city, cost_so_far) = S
            if answer is not None and cost_so_far >= answer:
                print(f'    ... too much money (${answer})')
                continue
            # "+1" b/c A -> B is 1 prior city but zero stops:
            if len(prior_cities) > k + 1:
                print(f'    ... too many stops ({len(prior_cities) - 1})')
                continue
            if current_city == dst:
                print(f'    arrive at {dst} for ${cost_so_far}')
                if answer is None or answer > cost_so_far:
                    answer = cost_so_far
                continue
            for F in flights:
                (fromCity, toCity, flightPrice) = F
                if fromCity == current_city:
                    if toCity in prior_cities:
                        # print(f'    -> {toCity} --loop--')
                        continue
                    # print(f'    -> {toCity} ${flightPrice}')
                    states.append(
                        (
                            prior_cities + [current_city],
                            toCity,
                            cost_so_far + flightPrice,
                        )
                    )
        print(f'{answer=}')
        return (
            answer
            if answer is not None
            else -1
        )

# NOTE: in progress
