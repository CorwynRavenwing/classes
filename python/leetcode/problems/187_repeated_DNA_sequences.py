class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        output = []
        for i in range(len(s) - 10 + 1):
            fragment = s[i:i + 10]
            # print(f'{fragment=} {len(fragment)}')
            if fragment not in output:
                if fragment in s[i+1:]:
                    print(f'  found: "{fragment}"')
                    output.append(fragment)
        return output

