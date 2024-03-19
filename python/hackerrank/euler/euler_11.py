#!/bin/python3

# import sys

def process_blocks(L):
    # L: List[Tuple[int,int,int,int]]
    L = [
        abcd
        for abcd in L
        if None not in abcd
    ]
    answers = [
        a * b * c * d
        for (a, b, c, d) in L
    ]
    # answers: List[int]
    return answers

def euler_11(grid):
    # print("#GRID", grid)
    retval = -1
    # print("#retval", retval)
    max_Y = len(grid)
    max_X = len(grid[0])
    # print("#maxX, maxY", max_X, max_Y)
    
    # horizontal
    # print("#horizontal")
    for y in range(max_Y):
        # print("#Y", y)
        RowY = grid[y]
        # print("#Y", y, RowY)
        BlockList = []
        for x in range(max_X - 4 + 1):
            Block = RowY[x:x+4]
            # print("#    X", x, Block)
            BlockList.append(Block)
        # print("#Blocks", BlockList)
        answers = process_blocks(BlockList)
        # print("#answers", answers)
        retval = max(retval, max(answers))
        # print("#retval", retval)
    
    # vertical
    # print("#vertical")
    grid_swap = list(zip(*grid))
    # print("#grid_swap", grid_swap)
    for y in range(max_Y):
        # print("#Y", y)
        RowY = grid_swap[y]
        # print("#Y", y, RowY)
        BlockList = []
        for x in range(max_X - 4 + 1):
            Block = RowY[x:x+4]
            # print("#    X", x, Block)
            BlockList.append(Block)
        # print("#Blocks", BlockList)
        answers = process_blocks(BlockList)
        # print("#answers", answers)
        retval = max(retval, max(answers))
        # print("#retval", retval)
    
    # diagonal ++
    # print("#diagonal ++")
    for y in range(max_Y - 4 + 1):
        # print("#Y", y)
        Rows = []
        for i in range(4):
            # print("#YI  ", y + i)
            small = [None] * i
            large = [None] * (4 - i - 1)
            RowYI = large + grid[y + i] + small
            Rows.append(RowYI)
        # print("#rows", Rows)
        BlockList = list(zip(*Rows))
        # print("#BlockList", BlockList)
        answers = process_blocks(BlockList)
        # print("#answers", answers)
        retval = max(retval, max(answers))
        # print("#retval", retval)

    # diagonal +-
    # print("#diagonal +-")
    for y in range(max_Y - 4 + 1):
        # print("#Y", y)
        Rows = []
        for i in range(4):
            # print("#YI  ", y + i)
            small = [None] * i
            large = [None] * (4 - i - 1)
            RowYI = small + grid[y + i] + large
            Rows.append(RowYI)
        # print("#rows", Rows)
        BlockList = list(zip(*Rows))
        # print("#BlockList", BlockList)
        answers = process_blocks(BlockList)
        # print("#answers", answers)
        retval = max(retval, max(answers))
        # print("#retval", retval)
    return retval

grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)
print(euler_11(grid))

