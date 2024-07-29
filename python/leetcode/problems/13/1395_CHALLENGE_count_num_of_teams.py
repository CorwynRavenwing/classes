class Solution:
    def numTeams(self, rating: List[int]) -> int:

        LEN = len(rating)
        LowerLeftCount = [0] * LEN
        LowerRightCount = [0] * LEN
        GreaterLeftCount = [0] * LEN
        GreaterRightCount = [0] * LEN
        for i, A in enumerate(rating):
            # print(f'{i=} {A=}')
            for j, B in enumerate(rating):
                if i >= j:
                    continue
                # print(f'  {j=} {B=}')
                if A < B:
                    GreaterRightCount[i] += 1
                    LowerLeftCount[j] += 1
                elif A > B:
                    LowerRightCount[i] += 1
                    GreaterLeftCount[j] += 1
                else:
                    print(f'ERROR: [{i},{j}] {A} == {B}')
                    return -777
        print(f'{LowerLeftCount=}')
        print(f'{LowerRightCount=}')
        print(f'{GreaterLeftCount=}')
        print(f'{GreaterRightCount=}')

        answer = 0
        increasing = list(zip(LowerLeftCount, GreaterRightCount))
        decreasing = list(zip(GreaterLeftCount, LowerRightCount))
        for (L, R) in increasing + decreasing:
            product = L * R
            print(f'{L=} * {R=} = {product}')
            answer += product

        return answer

