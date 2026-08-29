class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:

        raw_freq = Counter(s)

        freq = Counter()
        odd = ''
        for (letter, count) in raw_freq.items():
            print(f'{letter=} {count=}')

            half = count // 2

            if half:
                print(f'  {half=}')
                freq[letter] = half
                count -= (2 * half)

            if count:
                if odd:
                    print(f'  MULTIPLE ODD: FAIL {odd=} {letter=}')
                    return ''
                else:
                    odd = letter
                    print(f'  {odd=}')
        
        print(f'{freq=} {odd=}')

        # we borrow some code from #3720:

        # this is now a generator
        def DP_eq(
            i: int,
            freq: Dict[str,int],
            odd: str,
            X: str,
            avail: List[str]
        ) -> List[str]:
            if avail:
                if X not in avail:
                    # yield None
                    return

                new_freq = freq - Counter(X)
                for remainder in DP(
                    i + 1,
                    new_freq,
                    odd
                ):
                    print(f'DP_EQ: {remainder=}')
                    if remainder is None:
                        continue

                    yield X + remainder + X

            else:
                # center
                if X != odd:
                    # yield None
                    return
                print(f'DP_EQ: {odd=}')
                yield odd
                return

        # this is now a generator
        def DP_gt(
            i: int,
            freq: Dict[str,int],
            odd: str,
            X: str,
            avail: List[str]
        ) -> List[str]:
            if avail:
                greater = {
                    V
                    for V in avail
                    if V > X
                }
                print(f'DP_GT: {greater=}')
                if not greater:
                    # yield None
                    return

                Y = min(greater)
                print(f'DP_GT: {Y=}')
                new_freq = freq - Counter(Y)
                remainder = [
                    value * count
                    for value, count in new_freq.items()
                ]
                print(f'DP_EQ: {remainder=}')
                remainder = ''.join(sorted(remainder))
                print(f'DP_EQ: {remainder=}')

                rev_remainder = ''.join(reversed(remainder))

                yield Y + remainder + odd + rev_remainder + Y
                return
            
            else:
                # center
                if odd == '':
                    yield ''
                    return
                if odd <= X:
                    # yield None
                    return
                print(f'DP_EQ: {odd=}')
                yield odd
                return

        # this is now a generator
        def DP(
            i: int,
            freq: Dict[str,int],
            odd: str
        ) -> List[str]:
            print(f'DP({i},{freq}) ?')

            try:
                X = target[i]
            except IndexError:
                return None
            avail = set(freq.keys())
            print(f'  {X=} {avail=}')

            # try Equals
            for answer_eq in DP_eq(i, freq, odd, X, avail):
                print(f'DP({i},{freq}) {answer_eq=}')
                if answer_eq is not None:
                    yield answer_eq

            # try Greater
            for answer_gt in DP_gt(i, freq, odd, X, avail):
                print(f'DP({i},{freq}) {answer_gt=}')
                if answer_gt is not None:
                    yield answer_gt

            return

        for answer in DP(0, freq, odd):
            print(f'{answer=}')
            if answer is None:
                print(f'  NONE')
                continue
            if answer > target:
                print(f'  FOUND')
                return answer
            print(f'  TOO SMALL')

        print(f'FAIL')
        return ''

# NOTE: Acceptance Rate 27.8% (HARD)

# NOTE: re-used lots of code from prior version; had to turn it into a generator
# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (edge cases)
# NOTE: Runtime 208 ms Beats 17.39%
# NOTE: Memory 20.92 MB Beats 7.25%
