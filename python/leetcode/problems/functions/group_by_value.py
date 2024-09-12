        letters_and_counts = [
            (key, len(tuple(values)))
            for key, values in groupby(s)
        ]
        print(f'{letters_and_counts=}')

    # input: 11122222333311
    # output: [('1', 3), ('2', 5), ('3', 4), ('1', 2)]
    # note that similar letters are NOT merged, e.g. the '1's here
    # for the opposite behaviour, sort S before grouping,
