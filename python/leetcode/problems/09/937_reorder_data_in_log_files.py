class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        sortable = []
        for index, log in enumerate(logs):
            (identifier, contents) = log.split(' ', 1)
            firstChar = contents[0]
            logType = (
                '2:digit'
                if firstChar in '0123456789'
                else '1:letter'
            )
            print(f'{index=} {identifier=} {logType=} {contents=}')
            sortable.append(
                (
                    (
                        logType,
                        (
                            (contents, identifier)
                            if logType == '1:letter'
                            else (index, '')
                        ),
                    ),
                    log,
                )
            )
        print(f'{sortable=}')
        sortable.sort()

        answer = [
            log
            for order, log in sortable
        ]
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 96.76%
# NOTE: Memory 16.93 MB Beats 7.77%
