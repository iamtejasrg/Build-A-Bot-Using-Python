import random
import math
def play():
    user = input("Whats your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "Its a Tie"

    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

def is_win(player, opponent):
    # winning conditions: r > s, s > p, p > r
    if(player =='r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play_best_of(n):
    # play against the computer until someone wins the best of n games
    player_win = 0
    computer_win = 0
    wins_necessary = math.ceil(n/2)
    while player_win < wins_necessary or computer_win < wins_necessary:
        result, user, computer = play()
        #tie
        if(result==0):
            print("Its a Tie.")
        #you win
        elif(result==1):
            player_win += 1
            print("You Won")
        else:
            computer_win+=1
            print("Computer Won")
        print("\n")

if __name__=='__main__':
    play_best_of(2)
    # play_best_of(5)
