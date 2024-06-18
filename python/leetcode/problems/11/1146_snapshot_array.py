class SnapshotArray:

    def __init__(self, length: int):
        self.next_snap = 0
        self.length = length
        self.data = {}

    def set(self, index: int, val: int) -> None:
        print(f'set({index=},{val=})')
        if index > self.length:
            raise ValueError(f'set(): {index=} > {length=}')
        self.data.setdefault(index, [])
        if self.data[index]:
            prior = self.data[index][-1]
            (snap_then, value_then) = prior
            if snap_then == self.next_snap:
                del self.data[index][-1]
                # throw it away, replace with this one
        self.data[index].append(
            (self.next_snap, val)
        )
        return

    def snap(self) -> int:
        snap = self.next_snap
        self.next_snap += 1
        print(f'snap() -> {snap}')
        return snap

    def get(self, index: int, snap_id: int) -> int:
        print(f'get({index=},{snap_id=})')
        if index > self.length:
            raise ValueError(f'get(): {index=} > {length=}')
        if snap_id < 0 or snap_id >= self.next_snap:
            raise KeyError(f'get(): invalid {snap_id=} (min 0, max {self.next_snap})')
        self.data.setdefault(index, [])
        item = self.data[index]
        # print(f'#####\nSearch for {snap_id} in item=\n{item}\n#####')
        if not item:
            # print(f'shortcut 0 {item=}')
            return 0
        prior = item[-1]
        (snap_then, value_then) = prior
        if snap_then == snap_id:
            # print(f'shortcut prior {snap_then=}')
            return value_then
        L = 0
        R = len(item) - 1
        left = item[L][0]
        right = item[R][0]
        # print(f'0 [{L},{R}] = ({left},{right}) T={snap_id}')
        if left > snap_id:
            # print(f'0: {left=} > {snap_id=}')
            return 0
        if left == snap_id:
            # print(f'found {L=} {left} T={snap_id}')
            return item[L][1]
        if right == snap_id:
            # print(f'found {R=} {right} T={snap_id}')
            return item[R][1]
        while L + 1 < R:
            M = (L + R) // 2
            mid = item[M][0]
            # print(f'B [{L},{M},{R}] = ({left},{mid},{right}) T={snap_id}')
            if mid == snap_id:
                # print(f'  found {M=} {mid} T={snap_id}')
                return item[M][1]
            if mid < snap_id:
                # print('  replace left')
                (L, left) = (M, mid)
                continue
            if mid > snap_id:
                # print('  replace right')
                (R, right) = (M, mid)
                continue
            raise Exception('{mid} <=> {snap_id} is none of <, ==, >')
        # print(f'after loop: [{L},{R}] = ({left},{right}) T={snap_id}')
        if right < snap_id:
            # print(f'approx {R=} {right} (T={snap_id})')
            return item[R][1]
        if left < snap_id:
            # print(f'approx {L=} {left} (T={snap_id})')
            return item[L][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

