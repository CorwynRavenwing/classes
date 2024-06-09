class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        # clean up data:

        print(f'1 {len(heaters)=}')
        heaters = list(sorted(set(heaters)))
        print(f'2 {len(heaters)=}')

        print(f'A {len(houses)=}')
        houses = list(sorted(set(houses)))
        print(f'B {len(houses)=}')
        for He in heaters:
            if He in houses:
                houses.remove(He)
        print(f'C {len(houses)=}')
        distances = [None] * len(houses)
        j = 0
        for i, Ho in enumerate(houses):
            while True:
                # loop until we get an answer
                He = heaters[j]
                print(f'check house #{i}: [{Ho}] vs heater #{j}: {He}')
                if Ho < He:
                    answer = abs(Ho - He)
                    print(f'  {answer=}')
                    distances[i] = answer
                    break
                # assert Ho > He b/c we've deleted all the zero-distance houses
                if j + 1 < len(heaters):
                    # check next heater up
                    He2 = heaters[j+1]
                    if He < He2 < Ho:
                        print(f'  Next heater up is closer: {He} < {He2} < [{Ho}]')
                        j += 1
                        continue    # retry with new J
                    if He < Ho < He2:
                        print(f'  Between heaters: {He} < [{Ho}] < {He2}')
                        D1 = abs(Ho - He)
                        D2 = abs(Ho - He2)
                        if D1 < D2:
                            answer = D1
                            print(f'    lower one is still closer')
                            print(f'  {answer=}')
                            distances[i] = answer
                            break
                        else:
                            answer = D2
                            print(f'    higher one is closer now')
                            print(f'  {answer=}')
                            distances[i] = answer
                            j += 1  # also change heaters
                            break
                else:
                    # this is the max heater
                    answer = abs(Ho - He)
                    print(f'  {answer=}')
                    distances[i] = answer
                    break
            # print(f'  Found answer, moving on')
        print(f'{distances=}')

        return max(distances) if distances else 0

