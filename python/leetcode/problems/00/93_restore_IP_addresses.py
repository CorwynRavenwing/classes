class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        possible = [
            (
                (),   # numbers parsed out so far
                s,    # string left to parse
            )
        ]
        answers = []
        while possible:
            P = possible.pop(0)
            (nums, to_parse) = P
            if to_parse == '':
                if len(nums) == 4:
                    print(f'FOUND {nums}')
                    answers.append(
                        '.'.join(nums)
                    )
                    continue
                else:
                    print(f'FAIL {nums} len={len(nums)} {to_parse=}')
                    continue
            if len(nums) == 4:
                # fail because there is something left to parse
                print(f'FAIL {nums} len={len(nums)} {to_parse=}')
                continue
            if len(nums) > 4:
                print(f'FAIL {nums} len={len(nums)} {to_parse=}')
                continue
            
            for digits in range(1, 3+1):
                # print(f'  {digits=}')
                attempt = to_parse[:digits]
                remain = to_parse[digits:]
                print(f'  {attempt=} len={len(attempt)}')
                if len(attempt) != digits:
                    print(f'    off the end')
                    continue
                if attempt.startswith('0') and attempt != '0':
                    print(f'    no leading zeros')
                    continue
                if 0 <= int(attempt) <= 255:
                    print(f'    found digit')
                    possible.append(
                        (
                            nums + (attempt,),
                            remain,
                        )
                    )
                else:
                    print(f'    OOB')
        return answers

