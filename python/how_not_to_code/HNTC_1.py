from typing import List, Tuple

def bad_password_algorithm(password):
    # print(f'bad_pass({password})')
    while len(password) < 6:
        password += " "
    asc = map(ord, password)
    coeff = range(2, 2+len(password))
    pairs = zip(asc, coeff)
    total = 0
    for a, b in pairs:
        total += a * b
        # print((a, b), a * b, total)
    # print("total:", total)
    return total

def password_check(pw1, pw2):
    if pw1 == pw2:
        print(f"passed same password ({pw1}) twice")
        return False
    code1 = bad_password_algorithm(pw1)
    code2 = bad_password_algorithm(pw2)
    if code1 == code2:
        # print(f"PASSWORDS {pw1} and {pw2} match!  Code={code1}")
        return True
    else:
        print(f"passwords differ: {code1} {code2}")
        return False
    return None

def possible_alternate_groups(asc: List[int]):
    alternates = (
        # 2   3   4   5   6   7
        (+3, -2,  0,  0,  0,  0),
        (+2,  0, -1,  0,  0,  0),   # was 4, 2
        (+5,  0,  0, -2,  0,  0),
        (+3,  0,  0,  0, -1,  0),   # was 6, 2
        (+7,  0,  0,  0,  0, -2),

        ( 0, +4, -3,  0,  0,  0),
        ( 0, +5,  0, -3,  0,  0),
        ( 0, +2,  0,  0, -1,  0),   # was 6, 3
        ( 0, +7,  0,  0,  0, -3),

        ( 0,  0, +5, -4,  0,  0),
        ( 0,  0, +3,  0, -2,  0),   # was 6, 4
        ( 0,  0, +7,  0,  0, -4),

        ( 0,  0,  0, +6, -5,  0),
        ( 0,  0,  0, +7,  0, -5),

        ( 0,  0,  0,  0, +7, -6),
    )
    retval: List[List[int]] = []
    for a in alternates:
        # print("check a", a)
        new_asc_tuple = [
            (x + y, x - y)
            for x, y in zip(asc, a)
        ]
        # print("check new_asc_tuple", list(new_asc_tuple))
        new_asc_list = list(zip(*new_asc_tuple))
        # print("check new_asc_list", new_asc_list)
        retval.extend(new_asc_list)
    # print("found alternates", retval)
    return retval

def possible_alternate_groups_iter(asc, depth):
    possibles = [asc]
    for d in range(depth):
        # print("depth", d, "#poss", len(possibles))
        possibles = [
            q
            for p in possibles
            for q in possible_alternate_groups(p)
        ]
    # print("#poss", len(possibles))
    return possibles

def find_alternate_passwords(password: str):
    depth = 3
    asc = list(map(ord, password))
    legal_values = range(ord('A'), ord('Z')+1)
    found = 0
    possibles = possible_alternate_groups_iter(asc, depth)
    for new_asc in possibles:
        # print("check new_asc", new_asc)
        errors = [
            1
            for num in new_asc
            if num not in legal_values
        ]
        # print("check errors", errors)
        if errors == []:
            new_pass = map(chr, new_asc)
            new_pass = ''.join(new_pass)
            # print("check new_pass", new_pass)
            if password == new_pass:
                continue
            if password_check(password, new_pass):
                found += 1
    print(f"Found {found} alternates for {password} at depth {depth}")
    return
 
def check_password_range(first_pass, last_pass):
    first = bad_password_algorithm(first_pass)
    last = bad_password_algorithm(last_pass)
    difference = last - first + 1
    print(
        f"range '{first_pass}'-'{last_pass}':",
        first, last,
        difference
    )
    return difference

def display_hash_for_password(pw):
    print(f"password '{pw}' maps to hash {bad_password_algorithm(pw)}")
    return

# password_check("KLMNOP", "KLMNOP")
# password_check("KLMNOP", "MLLNOP")
# password_check("KLMNOP", "KNMNNP")
# password_check("KLMNOP", "RLMNON")

find_alternate_passwords("AAAAAA")
find_alternate_passwords("MMMMMM")
find_alternate_passwords("ABCDEF")

display_hash_for_password("ABCDEF")
display_hash_for_password("ABCDE")

check_password_range("AAAAAA", "ZZZZZZ")
check_password_range("AAAAA", "ZZZZZ")
check_password_range("AAAA", "ZZZZ")
check_password_range("AAA", "ZZZ")
answers = []
answers.append(check_password_range("AAA", "ZZZZZZ"))
answers.append(check_password_range("AA", "ZZ"))
answers.append(check_password_range("A", "Z"))
check_password_range("", "")

print("Total:", answers, sum(answers))

