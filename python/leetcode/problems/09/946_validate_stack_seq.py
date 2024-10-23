class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        while pushed or popped:
            # print(f'DEBUG: {pushed=} {stack=} {popped=}')
            if stack and popped and stack[-1] == popped[0]:
                print(f'POP {popped[0]}')
                del stack[-1]
                del popped[0]
            elif pushed:
                print(f'PUSH {pushed[0]}')
                stack.append(pushed[0])
                del pushed[0]
            else:
                print(f'NOTHING TO DO')
                return False

        return True

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 11 ms Beats 96.53%
# NOTE: Memory 16.92 MB Beats 13.40%
