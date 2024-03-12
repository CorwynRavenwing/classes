#!/bin/python3

# import sys

def digits_of(x):
    return tuple(str(x))

def is_palindrome(x):
    digits_of_x = digits_of(x)
    # print("#DIGITS", digits_of_x)
    L = len(digits_of_x)
    for i in range(L // 2):
        # even lengths: checks all digits
        # odd lengths: checks all but the center digit
        # print(
        #     "#  CHECK",
        #     digits_of_x[i],
        #     digits_of_x[L-i-1],
        # )
        if digits_of_x[i] != digits_of_x[L-i-1]:
            # print("#    FAIL")
            return False
        # if i > L-i-1:
        #     print("#    ERROR", i, L-i-1)
    return True

# test is_palindrome function:
assert is_palindrome(101)
assert is_palindrome(123321)
assert not is_palindrome(123421)
assert not is_palindrome(123)
assert not is_palindrome(90210)

def euler_4(n):
    MIN_3DIGIT = 100
    MAX_3DIGIT = 999
    max_known_palindrome = 0  # ... technically :-)
    for P in range(MIN_3DIGIT, MAX_3DIGIT+1):
        print("#P", P)
        digits_P = digits_of(P)
        if digits_P[-1] == '0':
            # P ends in 0
            # -> so does P*Q for all Q
            # -> none are palindromes
            continue
            # next P
        
        MaxQ = n // P   # highest Q where P*Q <= n
        MaxQ = min(MaxQ, MAX_3DIGIT)
        if MaxQ < P:
            # P is now > sqrt(n)
            break
            # from P loop -> stop
        
        R = reversed(range(P, MaxQ+1))
        for Q in R:
            if Q < P:
                print("#P NEXT")
                break
                # from Q loop -> next P
            trial = P * Q
            print("#Q", P, Q, trial)
            if trial >= n:
                continue
                # next Q
            
            if trial < max_known_palindrome:
                break
                # from Q loop -> next P
            
            if is_palindrome(trial):
                print("#!", P, Q, trial, "PALINDROME")
                max_known_palindrome = trial
            # else:
            #     print("#\tnot palindrome")
        # end Q loop
    # end P loop
    print("#DONE")
    return max_known_palindrome

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(euler_4(n))

