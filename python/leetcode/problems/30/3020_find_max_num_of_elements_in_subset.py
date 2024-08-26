class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        Lookup = set(nums)
        counts = Counter(nums)
        seen = set()
        answers = []
        for i in sorted(Lookup):
            if i in seen:
                continue
            else:
                seen.add(i)
            C = counts[i]
            if i == 1:
                if C % 2 == 0:
                    # even: need next-lower odd number
                    C -= 1
                print(f'  Answers[{i}]: {C}')
                answers.append(C)
                continue
            A = 1
            N = i
            while True:
                print(f'{A=} {N=} {C=}')
                if C < 2:
                    print(f'  {C=} < 2')
                    break
                N = N * N   # square the value
                if N not in Lookup:
                    print(f'  {N=} not in Lookup')
                    break
                seen.add(N)
                C = counts[N]
                A += 2
                print(f'  Answers[{i}]: {A}')
            answers.append(A)
            
        return max(answers)

# NOTE: Accepted on first Submit
# NOTE: Runtime 961 ms Beats 24.68%
# NOTE: Memory 31.26 MB Beats 9.49%
