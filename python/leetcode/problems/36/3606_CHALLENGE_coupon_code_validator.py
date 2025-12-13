class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        
        legal_lines = {"electronics", "grocery", "pharmacy", "restaurant"}
        valid = []
        for (codeI, lineI, activeI) in zip(code, businessLine, isActive):
            print(f'{codeI},{lineI},{activeI}:')
            if codeI == "":
                print(f'  code blank')
                continue
            match = re.match(r'^[a-zA-Z0-9_]*$', codeI)
            if not match:
                print(f'  code invalid: "{codeI}"')
                continue
            if lineI not in legal_lines:
                print(f'  line invalid: {lineI}')
                continue
            if not activeI:
                print(f'  active false')
                continue
            record = (lineI, codeI)
            print(f'  +{record}')
            valid.append(record)
        
        valid.sort()
        answer = [
            codeI
            for (lineI, codeI) in valid
        ]

        return answer

# NOTE: Acceptance Rate 53.7% (easy)

# NOTE: Accepted on second Run (regex error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 19 ms Beats 15.76%
# NOTE: Memory 18.26 MB Beats 13.18%
