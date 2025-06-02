class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        answer = [1] * len(ratings)
        print(f'pass 0: {answer}')

        def clean_answer(input_answer: List[int], input_ratings: List[int]) -> List[int]:
            # data = tuple(zip(input_answer, input_ratings))
            # print(f'  DEBUG: {data=}')

            output_answer = list(input_answer)
            for i in range(1, len(output_answer)):
                (A_prev, A_this) = output_answer[i - 1:i + 1]
                (R_prev, R_this) = input_ratings[i - 1:i + 1]
                if R_this > R_prev:
                    output_answer[i] = max(A_this, A_prev + 1)
                    print(f'  [{i}]: bump {A_this} to {output_answer[i]} b/c {R_this} > {R_prev}')
            print(f'  DEBUG: output={output_answer}')
            return output_answer

        answer = clean_answer(answer, ratings)
        print(f'pass 1: {answer}')

        R = lambda L: tuple(reversed(L))
        answer = R(clean_answer(R(answer), R(ratings)))

        print(f'pass 2: {answer}')

        return sum(answer)

# NOTE: Acceptance Rate 44.8% (HARD)

# NOTE: Accepted on second Submit (edge case 1 2 87 87 87 2 1)
# NOTE: Runtime 130 ms Beats 5.03%
# NOTE: Memory 20.68 MB Beats 5.22%
