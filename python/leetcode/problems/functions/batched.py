
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

