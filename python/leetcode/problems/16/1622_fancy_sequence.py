
# Binary exponentiation
def power(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result
    
# function to calculate GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modInverse(b, m):
    return power(b, m - 2, m)
    
def modDivide(a, b, m):
    # Division not possible
    if b == 0 or gcd(b, m) != 1:
        return -1
    inv = modInverse(b, m)
    return (a * inv) % m

MOD = 10 * 9 + 7

class Fancy:

    def __init__(self):
        self.seq = []
        self.mult = 1
        self.add = 0

    def append(self, val: int) -> None:
        val -= self.add
        val = modDivide(val, self.mult, MOD)
        self.seq.append(val)
        return

    def addAll(self, inc: int) -> None:
        self.add += inc
        return

    def multAll(self, m: int) -> None:
        self.mult *= m
        self.add *= m
        # c(ax+b) = acx + bc
        return

    def getIndex(self, idx: int) -> int:
        # try:
        answer = self.seq[idx]
        # except ValueError:
            # answer = -1
        return answer % MOD

# NOTE: Acceptance Rate 22.1% (HARD)

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)

# NOTE: wrong answer for some inputs
