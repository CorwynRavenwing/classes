class ATM:

    def __init__(self):
        self.banknote_sizes = [20, 50, 100, 200, 500]
        self.banknotes_present = [0] * len(self.banknote_sizes)
        return

    def deposit(self, banknotesCount: List[int]) -> None:
        print(f'deposit({banknotesCount}):')
        for banknote_index, banknote_count in enumerate(banknotesCount):
            if banknote_count:
                print(f'  + {banknote_count} ${self.banknote_sizes[banknote_index]} bills')
                self.banknotes_present[banknote_index] += banknote_count
        print(f'DEBUG: inventory {self.banknotes_present}')
        return

    def withdraw(self, amount: int) -> List[int]:
        print(f'withdraw({amount}):')
        answer = [0] * len(self.banknote_sizes)
        for banknote_index, denomination in reversed(tuple(enumerate(self.banknote_sizes))):
            if (denomination <= amount):
                # it's not too large a bill
                we_have = self.banknotes_present[banknote_index]
                if we_have > 0:
                    # and we have any
                    he_needs = amount // denomination
                    we_give = min(he_needs, we_have)
                    if we_give:
                        answer[banknote_index] += we_give
                        amount -= (we_give * denomination)
                        print(f'  = {we_give} ${denomination} bills ({amount=})')
        if amount > 0:
            print(f'  ERROR: we cannot help this person')
            print(f'DEBUG: inventory {self.banknotes_present}')
            return [-1]
        else:
            print(f'  (remove bills from inventory)')
            for banknote_index, banknote_count in enumerate(answer):
                if banknote_count:
                    denomination = self.banknote_sizes[banknote_index]
                    print(f'  - {banknote_count} ${denomination} bills')
                    self.banknotes_present[banknote_index] -= banknote_count
            print(f'DEBUG: inventory {self.banknotes_present}')
            return answer

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
