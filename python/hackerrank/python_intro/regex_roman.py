thou = r"M{0,3}(C+M)?(C+D)?D?"
hund = r"C{0,3}(X+C)?(X+L)?L?"
tens = r"X{0,3}(I+X)?(I+V)?V?"
ones = r"I{0,3}"
regex_pattern = r"^" + thou + hund + tens + ones + r"$"
# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

