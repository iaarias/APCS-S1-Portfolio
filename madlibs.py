#Ilani Arias
#12-9-24
#MadLibs

#Init

#Function

def madlib():
    print("Welcome to Madlibs!")
    print("Please fill in each blank with a word in each category.")
    dog = input("Dog breed: ")
    girl_name = input("Girl name: ")
    city = input("City: ")
    animal = input("Animal: ")
    thing = input("Object: ")
    reward = input("Another object: ")
    story(dog, girl_name, city, animal, thing, reward)

def story(dog, girl_name, city, animal, thing, reward):
    print("There once was a young " + dog + " named " + girl_name + ", who lived in " + city + ". She was on a walk one day, and saw a " + animal + " stuck in a tree!")
    print("It looked so sad and scared. " + girl_name + " knew she had to help. She ran to find a " + thing + " and used it to climb up the tree. Then, she rescued the " + animal + "!")
    print("'Thank you!' the " + animal + " said. 'Here's a " + reward + " as a reward for helping me!' The end! ")

#Main
madlib()

