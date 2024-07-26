class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:

        # batched() comes standard in python 3.12
        # unfortunately, leetcode uses python 3.11.9 as of right now
        # using a recipe from the itertools module, found at:
        # https://docs.python.org/3/library/itertools.html#itertools-recipes
        def batched(iterable, n):
            "Batch data into lists of length n. The last batch may be shorter."
            # batched('ABCDEFG', 3) --> ABC DEF G
            it = iter(iterable)
            while True:
                batch = list(islice(it, n))
                if not batch:
                    return
                yield batch
                
        # print(f'{sys.version=}')
        columns = len(encodedText) // rows
        print(f'{columns=} = len={len(encodedText)} / {rows=}')
        block = list(batched(encodedText, columns))
        for R, row in enumerate(block):
            print(f'{R=}: ' + ' '.join(row))
        coords = [
            (R, R + C)
            for C in range(columns)
            for R in range(rows)
            if R + C < columns
        ]
        # print(f'{coords=}')
        plainTextList = [
            block[R][C]
            for (R, C) in coords
        ]
        while plainTextList and plainTextList[-1] == ' ':
            del plainTextList[-1]
        # print(f'{plainTextList=}')
        plainText = ''.join(plainTextList)
        # print(f'{plainText=}')
        return plainText

