class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if len(original) != m * n:
            print(f'{len(original)=} != {(m * n)=}')
            # return [[]]
            # Annoyingly, even though they say "return an empty 2D array",
            # they actually want an empty *1D* array.
            return []
        
        answer = []
        while original:
            answer.append(
                original[:n]
            )
            original = original[n:]
        
        return answer

# NOTE: Accepted on second Run (first run failed b/c they asked
#       for an empty 2D array [[]] when they wanted a 1D array []
# NOTE: Accepted on first Submit
# NOTE: Runtime 1934 ms Beats 5.18%
# NOTE: Memory 24.20 MB Beats 31.73%
