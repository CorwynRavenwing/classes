class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(P: str) -> bool:
            return list(P) == list(reversed(list(P)))
        
        # data[N] contains "list of all possible partitionings
        #   of string s[:N]"
        # Which means that data[0] is "all partitionings of the
        #   substring ENDING at index 0, i.e. the empty string"
        # The answer will be in data[len(s)]
        data = {
            0: []
        }

        # print(f'{s}')
        # print(f'{s[:len(s)]}')
        
        for j in range(1,len(s)+1):
            partial = []
            for i in range(0,j):
                fragment = s[i:j]
                prior = data[i]
                is_pal = is_palindrome(fragment)
                print(f'{i=} {j=} {fragment} {is_pal} {prior=}')
                if not is_pal:
                    continue
                if prior:
                    new_record = [
                        P + [fragment]
                        for P in prior
                    ]
                else:
                    new_record = [[fragment]]
                print(f'  {new_record=}')
                partial.extend(new_record)
            data[j] = partial
        
        return data[len(s)]

