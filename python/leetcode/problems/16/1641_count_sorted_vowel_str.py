class Solution:
    def countVowelStrings(self, n: int) -> int:

        @cache
        def CVS_with_min(n: int, minChar: str) -> int:
            print(f'CVS({n},"{minChar}")')
            answer = 0
            if n == 0:
                # one way to do 0 characters: [""]
                return 1
            for vowel in 'aeiou':
                if vowel < minChar:
                    continue
                answer += CVS_with_min(n - 1, vowel)
            return answer
        
        return CVS_with_min(n, 'a')

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 4 ms Beats 20.18%
# NOTE: Memory 17.14 MB Beats 6.22%
