class Solution:
    def isPalindrome(self, x: int) -> bool:
        # trying the follow-up ""without turning it into a string first"

        if x < 0:
            return False
        elif x == 0:
            return True
        
        list_instead = []
        while x:
            list_instead.append(x % 10)
            x = x // 10
        print(f"#{list_instead}")
        
        while list_instead:
            if len(list_instead) == 1:
                print("#1, true")
                return True
            first = list_instead.pop(0)
            last = list_instead.pop(-1)
            if first != last:
                print(f"{first} != {last}, false")
                return False
        print("list empty, true")
        return True

