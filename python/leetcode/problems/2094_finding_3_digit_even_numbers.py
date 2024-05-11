class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

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
        return possible

