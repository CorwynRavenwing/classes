class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:

        # instead of keeping track of the entire value of word[:i],
        # and taking the modulus of this increasingly-huge number
        # each time, use this Number Theory trick:

        # ABC % M
        # = ((AB) * 10 + C) % M
        # = (((AB) * 10) % M + C % M) % M
        # = ((AB % M) * 10 + C % M) % M
        # first section is prior answer;
        # simple multiplication and one-digit mod will be quick.

        answer = []
        # value = 0
        modulus = 0
        for D in word:
            # value *= 10
            # value += int(D)
            # divides = (value % m == 0)
            modulus *= 10
            modulus += (int(D) % m)
            modulus %= m
            divides = (modulus == 0)
            # print(f'{D} {modulus} {divides}')
            answer.append(
                (1 if divides else 0)
            )
        return answer
# NOTE: Runtime 308 ms Beats 33.77%
# NOTE: Memory 26.40 MB Beats 6.58%
