vowels = ['A', 'E', 'I', 'O', 'U']
def is_vowel(char):
    return char in vowels

def minion_game(string):
    player_names = { True: "Kevin", False: "Stuart", }
    player_count_dict = {True: 0, False: 0, }
    for j in range(0, len(string)):
        first_char = string[j]
        v = is_vowel(first_char)
        player_count_dict[v] += len(string)-j
    winning_score = max(player_count_dict.values())
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
    winner = player_names[vowels_win]
    print("{} {}".format(winner, winning_score))
    return

if __name__ == '__main__':
    s = input()
    minion_game(s)

