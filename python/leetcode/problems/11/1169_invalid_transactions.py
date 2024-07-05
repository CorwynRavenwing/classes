class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        nameArr = []
        timeArr = []
        amountArr = []
        cityArr = []
        for T in transactions:
            (name, time, amount, city) = T.split(',')
            nameArr.append(name)
            timeArr.append(int(time))
            amountArr.append(int(amount))
            cityArr.append(city)
        invalids = set()
        for i in range(len(transactions)):
            if amountArr[i] > 1000:
                print(f'large transaction {i}')
                invalids.add(i)
            for j in range(i + 1, len(transactions)):
                nameMatch = nameArr[i] == nameArr[j]
                cityMismatch = cityArr[i] != cityArr[j]
                timeNearby = abs(timeArr[i] - timeArr[j]) <= 60
                if (nameMatch and cityMismatch and timeNearby):
                    print(f'mismatch transactions {i} {j}')
                    invalids.add(i)
                    invalids.add(j)
        invalidTransactions = [
            T
            for i, T in enumerate(transactions)
            if i in invalids
        ]
        return invalidTransactions

