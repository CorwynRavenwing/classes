        def digits_to_int(digits: List[int]) -> int:
            answer = 0
            for D in digits:
                answer *= 10
                answer += D
            return answer

