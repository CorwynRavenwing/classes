class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        counts = Counter(arr)
        by_freq = list(reversed(counts.most_common()))
        print(f'{k=}: {by_freq=}')

        while k and by_freq:
            (first_num, first_count) = by_freq[0]
            removed = min(k, first_count)
            print(f'{k=}: Remove {removed}/{first_count} "{first_num}"')
            k -= removed
            first_count -= removed
            if first_count:
                by_freq[0] = (first_num, first_count)
            else:
                del by_freq[0]

        print(f'{k=}: {by_freq=}')
        return len(by_freq)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 1222 ms Beats 5.08%
# NOTE: Memory 36.90 MB Beats 35.48%
