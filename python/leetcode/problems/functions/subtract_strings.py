
    def subtractStrings(self, sOrig, sMinus) -> str:
        # 'ABCDE' - 'AD' = 'BCE'
        answer = ''
        for char in sOrig:
            if sMinus and sMinus[0] == char:
                sMinus = sMinus[1:]
                continue
            answer += char
        return answer


