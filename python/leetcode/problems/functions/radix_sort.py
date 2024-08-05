
        # Radix Sort Algorithm:

        nums = [
            '123', '145', '456', '902', '219'
        ]

        def radix_sort_nums(radix: int) -> None:
            nonlocal nums
            all_digits = '0123456789'
            print(f'Called radix_sort_nums({radix})')
            buckets = {}
            for D in all_digits:
                buckets.setdefault(D, [])
            for N in nums:
                digit = N[-radix]   # i.e. radix=1 -> last character, etc.
                buckets[digit].append(N)
                print(f'  Bucket "{digit}" gets {N}')
            nums = [
                element
                for D in all_digits
                for element in buckets[D]
            ]
            print(f'    new order: {nums=}')

