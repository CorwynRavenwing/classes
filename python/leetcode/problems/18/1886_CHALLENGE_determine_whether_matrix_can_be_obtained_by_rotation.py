class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        TUP = lambda G: tuple(map(tuple, G))
        mat = TUP(mat)
        target = TUP(target)

        INV = lambda G: tuple(map(tuple, zip(*G)))
        print(f'{INV(mat)=}')

        REV_L = lambda L: tuple(reversed(L))
        # print(f'{REV_L(mat[0])=}')

        REV = lambda G: tuple(map(REV_L, G))
        print(f'{REV(mat)=}')

        ROT = lambda G: REV(INV(G))
        print(f'{ROT(mat)=}')

        # tester = [
        #     ["A", "B", "C"],
        #     ["D", "E", "F"],
        #     ["G", "H", "I"],
        # ]
        # print(f'{INV(tester)=}')
        # print(f'{REV(tester)=}')
        # print(f'{ROT(tester)=}')

        if mat == target:
            return True
        
        check = mat
        for i in range(4):
            check = ROT(check)
            print(f'{check=} {target=}')
            if check == target:
                return True
        
        return False

# NOTE: Acceptance Rate 59.4% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 14.06%
# NOTE: Memory 19.48 MB Beats 24.35%
