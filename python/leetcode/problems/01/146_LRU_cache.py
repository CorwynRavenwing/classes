class LRUCache:

    keys = None
    values = None

    def __init__(self, capacity: int):
        self.keys = [None] * capacity
        self.values = [None] * capacity

    def get(self, key: int) -> int:
        if key in self.keys:
            index = self.keys.index(key)
            # print(f'get(): found {key=} at {index=}')
            value = self.values[index]
            if index != 0:
                del self.keys[index]
                del self.values[index]
                self.keys.insert(0, key)
                self.values.insert(0, value)
            return value
        else:
            # print(f'get(): no such {key=}')
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            index = self.keys.index(key)
            # print(f'put(): delete {key=} at {index=}')
        elif None in self.keys:
            index = self.keys.index(None)
            # print(f'put(): delete {None} at {index=}')
        else:
            index = -1  # overwrite the oldest one
            # print(f'put(): delete LRU={self.keys[index]} at {index=}')
        del self.keys[index]
        del self.values[index]
        self.keys.insert(0, key)
        self.values.insert(0, value)
        return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
