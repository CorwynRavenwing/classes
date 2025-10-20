class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        
        def partitions_leftwards(s: str) -> List[int]:
            # nonlocal k
            answer = []
            count = Counter()
            total = 1
            for char in s:
                count[char] += 1
                if len(count) > k:
                    total += 1
                    count = Counter()
                answer.append(total)
            return tuple(answer)

        def partitions_rightwards(s: str) -> List[int]:
            REV = lambda L: tuple(reversed(L))
            rev_s = REV(s)
            rev_answer = partitions_leftwards(rev_s)
            answer = REV(rev_answer)
            return answer

        prefix = partitions_leftwards(s)
        suffix = partitions_rightwards(s)
        print(f'{prefix=}')
        print(f'{suffix=}')

        return -99999

# NOTE: Acceptance Rate 33.5% (HARD)
