class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        grid_M = len(grid)
        grid_N = len(grid[0])

        # def R(thing: List[int]) -> List[int]:
        #     return list(reversed(thing))
        R = lambda x: list(reversed(x))
        itemFirst = lambda x: x[0]
        itemLast = lambda x: x[-1]
        innerSlice = lambda x: x[1:-1]    # slice omitting #0 and #-1

        def grid_to_layers(grid: List[List[int]]) -> List[List[int]]:
            print(f'grid_to_layers({grid}):')

            if not grid or not grid[0]:
                return []
            
            top = itemFirst(grid)
            rightSide = [
                itemLast(row)
                for row in innerSlice(grid)
            ]
            bottom = R(itemLast(grid))
            leftSide = [
                itemFirst(row)
                for row in R(innerSlice(grid))
            ]

            this_layer = top + rightSide + bottom + leftSide
            print(f'this_layer:\n  {top=}\n  {rightSide=}\n  {bottom=}\n  {leftSide=}')
            
            inner_grid = [
                innerSlice(row)
                for row in innerSlice(grid)
            ]
            
            return [this_layer] + grid_to_layers(inner_grid)

        def rotate_layers(layers: List[List[int]], k: int) -> List[List[int]]:
            print(f'  rotate_layers({layers},{k}):')
            
            def rotate_1_layer(layer: List[int], k: int) -> List[int]:
                print(f'  rotate_1_layer({layer},{k}):')
                L = len(layer)
                if k > L:
                    print(f'    {k=} % {L=}')
                    k %= L
                    print(f'      -> {k}')
                new_layer = layer[k:] + layer[:k]
                print(f'    {new_layer=}')
                return new_layer
            
            return [
                rotate_1_layer(layer, k)
                for layer in layers
            ]

        def layers_to_grid(layers: List[List[int]], height=grid_M, width=grid_N) -> List[List[int]]:
            print(f'Layers_To_Grid({layers},{height},{width}):')
            if not layers:
                return [[]] * height
            
            this_layer = layers[0]
            other_layers = layers[1:]
            inner_grid = layers_to_grid(other_layers, height - 2, width - 2)

            top = this_layer[:width]
            right_side = this_layer[width:width + height - 2]
            bottom = R(this_layer[width + height - 2:width + height - 2 + width])
            left_side = R(this_layer[width + height - 2 + width:])
            print(f'this grid:\n  {top=}\n  {bottom=}')
            print(f'  {left_side=}\n  {inner_grid=}\n  {right_side=}')

            center = [
                [A] + B + [C]
                for (A, B, C) in zip(left_side, inner_grid, right_side)
            ]

            new_grid = [top] + center + [bottom]

            return new_grid

        layers = grid_to_layers(grid)
        print(f'{layers=}')
        same_grid = layers_to_grid(layers)
        if grid != same_grid:
            print(f'ERROR! {same_grid=} isnt')
            return [[-99999]]

        new_layers = rotate_layers(layers, k)

        new_grid = layers_to_grid(new_layers)
        print(f'{new_grid=}')

        return new_grid

