import re

word = input()
cons = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
vowel = 'AEIOUaeiou'
rConsBefore = r'(?<=[{}])'.format(cons)
rConsAfter  = r'(?=[{}])'.format(cons)
rVowels = r'([{}]+)'.format(vowel)
regex = rConsBefore + rVowels + rConsAfter
# print(regex)
ans = re.findall(regex, word)
# print(ans)
any_answers = False
for v in ans:
    if len(v) <= 1:
        # print("V ({}) is too short".format(v))
        continue
    print(v)
    any_answers = True
if not any_answers:
    print(-1)

