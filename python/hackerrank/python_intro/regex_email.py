import re
import email.utils

usr = r"[A-Za-z]" + r"([-_.A-Za-z0-9])*"
dom = r"[A-Za-z]+"
ext = r"[A-Za-z]{1,3}"
email_re = r"^"+usr+r"@"+dom+r"[.]"+ext+r"$"
email_test = re.compile(email_re)

N = int(input())
for i in range(N):
    line = input()
    PA = email.utils.parseaddr(line)
    # print("# pa", PA)
    (name, e) = PA
    if (re.match(email_test, e)):
        print(email.utils.formataddr((name, e)))
    # else:
        # print("# SKIP")

