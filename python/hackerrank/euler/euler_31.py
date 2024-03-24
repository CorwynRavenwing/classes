
def with_cache(fn):
    cache_data = {}

    def inner(x):
        if x in cache_data:
            R = cache_data[x]
            print("#cache hit", x, R)
        else:
            R = fn(x)
            cache_data[x] = R
            print("#cache miss", x, R)
        return R
    return inner

coins = [200, 100, 50, 20, 10, 5, 2, 1]

@with_cache
def hard(T):
    (pence, coin) = T
    print(f"#hard({pence},{coin})")
    max_this_coin = pence // coin
    coin_index = coins.index(coin)
    next_coin = (
        coins[coin_index + 1]
        if coin_index + 1 < len(coins)
        else None
    )
    possible = [
        easy(pence - (coin * this_coin), next_coin)
        for this_coin in range(max_this_coin + 1)
    ]
    return sum(possible)

def easy(pence, coin):
    print(f"#easy({pence},{coin})")
    if pence == 0:
        return 1
    if coin == 1:
        return 1
    return hard(
        (pence, coin)
    )
    pass

def euler_31(N):
    return easy(N, coins[0])

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_31(N))

