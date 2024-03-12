import operator

def person_lister(f):
    def inner(people):
        # print("#P0", people)
        # people.sort(key=operator.itemgetter(2))
        # itemgetter sorts as strings, not ints
        # so 100 < 2
        people.sort(key=lambda x: int(x[2]))
        # print("#P1", people)
        retval = []
        for person in people:
            retval.append(f(person))
        return retval
    return inner

@person_lister
def name_format(person):
    # print("#NF", len(person), person)
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

