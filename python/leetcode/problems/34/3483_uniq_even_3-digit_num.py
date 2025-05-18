class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        
        # we borrow some code from #2094:
        
        possible = []
        for i, A in enumerate(digits):
            # print(f"{i} ? ? | {A} ? ?")
            if A == 0:
                # print("  zero")
                continue
            for j, B in enumerate(digits):
                if i == j:
                    # print("  skip j")
                    continue
                # print(f"{i} {j} ? | {A} {B} ?")
                for k, C in enumerate(digits):
                    if i == k or j == k:
                        # print("  skip k")
                        continue
                    # print(f"{i} {j} {k} | {A} {B} {C}")
                    if C not in [0, 2, 4, 6, 8]:
                        # print("  odd")
                        continue
                    answer = (100 * A) + (10 * B) + C
                    # print(f"  {answer=}")
                    possible.append(answer)
        # print(f"{possible=}")
        possible = sorted(list(set(possible)))
        # print(f"{possible=}")
        return len(possible)

# NOTE: Acceptance Rate 66.1% (easy)

# NOTE: re-used entire previous version, with output format change
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 17 ms Beats 45.86%
# NOTE: Memory 17.74 MB Beats 87.95%
