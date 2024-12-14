class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.count1 = Counter(nums1)
        self.count2 = Counter(nums2)
        self.nums2 = nums2
        return

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        self.nums2[index] += val
        new_val = self.nums2[index]
        self.count2[old_val] -= 1
        self.count2[new_val] += 1
        print(f'add({index},{val}): {old_val} -> {new_val}')
        return

    def count(self, tot: int) -> int:
        print(f'count({tot})')
        answer = 0
        for N1, C1 in self.count1.items():
            N2 = tot - N1
            C2 = self.count2[N2]
            if C2:
                C = C1 * C2
                answer += C
                print(f'  {N1}+{N2}: {C}=({C1}*{C2})')
        print(f'->{answer}')
        return answer

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

# NOTE: Accepted on second Run (bad count logic)
# NOTE: Accepted on first Submit
# NOTE: Runtime 377 ms Beats 28.13%
# NOTE: Memory 48.58 MB Beats 26.08%
