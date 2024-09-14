class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        # we borrow some code from #3243:
        # but that's both far too slow and overkill for the actual question

        # First, each distance is just the ID number of the node,
        # due to how the adjacency matrix is set up;
        # and we only care about the last one
        distance_to_end = n - 1
        # these will be any sectons that we can skip past.
        jump_segments = []

        def segments_overlap(seg1: Tuple[int,int], seg2: Tuple[int,int]) -> bool:
            # this definition of "overlap" allows adjacent segments,
            # e.g. [1,2] and [2,3] do NOT overlap.
            (A1, B1) = seg1
            (A2, B2) = seg2
            return (
                (
                    (A1 <= A2 < B1)
                ) or (
                    (A1 < B2 <= B1)
                ) or (
                    (A2 <= A1 < B2)
                ) or (
                    (A2 < B1 <= B2)
                )
            )

        def merge_segments(seg1: Tuple[int,int], seg2: Tuple[int,int]) -> bool:
            (A1, B1) = seg1
            (A2, B2) = seg2
            return (
                min(A1, A2),
                max(B1, B2),
            )

        def jump_distance(segment: Tuple[int,int]) -> int:
            (A, B) = segment
            return (B - A - 1)

        def new_distance_after_linking(fromNode: int, toNode: int) -> None:
            nonlocal jump_segments
            nonlocal distance_to_end
            if fromNode == toNode:
                return distance_to_end
            new_segment = (fromNode, toNode)

            insert_point = bisect.bisect_left(jump_segments, new_segment)

            try:
                if new_segment == jump_segments[insert_point]:
                    print(f'  New segment already in jump_segments')
                    return distance_to_end
            except IndexError:
                pass

            jump = jump_distance(new_segment)
            distance_to_end -= jump
            jump_segments.insert(insert_point, new_segment)

            disjoint = 0
            # checked = 0
            for i in range(max(1, insert_point), len(jump_segments)):
                # checked += 1
                # print(f'Loop {i}: {jump_segments=}')
                prev_segment = jump_segments[i - 1]
                this_segment = jump_segments[i]
                if segments_overlap(prev_segment, this_segment):
                    new_segment = merge_segments(prev_segment, this_segment)
                    print(f'  Merge {prev_segment}, {this_segment} -> {new_segment}')

                    distance_to_end += sum([
                        # add back in the length of the jumps we're removing
                        jump_distance(prev_segment),
                        jump_distance(this_segment),
                        # subtract off the length of the new jump we're adding
                        -jump_distance(new_segment),
                    ])

                    jump_segments[i - 1] = None
                    jump_segments[i] = new_segment
                else:
                    # print(f'  Segments {prev_segment}, {this_segment} disjoint')
                    disjoint += 1
                    if disjoint >= 2:
                        # print(f'    ... stop.')
                        break
            # print(f'{checked=}')
            while None in jump_segments:
                jump_segments.remove(None)
            # print(f'after:  {jump_segments=}')
            return distance_to_end

        # initial_distance = new_distance_after_linking(0, 0)
        print(f'initial distance={distance_to_end}')

        def doQuery(Q: List[int]) -> int:
            (fromI, toI) = Q
            return new_distance_after_linking(fromI, toI)
        
        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Acceptance Rate 23.4%
# NOTE: Timeout for huge inputs
