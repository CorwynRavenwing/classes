vowels = ['A', 'E', 'I', 'O', 'U']
def is_vowel(char):
    return char in vowels

def minion_game(string):
    substring_count_dict = {}
    for i in range(1, len(string)+1):
        # print("#I", i)
        for j in range(0, len(string)-i+1):
            # print("#J", j)
            ss = string[j:j+i]
            # print("#I,J,SS", i, j, ss)
            substring_count_dict[ss] = substring_count_dict.get(ss, 0) + 1
    player_count_dict = {True: 0, False: 0}
    for word, num in substring_count_dict.items():
        first_char = word[0]
        v = is_vowel(first_char)
        player_count_dict[v] += num
        # print("#V", first_char, v, num)
    winning_score = max(player_count_dict.values())
    # print("#W", winning_score)
    vowels_win_list = [
        vowels_win
        for vowels_win, score
        in player_count_dict.items()
        if score == winning_score
    ]
    if len(vowels_win_list) == 2:
        print("Draw")
        return
    vowels_win = vowels_win_list[0]
    # print("#V", vowels_win)
    player_names = {
        True: "Kevin",
        False: "Stuart",
    }
    winner = player_names[vowels_win]
    print("{} {}".format(winner, winning_score))
    return

if __name__ == '__main__':
    s = input()
    minion_game(s)

