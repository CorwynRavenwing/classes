import re

def check_S_for_K(S, K):
    print("S", S)
    print("k", k)
    rK = re.compile(re.escape(k))
    any_results = False
    blanks = '~' * len(S)
    # print("~", blanks)
    skip_to_i = 0
    for i in range(len(S)):
        print("I", i)
        if i < skip_to_i:
            print("skip")
            continue
        subseq = blanks[:i] + S[i:]
        # print("ss", subseq)
        m = re.search(rK, subseq)
        # print("m", m)
        if m is not None:
            T = (m.start(), m.end()-1)
            print(T)
            any_results = True
            skip_to_i = m.start()+1
        else:
            break
            # if no results found, you won't
            # find any later in the 'i' loop
    if not any_results:
        T = (-1, -1)
        print(T)
    return
    
S = input()
k = input()
check_S_for_K(S,k)
