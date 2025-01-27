def tell_joke(joke_type):
   # """Function to tell jokes based on the provided type."""
    if joke_type == "robbers":
        input("Knock Knock. ")
        input("Calder. ")
        print("Calder police - I've been robbed!")
    elif joke_type == "tanks":
        input("Knock Knock. ")
        input("Tank. ")
        print("You are welcome!")
    elif joke_type == "pencils":
        input("Knock Knock. ")
        input("Broken pencil. ")
        print("Nevermind, it's pointless!")

def jokes(categories):
 #   """Main function to handle the joke-telling program."""
    joke = input("Do you want to hear a joke? (yes/no) ").lower()

    if joke == "no":
        print("Okay, suit yourself!")
        return
    elif joke == "yes":
        print("Great, Let's Play!")
        while True:
            question = input(f"Do you want to hear a joke about {', '.join(categories)}? ").lower()

            if question in categories:
                tell_joke(question)  # Call the joke function with the selected type
            else:
                print("Sorry, I don't have a joke about that. Please choose from the available categories.")

            # Ask if they want another joke or are finished
            joke = input("Do you want to hear another joke or are you finished? (another/finished) ").lower()
            if joke == "finished":
                rate = int(input("Please rate our game 1-10! "))
                final_score = rate * 10
                print(f"{final_score}% satisfaction rate")
                friend = input("Would you recommend this game to a friend? (yes/no) ").lower()
                if friend in ["yes", "maybe"]:
                    print("Thanks, we appreciate it.")
                else:
                    print("Sorry you did not enjoy it.")
                break
            elif joke != "another":
                print("Sorry, I didn't understand that. Please type 'another' or 'finished'.")
    else:
        print("Okay, maybe next time!")

# List of available joke categories
categories = ["robbers", "tanks", "pencils"]

# Call the jokes function with the categories as a parameter
jokes(categories)

# 1. tell_joke(joke_type)
# def tell_joke(joke_type):
#     """Function to tell jokes based on the provided type."""
# Purpose: This function takes one parameter, joke_type, and tells a joke based on that type.
# It contains different jokes for specific categories like "robbers," "tanks," and "pencils."
#     if joke_type == "robbers":
#         input("Knock Knock. ")
#         input("Calder. ")
#         print("Calder police - I've been robbed!")
# Explanation: If joke_type is "robbers," the program presents a knock-knock joke.
# input() is used to pause and simulate the interactive part of a knock-knock joke.
# The punchline is printed when the user completes the setup.
#     elif joke_type == "tanks":
#         input("Knock Knock. ")
#         input("Tank. ")
#         print("You are welcome!")
# Explanation: If joke_type is "tanks," another knock-knock joke is presented, with the punchline "You are welcome!"
#     elif joke_type == "pencils":
#         input("Knock Knock. ")
#         input("Broken pencil. ")
#         print("Nevermind, it's pointless!")
# Explanation: For the "pencils" category, a different knock-knock joke is told, ending with the punchline "Nevermind, it's pointless!"
# 2. jokes(categories)
# def jokes(categories):
#     """Main function to handle the joke-telling program."""
# Purpose: This function controls the flow of the entire joke-telling game. It interacts with the user, asking whether they want to hear a joke and handling their responses.
#     joke = input("Do you want to hear a joke? (yes/no) ").lower()
# Explanation: The program asks the user if they want to hear a joke. Their response is converted to lowercase to make it case-insensitive.
#     if joke == "no":
#         print("Okay, suit yourself!")
#         return
# Explanation: If the user says "no," the program prints a message and exits the function.
#     elif joke == "yes":
#         print("Great, Let's Play!")
# Explanation: If the user says "yes," the program continues and prints a welcome message.
#         while True:
#             question = input(f"Do you want to hear a joke about {', '.join(categories)}? ").lower()
# Explanation: A loop begins, asking the user to choose a joke category from the list categories. The options are printed as a comma-separated string.
#             if question in categories:
#                 tell_joke(question)
# Explanation: If the user’s input matches one of the joke categories, the program calls the tell_joke() function with the selected category.
#             else:
#                 print("Sorry, I don't have a joke about that. Please choose from the available categories.")
# Explanation: If the user provides an invalid category, the program informs them and asks again.
#             joke = input("Do you want to hear another joke or are you finished? (another/finished) ").lower()
# Explanation: After telling a joke, the program asks if the user wants to hear another joke or finish.
#             if joke == "finished":
#                 rate = int(input("Please rate our game 1-10! "))
#                 final_score = rate * 10
#                 print(f"{final_score}% satisfaction rate")
# Explanation: If the user is finished, the program asks for a rating (1-10) and calculates the satisfaction rate.
#                 friend = input("Would you recommend this game to a friend? (yes/no) ").lower()
#                 if friend in ["yes", "maybe"]:
#                     print("Thanks, we appreciate it.")
#                 else:
#                     print("Sorry you did not enjoy it.")
#                 break
# Explanation: The user is asked if they would recommend the game. The program responds accordingly. The loop then ends (break), finishing the joke session.
#             elif joke != "another":
#                 print("Sorry, I didn't understand that. Please type 'another' or 'finished'.")
# Explanation: If the user's response is anything other than "another" or "finished," the program will ask them again for clarification.
# 3. Execution of the program
# categories = ["robbers", "tanks", "pencils"]
# Explanation: A list of available joke categories is defined: "robbers," "tanks," and "pencils."
# jokes(categories)
# Explanation: The jokes() function is called, passing the categories list to it so the user can choose from these categories when asking for jokes.
# Summary of flow:
# The user is prompted if they want to hear a joke.
# If they say "yes," the program asks them to choose a category.
# Based on the choice, the corresponding knock-knock joke is told.
# The user can keep hearing more jokes or finish and rate the game.
