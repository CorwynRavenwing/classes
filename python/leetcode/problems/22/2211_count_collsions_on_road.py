class Solution:
    def countCollisions(self, directions: str) -> int:
        carList = list(directions)

        # ignore any leading 'L':
        while carList and carList[0] == 'L':
            print(f'remove leading L')
            carList = carList[1:]

        # ignore any trailing 'R':
        while carList and carList[-1] == 'R':
            print(f'remove trailing R')
            carList = carList[:-1]
        
        moving_cars_who_will_crash = [
            1
            for Car in carList
            if Car in 'RL'
        ]
        return sum(moving_cars_who_will_crash)

