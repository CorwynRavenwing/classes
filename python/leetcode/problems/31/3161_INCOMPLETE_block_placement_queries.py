class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        
        answers = []

        for query in queries:
            query_type = query.pop(0)
            if query_type == 1:
                X = query.pop(0)
                print(f'{X=}')
                # ...
                # insert each X into a list of blocks
                # keep track of distances between them
                # possibly have a fake block at "max X value used +1"
                # also keep track of max distance partial sum
                # ...
            elif query_type == 2:
                X = query.pop(0)
                sz = query.pop(0)
                print(f'{X=} {sz=}')
                # ...
                # find X in partial sums list
                # return max-value >= sz
                # ...
                answers.append(-42)
            else:
                assert query_type in [1, 2]
        
        return answers

# NOTE: Acceptance Rate 18.9% (HARD)

# NOTE: Incomplete, must do the algorithm described
