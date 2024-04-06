
from typing import List

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

coins: List[int] = []

@with_cache
def hard(T):
    (N, coin) = T
    print(f"#hard({N},{coin})")
    max_this_coin = N // coin
    coin_index = coins.index(coin)
    next_coin = (
        coins[coin_index + 1]
        if coin_index + 1 < len(coins)
        else None
    )
    possible = []
    for this_coin in reversed(range(max_this_coin + 1)):
        print(f"#{this_coin} * {coin} -> {N - (coin * this_coin)}, {next_coin}")
        possible.append(
            easy(N - (coin * this_coin), next_coin)
        )
        print(f"# -> {possible=}")
    # possible = [
    #     easy(N - (coin * this_coin), next_coin)
    #     for this_coin in reversed(range(max_this_coin + 1))
    # ]
    return sum(possible)

def easy(N, coin):
    print(f"#easy({N},{coin})")
    if N == 0:
        print("# -> 1")
        return 1
    if coin > N:
        print(f"# coin {coin} -> {N}")
        coin = N
    if coin == 1:
        print("# -> 1")
        return 1
    print(f"# -> hard({N},{coin})")
    return hard(
        (N, coin)
    )
    pass

def euler_31(N):
    global coins
    coins = tuple(reversed(range(1, N+1)))
    print(f"#{coins=}")
    return easy(N, coins[0])

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_31(N))

