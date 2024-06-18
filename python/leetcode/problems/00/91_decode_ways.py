class Solution:
    def numDecodings(self, s: str) -> int:

        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        codes = {
            str(index + 1): letter
            for index, letter in enumerate(alphabet)
        }
        # print(f'{codes=}')
        # '26': 'Z' for example

        data = [None] * (len(s) + 1)
        for i in range(len(s) + 1):
            print(f'{i=}')
            if i == 0:
                data[i] = 1
                continue
            data[i] = 0
            prior_1 = s[i-1:i]
            print(f'  {prior_1=}')
            if prior_1 in codes:
                print(f'    match {codes[prior_1]} (+{data[i-1]})')
                data[i] += data[i-1]
            else:
                print(f'    no match')
            if i >= 2:
                prior_2 = s[i-2:i]
                print(f'  {prior_2=}')
                if prior_2 in codes:
                    print(f'    match {codes[prior_2]} (+{data[i-2]})')
                    data[i] += data[i-2]
                else:
                    print(f'    no match')
            print(f'    ={data[i]}')
            
        
        return data[len(s)]

