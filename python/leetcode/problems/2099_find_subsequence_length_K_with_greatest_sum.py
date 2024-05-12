class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:

        # addition is commutative, so "subsequence" == "pick any group"
        # but they need to be returned in order, so we note their index

        nums_by_value = sorted(
            [
                (N, i)
                for i, N in enumerate(nums)
            ]
            , reverse=True
        )
        print(f'{nums_by_value=}')
        best = nums_by_value[:k]
        print(f'{best=}')
        best_by_index = sorted(
            best,
            key=lambda x: x[1]
        )
        print(f'{best_by_index=}')
        answer = [
            N
            for (N, i) in best_by_index
        ]
        print(f'{answer=}')
        return answer

