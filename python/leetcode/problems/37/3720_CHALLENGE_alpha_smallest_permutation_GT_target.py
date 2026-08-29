class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:

        def DP_eq(
            i: int,
            freq: Dict[str,int],
            X: str,
            avail: List[str]
        ) -> str:
            if X not in avail:
                return None
            print(f'DP_EQ: equal={X}')
            new_freq = freq - Counter(X)
            remainder = DP(
                i + 1,
                new_freq
            )
            print(f'DP_EQ: {remainder=}')
            if remainder is None:
                return None
            
            return X + remainder

        def DP_gt(
            i: int,
            freq: Dict[str,int],
            X: str,
            avail: List[str]
        ) -> str:
            greater = {
                V
                for V in avail
                if V > X
            }
            print(f'DP_GT: {greater=}')
            if not greater:
                return None
            
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

            return Y + remainder

        def DP(i: int, freq: Dict[str,int]) -> str:
            print(f'DP({i},{freq}) ?')

            try:
                X = target[i]
            except IndexError:
                return None     # was ''
            avail = set(freq.keys())
            print(f'  {X=} {avail=}')
            
            # try Equals
            answer_eq = DP_eq(i, freq, X, avail)
            print(f'DP({i},{freq}) {answer_eq=}')
            if answer_eq is not None:
                # if it's not null, it's lower than answer_gt
                if (i != 0) or (answer_eq > target):
                    return answer_eq
                    # if invalid 0th answer, fall through:

            # try Greater
            answer_gt = DP_gt(i, freq, X, avail)
            print(f'DP({i},{freq}) {answer_gt=}')
            if answer_gt is not None:
                # if it's not null, it's the best answer
                return answer_gt

            return None
        
        freq = Counter(s)

        answer = DP(0, freq)
        if answer is None:
            return ''
        
        return answer

# NOTE: Acceptance Rate 27.2% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted after several Submits (edge cases)
# NOTE: Runtime 223 ms Beats 5.26%
# NOTE: Memory 21.47 MB Beats 6.58%
