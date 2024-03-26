# Enter your code here. Read input from STDIN. Print output to STDOUT

def digit_at_location_2(i):
    # i is 1-based
    section1a = "X123456789101"  # actual digits to return
    section1b = "XXXXXXXXXXX"    # length to subtract off
    width = len(section1b)
    if i < len(section1a):
        return int(section1a[i])
    i -= width
    digits = 1
    while True:
        digits += 1
        first = 10 ** (digits - 1)  # 2 -> 10
        last = (10 ** digits) - 1   # 2 -> 99
        numbers = last - first + 1  # 2 -> 90
        length = numbers * digits   # 2 -> 180
        # okay, let's actually try it then
        string = ''.join(
            map(
                str,
                range(first, last+1)
            )
        )
        print("#S=", string[:10] + "..." + string[-11:])
        print("#L=", length, len(string))
        assert length == len(string)
        if i > length:
            i -= length
            continue
        return int(string[i])
    pass

def digit_at_location(i):
    # i is 1-based
    section1a = "X123456789101"  # actual digits to return
    section1b = "XXXXXXXXXXX"    # length to subtract off
    width = len(section1b)
    if i < len(section1a):
        return int(section1a[i])
    i -= width
    digits = 1
    while True:
        digits += 1
        first = 10 ** (digits - 1)  # 2 -> 10
        last = (10 ** digits) - 1   # 2 -> 99
        numbers = last - first + 1  # 2 -> 90
        length = numbers * digits   # 2 -> 180
        # Notionally, we're doing this, but without composing the huge string
        # string = ''.join(
        #     map(
        #         str,
        #         range(first, last+1)
        #     )
        # )
        # print("#", string)
        # print(f"# {length} {len(string)}")
        # assert length == len(string)
        if i > length:
            i -= length
            continue
        
        nth_number = i // digits
        digit_in_number = i % digits
        number_int = first + nth_number
        number_str = str(number_int)
        d = number_str[digit_in_number]
        # print(f"#number={number_int} digit={digit_in_number}: '{d}'")
        return int(d)

def multiply_list(digits):
    retval = 1
    for d in digits:
        retval *= d
    return retval

short_way = True

def euler_40(Ituple):
    assert len(Ituple) == 7
    Ituple = tuple(sorted(Ituple))
    print(f"#{Ituple=}")
    answers = [
        digit_at_location(i) if short_way else digit_at_location_2(i)
        for i in Ituple
    ]
    print(f"#{answers=}")
    return multiply_list(answers)

# print(euler_40(
#     (10, 11, 12, 13, 14, 15, 16)
# ))
# print(euler_40(
#     (100, 200, 300, 400, 500, 600, 700)
# ))
# exit()

T = int(input().strip())
for _ in range(T):
    Ituple = tuple(map(int, input().strip().split(' ')))
    print(euler_40(Ituple))

