class CustomStack:

    def __init__(self, maxSize: int):
        print(f'init({maxSize})')
        self.MaxSize = maxSize
        self.Size = 0
        self.Stack = []
        return

    def push(self, x: int) -> None:
        print(f'pop({x})')
        if self.Size >= self.MaxSize:
            print(f'Error: push on full stack')
            return
        self.Size += 1
        self.Stack.append(x)
        return

    def pop(self) -> int:
        print(f'pop()')
        if self.Size <= 0:
            print(f'Pop on empty stack')
            return -1
        self.Size -= 1
        return self.Stack.pop(-1)

    def increment(self, k: int, val: int) -> None:
        print(f'incr({k},{val})')
        k = min(k, self.Size)
        for i in range(k):
            self.Stack[i] += val
        return

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

# NOTE: Accepted on second Run (first was a 1-char variable name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 98 ms Beats 26.98%
# NOTE: Memory 17.67 MB Beats 18.01%
