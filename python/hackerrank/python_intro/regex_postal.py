regex_integer_in_range = r"[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(.)(?=.\1)"
# Do not delete 'r'.

import re
P = input()

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
print("Explanation:")

print("In range:", bool(re.match(regex_integer_in_range, P)))
print("Repetative:", len(re.findall(regex_alternating_repetitive_digit_pair, P)))

