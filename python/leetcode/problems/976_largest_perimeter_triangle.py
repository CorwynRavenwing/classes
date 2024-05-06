IN PROGRESS

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        def legalTriangle(A: int, B: int, C: int) -> int:
            # print(f"({A},{B},{C})")
            if A + B <= C:
                return False
            # any other rules I'm missing?
            return True

        nums.sort(reverse=True)
        max_answer = 0
        A_seen = []
        for i, A in enumerate(nums):
            print(f"{i} ? ? | {A} ? ?")
            if A in A_seen:
                # print(f"  seen {A=}")
                continue
            A_seen.append(A)
            next3 = nums[i:i+3]
            if len(next3) < 3:
                print(f"  A AT END")
                break
            if sum(next3) <= max_answer:
                print(f"  A TOO SMALL {next3}={sum(next3)}")
                break
            B_seen = []
            for j, B in enumerate(nums):
                if j <= i:
                    # print("    --")
                    continue
                # print(f"{i} {j} ? | {A} {B} ?")
                if B in B_seen:
                    # print(f"    seen {B=}")
                    continue
                B_seen.append(B)
                next2 = nums[j:j+2]
                if len(next2) < 2:
                    print(f"  B AT END")
                    break
                if A + sum(next2) <= max_answer:
                    print(f"  B TOO SMALL {A}+{next2}={A+sum(next2)}")
                    break
                C_seen = []
                for k, C in enumerate(nums):
                    if k <= j:
                        # print("      --")
                        continue
                    # print(f"{i} {j} {k} | {A} {B} {C}")
                    if C in C_seen:
                        # print(f"      seen {C=}")
                        continue
                    answer = A+B+C
                    if answer <= max_answer:
                        print(f"  C TOO SMALL {A}+{B}+{C}={answer}")
                        break
                    C_seen.append(C)
                    if legalTriangle(C, B, A):
                        print(f"  T=({A},{B},{C}) Size={answer}")
                        max_answer = max(max_answer, answer)
        return max_answer

IN PROGRESS
