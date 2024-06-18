class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cashbox = {
            5: 0,
            10: 0,
            20: 0,
        }
        for B in bills:
            print(f"{cashbox}")
            cashbox[B] += 1
            cash_owed = B - 5
            print(f"  {B} ({cash_owed})")
            if cash_owed >= 10:
                if cashbox[10] >= 1:
                    cashbox[10] -= 1
                    cash_owed -= 10
                    print(f"    {1} * {10}")
            if cash_owed >= 5:
                fives_owed = cash_owed // 5
                if cashbox[5] >= fives_owed:
                    cashbox[5] -= fives_owed
                    cash_owed -= fives_owed * 5
                    print(f"    {fives_owed} * {5}")
            if cash_owed > 0:
                print(f"      STILL OWE {cash_owed}")
                print(f"{cashbox}")
                return False
        print("success")
        print(f"{cashbox}")
        return True

