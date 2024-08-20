class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:

        def even_and_odd_counts(s: str) -> List[Dict[str,int]]:
            answer = [Counter(), Counter()]
            for i, char in enumerate(s):
                answer[i % 2][char] += 1
            return answer
        
        c1 = even_and_odd_counts(s1)
        c2 = even_and_odd_counts(s2)
        
        print(f'{c1=}')
        print(f'{c2=}')

        return c1 == c2

# NOTE: Accepted on first Submit
# NOTE: Runtime 334 ms Beats 5.15%
# NOTE: Memory 17.88 MB Beats 60.94%
