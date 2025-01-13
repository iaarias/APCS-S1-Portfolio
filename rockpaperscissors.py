#Ilani Arias
#1-7-25
#Rock, Paper, Scissors

#Init
import random
wins = 0
ties = 0
losses = 0
round = 1
#Functions
def rock_paper_scissors():
    global wins
    global losses
    global ties
    global round
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        player_move = input("Select a move! (R, P, S):  " )
        comp_gen = random.randint(1,3)
        if comp_gen == 1:
            comp_move = "Rock"
        elif comp_gen == 2:
            comp_move = "Paper"
        elif comp_gen == 3:
            comp_move = "Scissors"
        print("Rock, Paper, Scissors, Go!")
        print("I choose " + str(comp_move) + "!")


        if (player_move == "r" or player_move == "R") and comp_gen == 1:
            print("Tie!")
            ties = ties + 1

        elif (player_move == "r" or player_move == "R") and comp_gen == 2:
            print("I win! Paper beats rock!")
            losses = losses + 1

        elif (player_move == "r" or player_move == "R") and comp_gen == 3:
            print("You win! Rock beats scissors!")
            wins = wins + 1



        elif (player_move == "p" or player_move == "P") and comp_gen == 1:
            print("You win! Paper beats rock!")
            wins = wins + 1

        elif (player_move == "p" or player_move == "P") and comp_gen == 2:
            print("Tie!")
            ties = ties + 1

        elif (player_move == "p" or player_move == "P") and comp_gen == 3:
            print("I win! Scissors beats paper!")
            losses = losses + 1



        elif (player_move == "s" or player_move == "S") and comp_gen == 1:
            print("I win! Rock beats scissors!")
            losses = losses + 1

        elif (player_move == "s" or player_move == "S") and comp_gen == 2:
            print("You win! Scissors beats paper!")
            wins = wins + 1

        elif (player_move == "s" or player_move == "S") and comp_gen == 3:
             print("Tie!")
             ties = ties + 1


        print("Wins: " + str(wins) + ", Ties: " + str(ties) + ", Losses: " + str(losses))
        replay = input("Play again? (y, n)")
        if replay == "y":
            round = round + 1
            print("Round " + str(round) + "!" )
        elif replay == "n":
            print("Thank you for playing!")
            break


#Main
rock_paper_scissors()
