class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        count1 = Counter(nums1)
        # print(f'{count1=}')
        count2 = Counter(nums2)
        # print(f'{count2=}')
        
        def factors_of(N: int) -> List[int]:
            if N == 1:
                return [1]

            answers = []
            for D in range(1, N // 2 + 1):
                if N % D == 0:
                    Q = N // D
                    if D > Q:
                        break
                    answers.append(D)
                    if Q != D:
                        answers.append(Q)
            return answers

        hint1_F = Counter()
        for N, count in count2.items():
            hint1_F[N * k] += count
        # print(f'{hint1_F=}')
        hint1_F_set = set(hint1_F.keys())
        # print(f'{len(hint1_F_set)=}')

        answer = 0
        for N, count in sorted(count1.items()):
            # print(f'{N=} {count=}')
            factor_set = set(factors_of(N))
            intersect = factor_set & hint1_F_set
            if intersect:
                print(f'{N=} {count=} F={len(factor_set)} &={len(intersect)}')
            for D in intersect:
                print(f'  {D=} {hint1_F[D]=}')
                answer += count * hint1_F[D]

        return answer

# NOTE: Runtime 61 ms Beats 10.22%
# NOTE: Memory 16.60 MB Beats 64.05%
