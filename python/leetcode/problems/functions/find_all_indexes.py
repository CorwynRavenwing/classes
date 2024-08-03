        def find_all_indexes(char: str, s: str) -> List[int]:
            answers = []
            startIndex = 0
            while True:
                try:
                    index = s.index(char, startIndex)
                except ValueError:
                    break
                answers.append(index)
                startIndex = index + 1
            return answers
        

