class Solution:
    def longestBalanced(self, s: str) -> int:
        
        max_length = 0
        for i in range(len(s)):
            length = 0
            chars = Counter()
            for j in range(i, len(s)):
                length += 1
                B = s[j]
                chars[B] += 1
                counts = tuple(chars.values())
                countCounts = Counter(counts)
                L = len(countCounts)
                # print(f'[{i}:{j}] "{B}" {length} {counts} {L}')
                if L == 1:
                    # print(f'  (yes)')
                    max_length = max(length, max_length)

        return max_length

# NOTE: Acceptance Rate 69.6% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 13045 ms Beats 5.20%
# NOTE: Memory 19.48 MB Beats 22.02%
