# Python 2.7.13
#
# Author: Ryan Vinyard
#
# Purpose: The Tech Academy - Python Course, concept drill

# I've tried to model this script off of the nice/mean drill, to build good habits.


def start(name="", number=0, decimal=0, array=[]):
    #This start function allows us to smoothly go from function to function as we pass the relevant information.
    name = get_name(name)
    number = get_number(name, number)
    decimal = get_decimal(name, decimal)
    array = short_list(name, array)
    fun_facts(number,decimal)
    
def get_name(name):
    #In this function we get the user's name, assign the string to a variable, and use .format to print it back.
    name = raw_input("Hello my dude! I want to play a game. The rules are simple. Just do everything I ask. First of all, what is your name? ").capitalize()
    print("\n{}, what a great name!".format(name))
    return name

def get_number(name, number):
    #In this function we assign the user's number to a variable and start a while loop to make sure they give a relevant number.
    stop = False
    while stop == False:
        try:
            number = int(input(("\nAnother question, what is your favorite number? Don't get snarky and put in like 55.667 because I'll just make it a whole number. ")))
        except NameError:
            print("That's not a number")
            continue
        if number == 69 or number == 420:
            # Using the or operator to make sure you're not a JUVENILE
            print("No dude, we're not doing that. Give me literally any other number.")
        elif number == 0:
            print("That's 0, try again")
        else:
            print("\n{}, cool, neat-o, real nice number. The best number.".format(number))
            stop = not stop
            #This is a bit of a sloppy place to put the not operator.
            #I just wanted to show that I understand that if stop is false, it will return true.
    return number

def get_decimal(name, decimal):
    #In this function we assign the user's float to decimal, because float is already an expression.
    #We also use the and operator to make sure decimal is between 0 and 1.
    #In addition, we have an if statement with elif and else to make the user keep inputting until they get it right.
    stop = False
    while stop == False:
        try:
            decimal = float(raw_input(("\nOk, this one's a bit silly, but give me a decimal number between 0 and 1 noninclusive. ")))
        except ValueError:
            print("Yo, that's not a sweet decimal number, try again")
            continue
        if decimal<1 and decimal>0:
            print("\n{}, alright, I like that.".format(decimal))
            stop = True
        elif decimal>1:
            print("That's too high, try something between 0 and 1")
        else:
            print("That's too low, try again")
    return decimal

def short_list(name, array):
    
    print("\nOk {}, I'm gonna ask you about some people you like.".format(name))
    stop = False
    while stop == False:
        author = raw_input("\nCan you tell me an author you like, please? ").title()
        array.append(author)
        figure = raw_input("Now, can you tell me the name of someone who inspires you? ").title()
        array.append(figure)
        comedian = raw_input("Finally, who is a favorite comedian of yours? ").title()
        array.append(comedian)
        for i in array:
            print(i)
        answer = raw_input("Are these the people? Type yes if this is correct. ").capitalize()
        if answer == 'Yes':
            print("Well that's great, because I also like those people!")
            stop = True
        else:
            print("Then let's try again.")
            array = []
    return array

def fun_facts(number, decimal):
    #In this function we'll use all those math operators, +,-,*,/,+=,-, and %
    print("\nHey now, you remember those numbers you told me? {} and {}? Check this out, here's some fun facts: ".format(number,decimal))
    print("\nDid you know that if you add {} and my favorite number, 17, you get {}?".format(number,(number+17)))
    number += 17
    answer1 = number
    print("Then, if you subtract {} from {}, you get {}?".format(decimal,number,(number-decimal)))
    new_number= number-decimal
    answer2 = new_number
    print("Now if you multiply that by your favorite decimal number, you get {}.".format(new_number*decimal))
    new_number= new_number*decimal
    answer3 = new_number
    print("Now divide that by 2, and you get {} with a remainder of {}.".format(new_number/2,(new_number%2)))
    answer4 = new_number/2
    answer5 = new_number%2
    tup = (answer1, answer2, answer3, answer4, answer5)
    print("\nSo now we have these numbers:")
    for i in tup:
        print(i)
    exit()
        
    
if __name__ == "__main__":
    start()
