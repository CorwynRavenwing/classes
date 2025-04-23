class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        def sum_of_digits(x: int) -> int:
            # 42 -> "42" -> ("4", "2") -> (4, 2) -> 6
            return sum(
                map(
                    int,
                    tuple(
                        str(x)
                    )
                )
            )

        digitGroups = {}
        for i in range(1, n + 1):
            total = sum_of_digits(i)
            print(f'{i} -> {total}')
            digitGroups.setdefault(total, [])
            digitGroups[total].append(i)
        print(f'{digitGroups=}')

        groupSizes = tuple(map(len, digitGroups.values()))
        print(f'{groupSizes=}')
        maxSize = max(groupSizes)
        maxGroups = [
            size
            for size in groupSizes
            if size == maxSize
        ]
        print(f'{maxGroups=}')

        return len(maxGroups)

# NOTE: Acceptance Rate 66.5% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 111 ms Beats 5.00%
# NOTE: Memory 18.74 MB Beats 7.50%
