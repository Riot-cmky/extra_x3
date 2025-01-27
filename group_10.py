# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes

# FUnction that shows the joke and asks whether the audience wants to hear anither one
def tell_joke(joke_list):
    for joke in joke_list:
        print(joke)
        input("Press Enter for the next part of the joke.")
   
    return input("Do you want to hear another joke or are you finished? ").lower()


# Lists
#if they want to hear a robber joke
robber_jokes = [
    "Knock Knock",
    "Who's there?",
    "Calder",
    "Calder who?",
    "Calder police - I've been robbed!"
]
# if they want to hear a tank joke
tank_jokes = [
    "Knock Knock",
    "Who's there?",
    "Tank",
    "Tank who?",
    "You’re welcome!"
]

# if they want to hear a pencil joke
pencil_jokes = [
    "Knock Knock",
    "Who's there?",
    "Broken pencil",
    "Broken pencil who?",
    "Nevermind, it's pointless!"
]


# The important code that asks for users input
joke = input("Do you want to hear a joke? (yes/no) ").lower()
# If/Else statement
if joke == "no":
    print("Okay, suit yourself!")
else:
    print("Great, let's play!")
    while joke == "yes": #While loop
        question = input("Do you want to hear a joke about robbers, tanks, or pencils? ").lower()
       
        if question == "robbers":
            joke = tell_joke(robber_jokes)
        elif question == "tanks":
            joke = tell_joke(tank_jokes) #elif statement
        elif question == "pencils":
            joke = tell_joke(pencil_jokes)
        else:
            print("Sorry, I don't understand that category. Please choose from robbers, tanks, or pencils.")
            joke = input("Do you want to hear a joke? (yes/no) ").lower()

    if joke == "finished":
        rate = int(input("Please rate our game 1-10! ")) #integer
        final_score = int(rate * 10)
        print(f"{final_score} percent satisfaction rate") # f-string used here
        friend = input("Would you recommend this game to a friend? (yes/maybe/no) ").lower()

        if friend == "yes" or friend == "maybe":
            print("Thanks, we appreciate it.")
        else:
            print("Sorry you did not enjoy it.")