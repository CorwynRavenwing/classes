class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:

        possible_states = set()
        state_q = [(0,0)]   # start with no water
        while state_q:
            state = state_q.pop()
            if state in possible_states:
                continue
            possible_states.add(state)
            print(f'{state=}')
            (A, B) = state
            if target in [A, B, sum(state)]:
                print(f'  YES')
                return True
            new_states = set()
            new_states.add((x, B))   # fill jug A
            new_states.add((A, y))   # fill jug B
            new_states.add((0, B))   # empty jug A
            new_states.add((A, 0))   # empty jug B
            if A > 0 and B < y:
                # pour A into B
                if A >= (y - B):
                    # until B is full
                    b_full = (
                        A - (y - B),
                        B + (y - B),
                    )
                    assert b_full[1] == y
                    new_states.add(b_full)
                else:
                    # until A is empty
                    new_states.add((0, A + B))
            if B > 0 and A < x:
                # pour B into A
                if B >= (x - A):
                    # until A is full
                    a_full = (
                        A + (x - A),
                        B - (x - A),
                    )
                    assert a_full[0] == x
                    new_states.add(a_full)
                else:
                    # until B is empty
                    new_states.add((A + B, 0))
            for state in new_states:
                (A, B) = state
                assert 0 <= A <= x
                assert 0 <= B <= y
                print(f'  -> {state}')
                state_q.append(state)
        print(f'NO')
        return False

