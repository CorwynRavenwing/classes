class Solution:
    def minimumOperations(self, num: str) -> int:
        
        # we want to start from the end instead
        numR = tuple(reversed(num))
        print(f'{numR=}')
        answers = []
        try:
            first0 = numR.index('0')
            try:
                first00 = numR.index('0', first0 + 1)
                print(f'Found {00} at {first0},{first00}')
                answers.append(first00)
            except ValueError:
                print(f"No 00's in number")

            try:
                first50 = numR.index('5', first0 + 1)
                print(f'Found {50} at {first0},{first50}')
                answers.append(first50)
            except ValueError:
                print(f"No 50's in number")
                
        except ValueError:
            first0 = None
            print(f"No 0's in number")
        
        try:
            first5 = numR.index('5')
            try:
                first25 = numR.index('2', first5 + 1)
                print(f'Found {25} at {first5},{first25}')
                answers.append(first25)
            except ValueError:
                print(f"No 25's in number")

            try:
                first75 = numR.index('7', first5 + 1)
                print(f'Found {75} at {first5},{first75}')
                answers.append(first75)
            except ValueError:
                print(f"No 75's in number")
                
        except ValueError:
            print(f"No 5's in number")
        
        if not answers:
            if first0 is None:
                # delete all numbers
                return len(num)
            else:
                # delete all but the single zero
                return len(num) - 1

        return min(answers) - 1
# NOTE: Accepted on first Submit
# NOTE: Runtime 27 ms Beats 100.00%
# NOTE: Memory 16.62 MB Beats 20.38%
