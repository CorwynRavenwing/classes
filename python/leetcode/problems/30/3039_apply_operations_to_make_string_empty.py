class Solution:
    def lastNonEmptyString(self, s: str) -> str:

        # counting method:

        print(f'{len(s)=}')
        counts = Counter(s)
        print(f'{counts=}')
        most_common = counts.most_common()
        print(f'{most_common=}')

        def most_common_filter(MC: Tuple[str,int]) -> List[str]:
            def most_common_filter_generator(MC: Tuple[str,int]) -> List[str]:
                maxSize = None
                for (value, count) in MC:
                    if maxSize is None:
                        yield value
                        maxSize = count
                    elif maxSize == count:
                        yield value
                    else:
                        return
            return tuple(most_common_filter_generator(MC))
        
        common = most_common_filter(most_common)
        print(f'{common=}')

        # smart cleanup:

        if len(common) == 1:
            return common[0]

        REV = lambda x: tuple(reversed(tuple(x)))

        sRev = REV(s)

        last_found = [
            (
                sRev.index(C),
                C
            )
            for C in common
        ]
        print(f'{last_found=}')
        
        answerRev = [
            C
            for (count, C) in sorted(last_found)
        ]
        print(f'{answerRev=}')

        return ''.join(
            REV(answerRev)
        )
# NOTE: This is the less brute-force method I wanted to write
# NOTE: Runtime 198 ms Beats 87.32%
# NOTE: Memory 22.52 MB Beats 17.39%

# NOTE: brute force version was:
# NOTE: Runtime 331 ms Beats 70.65%
# NOTE: Memory 22.30 MB Beats 81.52%

# NOTE: runtime 33% faster, surpassing 16% of other users, BUT:
# NOTE: uses a tiny bit more memory, falling behind over 50% of others

