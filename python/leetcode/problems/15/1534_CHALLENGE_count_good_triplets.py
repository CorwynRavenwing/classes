class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        answer = 0
        for i, val_i in enumerate(arr):
            for j, val_j in enumerate(arr):
                if i >= j:
                    continue
                for k, val_k in enumerate(arr):
                    if j >= k:
                        continue
                    if abs(val_i - val_j) > a:
                        continue
                    if abs(val_j - val_k) > b:
                        continue
                    if abs(val_i - val_k) > c:
                        continue
                    answer += 1
        return answer

# NOTE: Acceptance Rate 82.2% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 395 ms Beats 15.32%
# NOTE: Memory 17.92 MB Beats 24.73%
