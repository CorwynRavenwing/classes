def alnum_plus_underscore_hyphen(s):
    for c in s:
        if c.isalnum():
            continue
        elif c == '_':
            continue
        elif c == '-':
            continue
        else:
            # print("invalid char '{}'".format(c))
            return False
    return True

def fun(s):
    # return True if s is a valid email,
    # else return False
    # print(s)
    split_at = s.split('@')
    # print(split_at)
    if len(split_at) != 2:
        # print("Wrong number of @ signs")
        return False
    username = split_at[0]
    fqdn = split_at[1]
    if len(username) == 0:
        # print("No username")
        return False
    split_dot = fqdn.split('.')
    if len(split_dot) != 2:
        # print("Wrong number of dots")
        return False
    webname = split_dot[0]
    extension = split_dot[1]
    if len(extension) > 3:
        # print("Too big an extension")
        return False
    if not alnum_plus_underscore_hyphen(username):
        # print("Invalid character in username")
        return False
    if not webname.isalnum():
        # print("Invalid character in webname")
        return False
    if not extension.isalpha():
        # print("Invalid character in extension")
        return False
    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

