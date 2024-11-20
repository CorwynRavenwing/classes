class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:

        answer = 0
        seen_rows = set()
        seen_cols = set()
        for (typeI, indexI, valI) in reversed(queries):
            print(f'{"ROW" if typeI == 0 else "COL"} [{indexI}]={valI}')
            if typeI == 0:
                # row change
                if indexI in seen_rows:
                    print(f'  Row already seen')
                    continue
                else:
                    seen_rows.add(indexI)
                changes = n - len(seen_cols)
                # print(f'  Update {changes} columns of this row')
                answer += valI * changes
                # print(f'  answer +{valI * changes} = {answer}')
            else:
                # column change
                if indexI in seen_cols:
                    print(f'  Column already seen')
                    continue
                else:
                    seen_cols.add(indexI)
                changes = n - len(seen_rows)
                # print(f'  Update {changes} rows of this column')
                answer += valI * changes
                # print(f'  answer +{valI * changes} = {answer}')

        return answer
# NOTE: Runtime 1729 ms Beats 10.29%
# NOTE: Memory 39.38 MB Beats 34.56%
