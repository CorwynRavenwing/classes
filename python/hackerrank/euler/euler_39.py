def with_cache(fn):
    cache_data = {}

    def inner(x):
        if x in cache_data:
            R = cache_data[x]
            # print("#cache hit", x, R)
        else:
            R = fn(x)
            cache_data[x] = R
            # print("#cache miss", x, R)
        return R
    return inner

@with_cache
def integer_right_triangles(p):
    retval = []
    # a < b < c, therefore a is at most 1/3 of perimeter
    a_max = p // 3
    for a in range(1, a_max + 1):
        # a^2 + b^2 = c^2
        # a + b + c = p
        # c = p - (a+b)
        # a^2 + b^2 = (p - (a+b))^2
        # a^2 + b^2 = p^2 - 2p(a+b) + (a+b)^2
        # a^2 + b^2 = p^2 - 2pa - 2pb + a^2 + 2ab + b^2
        # cancel a^2 and b^2:
        # 0 = p^2 - 2pa - 2pb + 2ab
        # move B terms to left:
        # 2pb - 2ab = p^2 - 2pa
        # pb - ab = (1/2)p^2 - pa
        # b(p - a) = p(p/2 - a)
        # b = p(p/2 - a) / (p - a)
        if p == a:
            # print(f"#SKIP {a=} > {p=}")
            continue
        b = p * (p // 2 - a) // (p - a)
        if b < a:
            # print(f"#SKIP {a=} > {b=}")
            continue
        c = p - (a + b)
        if (a * a) + (b * b) == (c * c):
            point = (a, b, c)
            # print(f"#FOUND {point=}")
            retval.append(point)
    return retval

def euler_39(N):
    max_answer_val = 0
    max_answer_p = 0
    for p in range(N+1):
        L = integer_right_triangles(p)
        if len(L):
            print(f"#found {p=} {L=}")
        answer = len(L)
        if max_answer_val < answer:
            max_answer_val = answer
            max_answer_p = p
            print(f"#(new max) {p=} {answer} {L=}")
    print(f"#max: {max_answer_p} {max_answer_val}")
    return max_answer_p

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(euler_39(N))

