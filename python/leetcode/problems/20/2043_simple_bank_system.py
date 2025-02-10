class Bank:

    def __init__(self, balance: List[int]):
        balance = [None] + balance
        self.accounts = len(balance)
        self.balance = balance
        return

    def __legal_account(self, account: int) -> bool:
        return (0 < account < self.accounts)
    
    def __amount_available(self, account: int, money: int) -> bool:
        if not self.__legal_account(account):
            return False
        return (self.balance[account] >= money)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        print(f'transfer({account1},{account2},${money})')
        if not self.__legal_account(account1):
            print(f'  NO: bad {account1=}')
            return False
        if not self.__legal_account(account2):
            print(f'  NO: bad {account2=}')
            return False
        if not self.__amount_available(account1, money):
            print(f'  NO: NSF {account1=} ${money} > ${self.balance[account1]}')
            return False
        self.balance[account1] -= money
        self.balance[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        print(f'deposit({account},${money})')
        if not self.__legal_account(account):
            print(f'  NO: bad {account=}')
            return False
        self.balance[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        print(f'withdraw({account},${money})')
        if not self.__legal_account(account):
            print(f'  NO: bad {account=}')
            return False
        if not self.__amount_available(account, money):
            print(f'  NO: NSF {account=} ${money} > ${self.balance[account]}')
            return False
        self.balance[account] -= money
        return True

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)

# NOTE: Accepted on second Run (1-basis accounts vs. 0-basis array)
# NOTE: Accepted on first Submit
# NOTE: Runtime 65 ms Beats 9.87%
# NOTE: Memory 49.34 MB Beats 18.51%
