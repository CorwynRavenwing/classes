
mod_10_chars = 10_000_000_000
def N_pow_N_mod_10_chars(n):
    retval = 1
    for i in range(n):
        retval *= n
        retval %= mod_10_chars
        # print(f"#n_pow_n({n}):{retval}")
    return retval

def sum_N_pow_N_mod(N):
    retval = 0
    for n in range(1, N+1):
        retval += N_pow_N_mod_10_chars(n)
        retval %= mod_10_chars
        # print(f"#sum_n_pow_n({N}):{retval}")
    return retval

def euler_48(N):
    return sum_N_pow_N_mod(N)

N = int(input().strip())
print(euler_48(N))

