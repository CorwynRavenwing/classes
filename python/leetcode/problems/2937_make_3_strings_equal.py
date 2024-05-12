class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        oper = 0
        print(f'{oper=} {s1=} {s2=} {s3=}')
        length = min(len(s1), len(s2), len(s3))
        while len(s1) > length:
            oper += 1
            s1 = s1[:-1]
            print(f'{oper=} {s1=} {s2=} {s3=}')
        while len(s2) > length:
            oper += 1
            s2 = s2[:-1]
            print(f'{oper=} {s1=} {s2=} {s3=}')
        while len(s3) > length:
            oper += 1
            s3 = s3[:-1]
            print(f'{oper=} {s1=} {s2=} {s3=}')
        while s1 != s2 or s2 != s3 or s1 != s3:
            oper += 1
            s1 = s1[:-1]
            oper += 1
            s2 = s2[:-1]
            oper += 1
            s3 = s3[:-1]
            print(f'{oper=} {s1=} {s2=} {s3=}')
        if not s1 or not s2 or not s3:
            return -1
        else:
            return oper

