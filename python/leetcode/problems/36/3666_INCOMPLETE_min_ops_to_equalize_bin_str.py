class Solution:
    def minOperations(self, s: str, k: int) -> int:
        
        counts = Counter(s)
        # print(f'{counts=}')

        zeros = counts['0']
        ones = counts['1']

        state = (0, (zeros, ones))
        # print(f'{state=}')

        queue = [state]
        seen = set()
        while queue:
            state = queue.pop(0)
            (distance, counts) = state
            if counts in seen:
                # print(f'  {state=} SEEN')
                continue
            else:
                seen.add(counts)

            (zeros, ones) = counts
            # print(f'{distance=} {zeros=} {ones=}')
            if zeros == 0:
                return distance
            
            for i in range(k + 1):
                j = k - i
                # print(f'  try [{i},{j}]:')
                if zeros < i:
                    # print(f'    no, I negative')
                    continue
                if ones < j:
                    # print(f'    no, J negative')
                    continue
                new_zeros = zeros - i + j
                new_ones = ones + i - j
                if new_zeros < 0 or new_ones < 0:
                    # print(f'    negative')
                    continue

                state = (
                    distance + 1,
                    (
                        new_zeros,
                        new_ones,
                    )
                )
                # print(f'    new {state=}')
                bisect.insort(queue, state)
        
        # failed
        return -1

# NOTE: Acceptance Rate 29.0% (HARD)

# NOTE: Time Limit Exceeded for large inputs (testcase 937)
