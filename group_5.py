def robbers():  # Function to define the robbers joke
    input("Knock Knock ")
    input("Calder")
    print("Calder police - I've been robbed!")

def tanks():  # Function to define the tanks joke
    input("Knock Knock ")
    input("Tank ")
    print("You are welcome!")

def pencils():  # Function to define the pencils joke
    input("Knock Knock ")
    input("Broken pencil ")
    print("Nevermind, it's pointless!")

# List containing the joke topics and their functions
jokes = {"robbers": robbers, "tanks": tanks, "pencils": pencils}

# Main function with parameters
def jokeFunction(initial_question, joke_topics):
    if initial_question.lower() == "no":  # End if the user doesn't want to hear a joke
        print("Ok BYE!")
        return

    while initial_question.lower() == "yes":  # Loop if the user wants jokes
        print("Great, Let's Play!")
        topic = input("Do you want to hear a joke about robbers, tanks, or pencils? ").lower()

        # Check if the topic is valid and call the corresponding joke function
        if topic in joke_topics:
            joke_topics[topic]()  # Call the joke function
        else:
            print("Sorry, I don't have a joke for that topic.")

        # Ask if they want another joke
        initial_question = input("Do you want to hear another joke or are you finished? (yes/finished) ").lower()

    if initial_question == "finished":  # Handle when the user finishes the jokes
        rate = int(input("Please rate our game 1-10! "))
        final_score = rate * 10
        print(f"{final_score}% satisfaction rate")

        friend = input("Would you recommend this game to a friend? (yes/no) ").lower()
        if friend == "yes" or friend == "maybe":
            print("Thanks, we appreciate it!")
        else:
            print("Sorry you did not enjoy it.")

# Initial question to start the program
initial_question = input("Do you want to hear a joke? (yes/no) ")

# Call the function with parameters
jokeFunction(initial_question, jokes)