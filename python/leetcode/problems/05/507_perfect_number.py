class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        def divisors_of(num: int) -> List[int]:
            divisors = []
            sqrt = int(num ** 0.5)
            # print(f"{num=} {sqrt=}")
            for D in range(1, sqrt + 1):
                if num % D == 0:
                    Q = num // D
                    # print(f"  {D=} {Q=}")
                    divisors.append(D)
                    if D != Q:
                        divisors.append(Q)
            divisors.remove(num)
            return divisors

        divisors = divisors_of(num)
        # print(f'{num=} {divisors=} {sum(divisors)}')

        return (num == sum(divisors))

