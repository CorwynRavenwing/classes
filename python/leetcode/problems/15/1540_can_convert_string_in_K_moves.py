class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:

        if len(s) != len(t):
            print(f'Now that is just cheating: S and T are different lengths')
            return False
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        code = {L: i for i, L in enumerate(alphabet)}
        changes = [
            (code[Tch] - code[Sch]) % 26
            for (Sch, Tch) in zip(s, t)
            if Sch != Tch
        ]
        # print(f'{changes=}')
        changeCounts = Counter(changes)
        while changeCounts:
            # print(f'{k=} {changeCounts=}')
            if k < max(changeCounts):
                print(f'  Ran out of K')
                return False
            for L, count in changeCounts.items():
                # print(f'  {L}')
                changeCounts[L] -= 1
            changeCounts = {
                L: count
                for L, count in changeCounts.items()
                if count
            }
            k -= 26
        return True

