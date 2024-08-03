class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:

        # since tiles are guaranteed to be non-overlapping,
        # we can merge adjacent tile sets to simplify the problem:
        tiles.sort()
        # print(f'sorted {tiles=}')
        for i in range(1, len(tiles)):
            (thisBegin, thisEnd) = tiles[i]
            (prevBegin, prevEnd) = tiles[i - 1]
            if thisBegin == prevEnd + 1:
                # print(f'Merge tiles {i-1},{i}')
                tiles[i] = [prevBegin, thisEnd]
                tiles[i - 1] = None
        while None in tiles:
            tiles.remove(None)
        # print(f'{tiles[:4]=}')
        precomputeTileSizes = [
            End - Begin + 1
            for (Begin, End) in tiles
        ]
        # print(f'{precomputeTileSizes[:10]=}')
        prefixSumsOfTileSizes = tuple(accumulate(precomputeTileSizes))
        # print(f'{prefixSumsOfTileSizes[:10]=}')

        # print(f'new {tiles=}')
        tile_beginnings = [
            Begin
            for (Begin, End) in tiles
        ]
        # print(f'{tile_beginnings=}')
        rug_starts_overlapping_T_B = [
            (RugEnd - carpetLen + 1)
            for RugEnd in tile_beginnings
        ]
        # print(f'temp {rug_starts_overlapping_T_B=}')
        rug_starts_overlapping_T_B = [
            RugStart
            for RugStart in rug_starts_overlapping_T_B
            if RugStart > 0
        ]
        # print(f'{rug_starts_overlapping_T_B=}')
        relevant_beginnings = sorted(set(tile_beginnings + rug_starts_overlapping_T_B))
        # print(f'{relevant_beginnings=}')

        # if len(tiles) > 1000:
        #     return -888

        answers = []
        for RugStart in relevant_beginnings:
            RugEnd = RugStart + carpetLen - 1
            # print(f'Try {RugStart}:{RugEnd}')
            overlapping_tiles = []
            leftEndPoint = [RugStart, 0]
            leftIndex = bisect_left(tiles, leftEndPoint)
            if leftIndex > 0:
                (BeginPrev, EndPrev) = tiles[leftIndex - 1]
                if (BeginPrev <= RugStart <= EndPrev):
                    # print(f'  L-: {tiles[leftIndex-1]} overlaps {RugStart}: use instead')
                    overlapping_tiles.append(tiles[leftIndex - 1])
                else:
                    (Begin, End) = tiles[leftIndex]
                    if (Begin <= RugStart <= End):
                        # print(f'  L+: {tiles[leftIndex]} overlaps {RugStart}: use that')
                        overlapping_tiles.append(tiles[leftIndex])
                        leftIndex += 1
                    # else:
                    #     # print(f'  L: {tiles[leftIndex]} does not overlap {RugStart}: keep')
            else:
                (Begin, End) = tiles[leftIndex]
                if (Begin <= RugStart <= End):
                    # print(f'  L+: {tiles[leftIndex]} overlaps {RugStart}: use that')
                    overlapping_tiles.append(tiles[leftIndex])
                    leftIndex += 1
                # else:
                #     # print(f'  L: {tiles[leftIndex]} does not overlap {RugStart}: keep')
            rightEndPoint = [RugEnd, float('inf')]
            rightIndex = bisect_right(tiles, rightEndPoint) - 1
            (Begin, End) = tiles[rightIndex]
            if (Begin <= RugEnd <= End):
                # print(f'  R-: {tiles[rightIndex]} overlaps {RugEnd}: use that')
                overlapping_tiles.append(tiles[rightIndex])
                rightIndex -= 1
            # else:
            #     # print(f'  R: {tiles[rightIndex]} does not overlap {RugEnd}: keep')
            # if leftIndex > rightIndex:
            #     # print(f'  L=[{leftIndex}]: Out of order')
            #     # print(f'  R=[{rightIndex}]: Out of order')
            # else:
            #     if leftIndex < len(tiles):
            #         # print(f'  L=[{leftIndex}]: {tiles[leftIndex]}')
            #     else:
            #         # print(f'  L=[{leftIndex}]: OOB')
            #     if rightIndex < len(tiles):
            #         # print(f'  R=[{rightIndex}]: {tiles[rightIndex]}')
            #     else:
            #         # print(f'  R=[{rightIndex}]: OOB')
            # print(f'  {overlapping_tiles=}')
            uniq_overlapping_tiles = set(
                map(tuple, overlapping_tiles)
            )
            # print(f'  {uniq_overlapping_tiles=}')
            truncated_overlapping_tiles = [
                (
                    max(RugStart, Begin),   # cut off start of tile at rug start
                    min(RugEnd, End),       # cut off end of tile at rug end
                )
                for (Begin, End) in uniq_overlapping_tiles
            ]
            # print(f'  {truncated_overlapping_tiles=}')
            tileSizes = [
                End - Begin + 1
                for (Begin, End) in truncated_overlapping_tiles
            ]
            # print(f'    {tileSizes=}')
            # NonOverlappingSizes_manual = sum(precomputeTileSizes[leftIndex:rightIndex + 1])
            NonOverlappingSizes = (
                0
                if leftIndex > rightIndex
                else
                (
                    (
                        prefixSumsOfTileSizes[rightIndex]
                    ) - (
                        0
                        if leftIndex == 0
                        else
                        prefixSumsOfTileSizes[leftIndex - 1]
                    )
                )
            )
            # CHECK = (NonOverlappingSizes_manual == NonOverlappingSizes)
            # print(f'{NonOverlappingSizes_manual} <=> {NonOverlappingSizes}: {CHECK}')
            # print(f'    {len(NonOverlappingSizes)=}')
            answers.append(sum(tileSizes) + NonOverlappingSizes)
        # print(f'{answers=}')
        
        return max(answers)
# NOTE: Runtime 1858 ms Beats 5.95%
# NOTE: Memory 37.01 MB Beats 100.00%
