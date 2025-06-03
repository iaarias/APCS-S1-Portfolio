#Slot Machine
#Init
import random
import time
credits = 200
jackpots = 0
wins = 0
losses = 0
symbols = ["7","🂲","🂡","❤","✾","✪","🃁"]
winnings = 0
#Functions
#1. Introduction
#2. Ask the player, spin or quit
#3. Randomly pull 3 items from your list

def slotmachine():
    global credits
    global wins
    global losses
    global jackpots
    global winnings
    global bet
    while True:
        print("✧✧ Welcome to the Slot Machine! You have " + str(credits) + " credits.✧✧""")
        print("🌟 JACKPOT! = x1000 credits 🌟")
        answer = int(input("""Slot Machine:
                       1. Spin
                       2. Stats
                       3. Quit

                       Option: """))
        if answer == 1 and credits == 0:
            buy = input("You have no credits left. Would you like to buy more? (Y/N): ")
            if buy == "y" or buy == "Y":
                addcredits = int(input("How many credits would you like to buy?: "))
                credits = credits + addcredits
            elif buy == "n" or buy == "N":
                print("Bye!")
                break
        elif answer == 1 and credits > 0:
            bet = int(input("How many credits would you like to bet?: "))
            if bet > credits:
                print("Error: Not enough credits. Please try again.")
            else:
                print("Spinning...")
                time.sleep(2)
                credits = credits - bet
                image1 = random.choices(symbols,weights = [1,5,5,5,5,5,5,], k = 1)
                image2 = random.choices(symbols,weights = [1,5,5,5,5,5,5,], k = 1)
                image3 = random.choices(symbols,weights = [1,5,5,5,5,5,5,], k = 1)
                print("Slots: " + "  " + str(image1) + "  " + str(image2) + "  " + str(image3))
                if image1 == "7" and image2 == "7" and image3 == "7":
                    jackpots = jackpots + 1
                    winnings = bet * 1000
                    credits = credits + winnings
                    print("JACKPOT! You won " + str(winnings) + " credits!")
                elif image1 == image2 and image1 == image3:
                    wins = wins + 1
                    winnings = bet * 20
                    credits = credits + winnings
                    print("3 of a kind win! You won " + str(winnings) + " credits!")
                elif image1 == image2 or image1 == image3 or image2 == image3:
                    wins = wins + 1
                    winnings = bet * 5
                    credits = credits + winnings
                    print("2 of a kind win! You won " + str(winnings) + " credits!")
                else:
                    losses = losses + 1
                    print("Loss!")
                print("You have " + str(credits) + " credits.")
        elif answer == 2:
            print("Stats: ")
            print("Wins: " + str(wins))
            print("Losses: " + str(losses))
            print("JACKPOTS!: " + str(jackpots))

        else:
            print("Bye!")
            break

#Main
slotmachine()
