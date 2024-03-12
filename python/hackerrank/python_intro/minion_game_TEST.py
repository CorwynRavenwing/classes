def test_numbers(l):
    string = "X" * l
    iloop = []
    for i in range(1, len(string)+1):
        for j in range(0, len(string)-i+1):
            # print("I J", i, j)
            iloop.append( (i, j) )
    print(sorted(iloop))
    print("-" * 10)

    jloop = []
    for j in range(0, len(string)):
        n = 0
        for i in range(1, len(string)-j+1):
            # print("I J", i, j)
            jloop.append( (i, j) )
            n += 1
        print("N", n, len(range(1, len(string)-j+1)), len(string)-j)
        
    print(sorted(jloop))
    print("=" * 10)
    return

test_numbers(3)
test_numbers(5)
