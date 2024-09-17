
        def HHMM_to_minutes(HHMM: str) -> int:
            (HH, MM) = map(int, HHMM.split(':'))
            return HH * 60 + MM

