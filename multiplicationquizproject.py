#Ilani Arias
#Multiplication Quiz
#1-9-25

#Init
import random
score = 0 #This is the starting score
question = 1 #The player starts on question 1!

#Func
def quiz(): #This is the entire function to create the quiz.
    global score #Global allows these to be used throughout the function.
    global question
    print("Welcome to the Multiplication Quiz!")
    diff = input("Select a difficulty! Easy (E), Medium (M), or Hard (H): ") #the player selects a difficulty
    game_mode = input("Select a game mode! Normal Mode (N) or Endless Mode (E)!: ") #they player selects if they want a quiz with a certain amount of questions, or if they want bto continue endlessly.
    if game_mode == "n" or game_mode == "N":
        quiz_length = int(input("How many questions would you like your quiz to be?: ")) #This is used for "normal mode", allowing them player to choose the amount of questions they want to answer.
        if diff == "e" or diff == "E":
            for i in range(quiz_length):
                e_num1 = random.randint(1,10) #These generate two numbers within the "easy" category
                e_num2 = random.randint(1,10)
                correct_ans = e_num1 * e_num2 #This is the correct answer to the problem
                player_ans = int(input("Question " + str(question) + ": What is " + str(e_num1) + " times " + str(e_num2) + "? "))
                if player_ans == correct_ans: #If the player gets it correct, their score goes up
                    score = score + 1
                    question = question + 1
                    print("That is correct!")
                else:
                    question = question + 1
                    print("That is incorrect! The correct answer is " + str(correct_ans) + "!")
            print("Your final score is " + str(score) + " out of " + str(quiz_length) + "! Thank you for playing!") #Score is provided at the end
        elif diff == "m" or diff == "M":
            for i in range(quiz_length):
                m_num1 = random.randint(1,10) #These generate two numbers within the "medi7um" category
                m_num2 = random.randint(10,99)
                correct_ans = m_num1 * m_num2  #This is the correct answer to the problem
                player_ans = int(input("What is " + str(m_num1) + " times " + str(m_num2) + "? "))
                if player_ans == correct_ans: #If the player gets it correct, their score goes up
                    score = score + 1
                    question = question + 1
                    print("That is correct!")
                else:
                    question = question + 1
                    print("That is incorrect! The correct answer is " + str(correct_ans) + "!")
            print("Your final score is " + str(score) + " out of " + str(quiz_length) + "! Thank you for playing!") #Score is provided at the end
        elif diff == "h" or diff == "H":
            for i in range(quiz_length):
                h_num1 = random.randint(10,99) #These generate two numbers within the "hard" category
                h_num2 = random.randint(10,99)
                correct_ans = h_num1 * h_num2  #This is the correct answer to the problem
                player_ans = int(input("What is " + str(h_num1) + " times " + str(h_num2) + "? "))
                if player_ans == correct_ans: #If the player gets it correct, their score goes up
                    score = score + 1
                    question = question + 1
                    print("That is correct!")
                else:
                    question = question + 1
                    print("That is incorrect! The correct answer is " + str(correct_ans) + "!")
            print("Your final score is " + str(score) + " out of " + str(quiz_length) + "! Thank you for playing!") #Score is provided at the end

    elif game_mode == "e" or game_mode == "E":
        print("Welcome to Endless Mode!")
        if diff == "e" or diff == "E":
            while True: #This allows for the player to continue until they want to stop and break the loop
                e_num1 = random.randint(1,10) #These generate two numbers within the "easy" category
                e_num2 = random.randint(1,10)
                correct_ans = e_num1 * e_num2  #This is the correct answer to the problem
                player_ans = int(input("What is " + str(e_num1) + " times " + str(e_num2) + "? "))
                if player_ans == correct_ans: #If the player gets it correct, their score goes up
                    score = score + 1
                    question = question + 1
                    print("That is correct!")
                    replay = input("Keep playing? (Y,N): ")
                    if replay == "y" or replay == "Y":
                        print("Question " + str(question) + ": ")
                    elif replay == "n" or replay == "N": #Breaks the loop
                        question = question - 1
                        print("Your final score is " + str(score) + " out of " + str(question) + "! Thank you for playing!") #Score is provided when the player decided to quit, and the loop is broken
                        break
                else:
                    question = question + 1
                    print("That is incorrect! The correct answer is " + str(correct_ans) + "!")
                    replay = input("Keep playing? (Y,N): ")
                    if replay == "y" or replay == "Y":
                        print("Question " + str(question) + ": ")
                    elif replay == "n" or replay == "N": #Breaks the loop
                        question = question - 1
                        print("Your final score is " + str(score) + " out of " + str(question) + "! Thank you for playing!") #Score is provided when the player decided to quit, and the loop is broken
                        break

        elif diff == "m" or diff == "M":
            while True:  #This allows for the player to continue until they want to stop and break the loop
                m_num1 = random.randint(1,10) #These generate two numbers within the "medium" category
                m_num2 = random.randint(10,99)
                correct_ans = m_num1 * m_num2  #This is the correct answer to the problem
                player_ans = int(input("What is " + str(m_num1) + " times " + str(m_num2) + "? "))
                if player_ans == correct_ans: #If the player gets it correct, their score goes up
                    score = score + 1
                    question = question + 1
                    print("That is correct!")
                    replay = input("Keep playing? (Y,N): ")
                    if replay == "y" or replay == "Y":
                        print("Question " + str(question) + ": ")
                    elif replay == "n" or replay == "N": #Breaks the loop
                        question = question - 1
                        print("Your final score is " + str(score) + " out of " + str(question) + "! Thank you for playing!") #Score is provided when the player decided to quit, and the loop is broken
                        break
                else:
                    question = question + 1
                    print("That is incorrect! The correct answer is " + str(correct_ans) + "!")
                    replay = input("Keep playing? (Y,N): ")
                    if replay == "y" or replay == "Y":
                        print("Question " + str(question) + ": ")
                    elif replay == "n" or replay == "N": #Breaks the loop
                        question = question - 1
                        print("Your final score is " + str(score) + " out of " + str(question) + "! Thank you for playing!") #Score is provided when the player decided to quit, and the loop is broken
                        break

        elif diff == "h" or diff == "H":
            while True:  #This allows for the player to continue until they want to stop and break the loop
                h_num1 = random.randint(10,99) #These generate two numbers within the "hard" category
                h_num2 = random.randint(10,99)
                correct_ans = h_num1 * h_num2  #This is the correct answer to the problem
                player_ans = int(input("What is " + str(h_num1) + " times " + str(h_num2) + "? "))
                if player_ans == correct_ans: #If the player gets it correct, their score goes up
                    score = score + 1
                    question = question + 1
                    print("That is correct!")
                    replay = input("Keep playing? (Y,N): ")
                    if replay == "y" or replay == "Y":
                        print("Question " + str(question) + ": ")
                    elif replay == "n" or replay == "N": #Breaks the loop
                        question = question - 1
                        print("Your final score is " + str(score) + " out of " + str(question) + "! Thank you for playing!") #Score is provided when the player decided to quit, and the loop is broken
                        break
                else:
                    question = question + 1
                    print("That is incorrect! The correct answer is " + str(correct_ans) + "!")
                    replay = input("Keep playing? (Y,N): ")
                    if replay == "y" or replay == "Y":
                        print("Question " + str(question) + ": ")
                    elif replay == "n" or replay == "N": #Breaks the loop
                        question = question - 1
                        print("Your final score is " + str(score) + " out of " + str(question) + "! Thank you for playing!") #Score is provided when the player decided to quit, and the loop is broken
                        break



#Main
quiz()
