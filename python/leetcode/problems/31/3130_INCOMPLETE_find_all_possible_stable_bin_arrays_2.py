class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        
        # we borrow some code from #3129
        
        # SHORTCUT: "each subarray of size greater than limit must contain both 0 and 1"
        # === "maximum run length of 0s or 1s is no more than limit"

        # SHORTCUT: for a combination of Z zeros and Y ones, there *cannot* be a run
        # of more than max(Y,Z): therefore a limit greater than that is irrelevant

        limit = min(
            limit,
            max(zero, one)
        )

        mod = 10 ** 9 + 7

        @cache
        def dp(zeros_remain: int, ones_remain: int, lastNum: int, countOfLastNum: int, d=0) -> int:

            margin = '  ' * d

            if countOfLastNum > limit:
                return 0
                
            if zeros_remain < 0 or ones_remain < 0:
                return 0
            
            if zeros_remain == ones_remain == 0:
                return 1
            
            # print(f'{margin}dp({zeros_remain},{ones_remain},{lastNum},{countOfLastNum})')

            answer = 0
            if lastNum is None or lastNum == 1:
                for i in range(1, min(zeros_remain, limit) + 1):
                    answer += (
                        dp(
                            zeros_remain - i,
                            ones_remain,
                            0,
                            i,
                            d+1
                        )
                    )
            if lastNum is None or lastNum == 0:
                for i in range(1, min(ones_remain, limit) + 1):
                    answer += (
                        dp(
                            zeros_remain,
                            ones_remain - i,
                            1,
                            i,
                            d+1
                        )
                    )
            # print(f'{margin}  {answer=}')
            return answer % mod

        answer = dp(zero, one, None, 0)

        return answer % mod

# NOTE: *memory* limit exceeded for huge inputs.
