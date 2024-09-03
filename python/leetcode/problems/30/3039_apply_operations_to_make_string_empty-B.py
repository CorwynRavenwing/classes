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

        # brute-force cleanup:

        Alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for C in Alphabet:
            if C in s:
                if C in common:
                    count = counts[C]
                    print(f'{C} common, {count=}')
                    s = s.replace(C, '', count - 1)
                else:
                    print(f'{C} delete')
                    s = s.replace(C, '')
            # else:
            #     print(f'{C} missing')

        return s
# NOTE: Runtime 331 ms Beats 70.65%
# NOTE: Memory 22.30 MB Beats 81.52%
# NOTE: there is still a brute-force section that I want to rewrite
