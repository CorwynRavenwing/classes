class Solution:
    def romanToInt(self, s: str) -> int:
        
        conversions = (
            ('M', 1000),
            ('CM', 900),
            ('D',  500),
            ('CD', 400),
            ('C',  100),
            ('XC',  90),
            ('L',   50),
            ('XL',  40),
            ('X',   10),
            ('IX',   9),
            ('V',    5),
            ('IV',   4),
            ('I',    1),
        )
        answer = 0
        print(f"{s=} {answer=}")
        for (roman, value) in conversions:
            while s.startswith(roman):
                print(f"  {roman=} {value=}")
                answer += value
                skip = len(roman)
                s = s[skip:]
                print(f"{s=} {answer=}")

        return answer

