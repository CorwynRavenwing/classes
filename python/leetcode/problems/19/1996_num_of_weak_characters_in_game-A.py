class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:

        properties.sort()
        for i, Char1 in enumerate(properties):
            print(f'{i}: {Char1}')
            A1, D1 = Char1
            for j, Char2 in enumerate(properties):
                if i >= j:
                    continue
                # print(f'  {j}: {Char2}')
                A2, D2 = Char2
                if (A1 < A2) and (D1 < D2):
                    print(f'    {i} is weak to {j}')
                    answer += 1
                    # don't double-count this I being weak to every J
                    break
        return answer
# NOTE: works for small inputs, Time Limit Exceeded for large inputs
