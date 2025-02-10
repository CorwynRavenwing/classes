        def find_all_indexes(needle: str, haystack: str) -> List[int]:
            answers = []
            startIndex = 0
            while True:
                try:
                    index = haystack.index(needle, startIndex)
                except ValueError:
                    break
                answers.append(index)
                startIndex = index + 1
            return answers
        

