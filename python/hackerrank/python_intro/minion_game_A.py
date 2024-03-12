def all_substring_counts(string):
    strlen = len(string)
    D = {}
    for length in range(1, strlen+1):
        print("LEN", length)
        for start in range(0, strlen-length+1):
            end = start+length
            s = string[start:end]
            D[s] = D.get(s, 0)
            D[s] += 1
            print("[{}:{}] {} ={}".format(start, end, len(s), D[s]))
    return D

def starts_with_vowel(string):
    vowels = ('A', 'E', 'I', 'O', 'U')
    first_char = string[0]
    retval = False
    if first_char in vowels:
        # print("{} is a VOWEL".format(first_char))
        retval = True
    # else:
        # print("{} is not a vowel".format(first_char))
    
    return retval

def minion_game(string):
    word_data = all_substring_counts(string)
    print("WD:", word_data)

    vowel_player = 0
    cons_player  = 0
    for s in word_data.keys():
        if starts_with_vowel(s):
            vowel_player += word_data[s]
            print(s, "vowel +", word_data[s], vowel_player)
        else:
            cons_player += word_data[s]
            print(s, "cons  +", word_data[s], cons_player)
    
    # print("VOWEL", vowel_player)
    # print("CONS ", cons_player)
    
    if vowel_player > cons_player:
        winner = "Kevin"
        score = vowel_player
    elif vowel_player < cons_player:
        winner = "Stuart"
        score = cons_player
    else:
        winner = None
    
    if winner:
        print("{} {}".format(winner, score))
    else:
        print("Draw")

    return

if __name__ == '__main__':
    s = input()
    minion_game(s)

