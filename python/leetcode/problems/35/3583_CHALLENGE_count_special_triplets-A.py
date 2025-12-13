class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        
        mod = 10 ** 9 + 7

        def freq_previous(nums: List[int]) -> List[Dict[int,int]]:
            freq = Counter()
            answer = [freq]
            # print(f'begin: {answer=}')
            for N in nums:
                # freq += Counter([N])  # NOT "+=", which behaves differently
                freq = freq + Counter([N])  # NOT "+=", which behaves differently
                answer.append(freq)
                # print(f'{N=}: {answer=}')
            del answer[-1]
            # answer = tuple([
            #     dict(C)
            #     for C in answer
            # ])
            # print(f'done: {answer=}')
            return answer
        
        def freq_next(nums: List[int]) -> List[Dict[int,int]]:
            REV = lambda L: list(reversed(L))
            r_nums = REV(nums)
            r_answer = freq_previous(r_nums)
            answer = REV(r_answer)
            return answer
        
        freqPrev = freq_previous(nums)
        freqNext = freq_next(nums)

        # print(f'{freqPrev=}')
        # print(f'{freqNext=}')

        answer = 0
        for (aFreq, b, cFreq) in zip(freqPrev, nums, freqNext):
            b2 = b * 2
            a = aFreq[b2]
            c = cFreq[b2]
            prod = a * c
            # print(f'{b=} {b2=} {a=} {c=} {prod=}')
            answer += prod
            answer %= mod

        return answer % mod

# NOTE: Acceptance Rate 37.9% (medium)

# NOTE: Memory Exceeded and/or Time Limit Exceeded for large inputs
