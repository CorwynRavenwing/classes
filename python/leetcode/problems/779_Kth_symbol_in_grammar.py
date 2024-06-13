class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def inverse(i: int) -> int:
            return (
                0
                if i == 1
                else 1
            )
        
        def kthElement_index0(n: int, k: int, depth=0) -> int:
            margin = '  ' * depth
            print(margin + f'kthElement({n},{k})')
            # now n goes from 0
            # length of Nth grammar is now 2^N
            assert n >= 0
            assert 0 <= k <= 2 ** n

            # base case: 0th element of 0th grammar is 0.
            if n == 0 and k == 0:
                print(margin + f'= 0')
                return 0
            
            # Kth element of Nth grammar ==
            # examine (K//2)th element of (N-1)th grammar.
            prior = kthElement_index0(n - 1, k // 2, depth + 1)

            # if K is even: return same answer
            # if K is odd: return the opposite.
            answer = (
                prior
                if k % 2 == 0
                else inverse(prior)
            )
            print(margin + f'= {answer}')
            return answer
        
        def kthElement_index1(n: int, k: int) -> int:
            return kthElement_index0(n-1, k-1)

        return kthElement_index1(n, k)

