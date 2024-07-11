class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        if len(arr) % 2 != 0:
            # cant divide into pairs
            return False

        if sum(arr) % k != 0:
            # sum(pairs) === sum(arr)
            # sum(each pair % k) --> sum(arr) % k
            return False
        
        modK = [
            A % k
            for A in arr
        ]
        print(f'{modK=}')
        Kcount = Counter(modK)
        print(f'{Kcount}')
        for A, Acount in Kcount.items():
            print(f'{A=} {Acount=}')
            B = (k - A) % k
            Bcount = Kcount[B]
            print(f'->{B=} {Bcount=}')
            if Acount != Bcount:
                return False
            if A == B:
                if Acount % 2 != 0:
                    return False
        return True

