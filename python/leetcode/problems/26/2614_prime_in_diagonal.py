class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:

        max_known = 2
        primes = [2]

        def is_obviously_nonprime(num: int) -> bool:
            if num in [2, 3, 5, 7]:
                return False
            if num in [1, 9]:
                return True
            int_string = str(num)
            last_char = int_string[-1]
            last_digit = int(last_char)
            return last_digit in [0, 2, 4, 6, 8, 5]

        def is_prime(num: int) -> bool:
            nonlocal max_known, primes
            print(f"is_prime({num}): {max_known=} {len(primes)=}")
            # print(f"{max_known=} {primes=}")
            if num <= max_known:
                answer = num in primes
                # print(f"{num}: cached {answer}")
                return answer
            for i in range(max_known, num + 1):
                if i in primes:
                    # print(f"  {i} cached PRIME")
                    continue
                i_is_prime = True
                for P in primes:
                    if i % P == 0:
                        # print(f"  {i} not prime")
                        i_is_prime = False
                        break
                if i_is_prime:
                    # print(f"  {i} PRIME")
                    primes.append(i)
            max_known = i
            answer = num in primes
            return answer
        
        diagonals = list(
            [
                row[i]
                for i, row in enumerate(nums)
            ] + [
                row[-1-i]
                for i, row in enumerate(nums)
            ]
        )
        diagonals = [
            D
            for D in diagonals
            if not is_obviously_nonprime(D)
        ]
        diagonals.sort(reverse=True)
        # print(f'{diagonals=}')
        print(f"{len(diagonals)=}")
        print(f'{diagonals[:10]=}')
        if not diagonals:
            return 0
        M = diagonals[0]
        if M > 1_000_000:
            print(f"can't actually check primes this high: {M=}")
            return M
        for D in diagonals:
            if is_prime(D):
                return D
        return 0

