class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:

        barcode_counts = Counter(barcodes)
        # print(f'{barcode_counts=}')

        barcodes_by_count_Dict = {}
        max_count = 0
        for (val, count) in barcode_counts.items():
            barcodes_by_count_Dict.setdefault(count, [])
            barcodes_by_count_Dict[count].append(val)
            max_count = max(max_count, count)
        # print(f'{barcodes_by_count_Dict=}')
        # add entries for counts that are currently unused
        for count in range(max_count):
            barcodes_by_count_Dict.setdefault(count, [])
        barcodes_by_count = [
            [count, barcodes]
            for count, barcodes in barcodes_by_count_Dict.items()
        ]
        barcodes_by_count.sort(reverse=True)
        # print(f'{barcodes_by_count=}')

        def CBC() -> str:
            return '--'
            nonlocal barcodes_by_count
            max_show = 5
            count_by_count = [
                f'{count}: {len(barcodes)}'
                for (count, barcodes) in barcodes_by_count
                if barcodes
            ]
            count_string = ", ".join(count_by_count[:max_show])
            elipsis = " ..." if len(count_by_count) > max_show else ""
            return f'<{count_string}{elipsis}>'
        
        # print(f'begin: {CBC()}')

        prior = -999    # guaranteed not in list
        answer = []
        while barcodes_by_count:
            next_count_pos = 0
            (next_count, barcodes) = barcodes_by_count[next_count_pos]
            if not len(barcodes):
                # print(f'  No barcodes with count {next_count}')
                del barcodes_by_count[next_count_pos]
                continue
            next_barcode_pos = 0
            next_val = barcodes[next_barcode_pos]
            # print(f'{next_val}: {next_count}')
            if next_count == 0:
                print(f'  DONE')
                break
            if next_val == prior:
                # print(f'  same as prior: next')
                if len(barcodes) > 1:
                    next_barcode_pos = 1
                    next_val = barcodes[next_barcode_pos]
                else:
                    while True:
                        next_count_pos += 1
                        (next_count, barcodes) = barcodes_by_count[next_count_pos]
                        if len(barcodes):
                            next_barcode_pos = 0
                            next_val = barcodes[next_barcode_pos]
                            # print(f'{next_val}: {next_count}')
                            break
                        else:
                            # print(f'No barcodes at count {next_count}: continue')
                            if next_count == 0:
                                print(f'ERROR: reached count zero!')
                                return [-999]
            
            # print(f'add {next_val}: {next_count}')
            prior = next_val
            answer.append(next_val)
            # print(f'- {barcodes_by_count[next_count_pos][1]}')
            barcodes_by_count[next_count_pos][1].remove(next_val)
            # print(f'= {barcodes_by_count[next_count_pos][1]}')
            # print(f'+ {barcodes_by_count[next_count_pos + 1][1]}')
            barcodes_by_count[next_count_pos + 1][1].append(next_val)
            # print(f'= {barcodes_by_count[next_count_pos + 1][1]}')

            # print(f'add {next_val}: {next_count} {CBC()}')
            # print(f'add {next_val}: {next_count} {barcode_counts}')

        return answer

