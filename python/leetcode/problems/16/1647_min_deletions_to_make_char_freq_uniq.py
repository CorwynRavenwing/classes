class Solution:
    def minDeletions(self, s: str) -> int:
        
        counts = Counter(s)
        letter_counts = tuple(reversed(counts.most_common()))
        print(f'{letter_counts=}')

        answer = 0
        used_counts = set()
        for (letter, count) in letter_counts:
            print(f'{count} * "{letter}"')
            if count in used_counts:
                new_count = count
                while new_count in used_counts:
                    new_count -= 1
                    answer += 1
                print(f'  delete {count - new_count} "{letter}" -> {new_count}')
                if new_count:
                    # don't record freq of "0"
                    used_counts.add(new_count)
            else:
                used_counts.add(count)
        
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 66 ms Beats 79.58%
# NOTE: Memory 17.23 MB Beats 41.46%
