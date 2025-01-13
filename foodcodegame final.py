#Ilani Arias
#10-18-24
#Food Generator Game

#init
#func
print("Welcome to the Food Generator! What food do you want to eat?")
print("Answer the questions and be given a food!")

ans = input("Savory or Sweet? ")
if ans == "savory" or ans == "Savory":
    ans = input("Smaller portion (s) , or a meal (m)? ")
    if ans == "m" or ans == "M":
        ans = input("On a crust or bun? ")
        if ans == "bun" or ans == "Bun":
            print("Your food is: A burger or hotdog!")
        else:
            print("Your food is: Pizza!")
    if ans == "s" or ans == "S":
        ans = input("Fried, or seafood? ")
        if ans == "seafood" or "Seafood":
            print("Your food is: Sushi!")
        else:
            print("Your food is: Fries or Chips!")

if ans == "sweet" or ans == "Sweet":
    ans = input("Frosting (f) or no (n)? ")
    if ans == "f" or "F":
        ans = input("Smaller (s) or larger portion (l)? ")
        if ans == "s" or ans == "S":
            print("Your food is:  A Cupcake or Ice Cream!")
        else:
            print("Your food is: Cake or pie!")
    elif ans == "N" or "n":
        ans = input("Baked goods (b), or sugary sweet (s)? ")
        if ans == "b" or "B":
            print("Your food is: A Cookie!")
        else:
            print("Your food is: Candy!")


