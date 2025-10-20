class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        X = 0
        for op in operations:
            match op:
                case "X++":
                    X += 1
                case "++X":
                    X += 1
                case "X--":
                    X -= 1
                case "--X":
                    X -= 1
                case _:
                    raise Exception(
                        f'Invalid {op=}'
                    )
        return X

# NOTE: Acceptance Rate 89.7% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.88 MB Beats 37.61%
