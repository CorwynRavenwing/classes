class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        
        # making the rules make sense:
        # start anywhere
        # jump from current index to any index within 'd' spaces inclusive
        # can only jump *TO* indexes with strictly lower values
        # can only jump OVER indexes with strictly lower values
        # return the max NUMBER OF JUMPS possible

        LEN = len(arr)

        def DP_MAX_OF_LIST(indexes: List[int]) -> int:
            answers = [
                DP(i)
                for i in indexes
            ]
            return max(answers, default=0)
        
        @cache
        def DP(index: int) -> int:
            print(f'DP({index})')
            compare = arr[index]
            indexes = set()
            possible_diffs = tuple(range(1, d+1))
            for diff in possible_diffs:
                j = index + diff
                if j >= LEN:
                    print(f'  [{j}]: OOB')
                    break
                value = arr[j]
                if value >= compare:
                    print(f'  [{j}]:{value} >= {compare}')
                    break
                indexes.add(j)
            for diff in possible_diffs:
                j = index - diff
                if j < 0:
                    print(f'  [{j}]: OOB')
                    break
                value = arr[j]
                if value >= compare:
                    print(f'  [{j}]:{value} >= {compare}')
                    break
                indexes.add(j)
            print(f'DP({index}): [{indexes}]')
            answer = 1 + DP_MAX_OF_LIST(indexes)
            print(f'DP({index}): {answer}')
            return answer
        
        return DP_MAX_OF_LIST(range(LEN))

# NOTE: Acceptance Rate 65.7% (HARD)

# NOTE: Accepted on second Run (deal with 0 case)
# NOTE: Accepted on second Submit (Output Exceeded: add cache)
# NOTE: Runtime 873 ms Beats 5.43%
# NOTE: Memory 70.16 MB Beats 5.14%
