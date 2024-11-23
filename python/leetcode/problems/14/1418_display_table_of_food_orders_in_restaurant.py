class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        
        Data = Counter()
        Tables = set()
        Foods = set()
        for (name_ignore, table, food) in orders:
            Tables.add(table)
            Foods.add(food)
            key = (table, food)
            Data[key] += 1
        
        FoodList = list(sorted(Foods))
        NUMERICALLY = lambda X: int(X)
        TableList = list(sorted(Tables, key=NUMERICALLY))
        answer = []
        answer.append(
            ["Table"] + FoodList
        )
        for table in TableList:
            orders = [
                str(Data[(table, food)])
                for food in FoodList
            ]
            answer.append(
                [table] + orders
            )
        return answer

# NOTE: Accepted on third Run (string/integer errors)
# NOTE: Accepted on first Submit
# NOTE: Runtime 348 ms Beats 26.11%
# NOTE: Memory 41.65 MB Beats 27.48%
