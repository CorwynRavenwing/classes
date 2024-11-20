class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        Len = len(arr)
        Half = Len // 2
        print(f'{Len=} {Half=}')
        answer = 0
        for (number, count) in Counter(arr).most_common():
            Len -= count
            answer += 1
            print(f'  {answer}: remove {count} "{number}" (-> {Len})')
            if Len <= Half:
                break
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 112 ms Beats 17.44%
# NOTE: Memory 40.21 MB Beats 24.08%
