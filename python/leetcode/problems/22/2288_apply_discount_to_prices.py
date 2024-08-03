class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:

        words = sentence.split(' ')
        # print(f'{words=}')
        for i, W in enumerate(words):
            if W.startswith('$'):
                print(f'with dollar sign "{W}"')
                X = W[1:]
                digit_check = [
                    d.isdigit()
                    for d in list(X)
                ]
                if not len(X):
                    print(f'  Nothing after dollar sign, skipping')
                    continue
                elif all(digit_check):
                    print(f'  All digits, performing discount')
                    price = int(X)
                    price *= (100 - discount)
                    price /= 100
                    W = f'${price:.2f}'
                    print(f'    {W=}')
                    words[i] = W
                else:
                    print(f'  Some non-digits, skipping')
            # else:
            #     print(f'  Does not start with dollar-sign, skipping')
        
        return ' '.join(words)
# NOTE: Runtime 205 ms Beats 9.31%
# NOTE: Memory 18.77 MB Beats 45.21%
