class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        A = nums1[:m]
        B = nums2[:n]
        # print(f"{nums1=} {m=} {nums2=} {n=}")
        # print(f"{A=} {B=}")
        C = []
        while A and B:
            # print(f"AB {C=} {A=} {B=}")
            a = A[0]
            b = B[0]
            if a <= b:
                C.append(a)
                trash = A.pop(0)
            else:
                C.append(b)
                trash = B.pop(0)
        # print(f"AB {C=} {A=} {B=}")
        if A:
            C.extend(A)
            A = []
            # print(f"A {C=} {A=} {B=}")
        if B:
            C.extend(B)
            B = []
            # print(f"B {C=} {A=} {B=}")
        # print(f"X {C=} {A=} {B=}")

        for i, val in enumerate(C):
            # print(f"  {i=} {val=}")
            nums1[i] = val
        pass

