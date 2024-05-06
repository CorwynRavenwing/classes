class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        mode = "new"
        prior = arr[0]
        for val in arr[1:]:
            if val > prior:
                # rising
                if mode == "new":
                    print("Begin")
                    mode = "rise"
                if mode == "rise":
                    print("  up")
                    pass
                elif mode == "fall":
                    print("FAIL, fall then rise")
                    return False
                else:
                    raise Exception(f"Unknown mode '{mode}' while rising")
            elif val == prior:
                print(f"FAIL, equal, not strictly rising or falling, mode '{mode}'")
                return False
            elif val < prior:
                # falling
                if mode == "new":
                    print(f"FAIL, mode falling from mode '{mode}'")
                    return False
                elif mode == "rise":
                    print("Peak")
                    mode = "fall"
                elif mode == "fall":
                    print("  down")
                    pass
                else:
                    raise Exception(f"Unknown mode '{mode}' while falling")
            prior = val
        if mode != "fall":
            print("FAIL: end of list, not falling, mode '{mode}'")
            return False
        print("Success")
        return True

