def jokess(joke_list):
    joke_list = []  # Creates an empty list called joke list

    jokes = input("Do you want to hear a joke? ").lower() #asks the user if you want to hear a joke
    if jokes == "no": #if jokes =  no it will carry out this part of code
        print("Okay suit yourself!") #displays okay suit yourself
        return joke_list  # Return the joke list

    while jokes == "yes": # while yes equals jokes the program will keep asking questions while jokes yes
        print("Great, Let's Play!")
        question = input("Do you want to hear a joke about robbers, tanks, or pencils? ").lower() #asks user about what question they would like to hear

        if question == "robbers": # If the variable questions is equal to robbers the function will tell them the robbers joke
            input("Knock Knock ")
            input("Calder")
            print("Calder police - I've been robbed!")
            joke_list.append("robbers") # This adds the joke heard by the user to the list "joke_list" where the jokes will be displayed at the end of the function
        elif question == "tanks": # If the variable questions is equal to tanks the function will tell them the tanks joke
            input("Knock Knock ")
            input("Tanks")
            print("You are welcome!")
            joke_list.append("tanks") # Adds the joke to the list joke_list to display at the end of the function
        elif question == "pencils": # If the variable questions is equal to pencils the function will tell them the pencils joke
            input("Knock Knock ")
            input("Broken pencil ")
            print("Nevermind, it's pointless!")
            joke_list.append("pencils") # Adds the joke to the list joke_list to be displayed at the end of the function
        else:
            print("Sorry, I don't have a joke for that topic.")
            continue  # Skip to the next iteration if the topic is invalid

        jokes = input("Do you want to hear another joke or are you finished? (yes/finished) ").lower()
        if jokes == "finished": # if user inputs that they are done hearing jokes with sequence through this part of the code
            rate = int(input("Please rate our game 1-10! ")) #asks user to rate the game
            final_score = rate * 10
            print(f"{final_score}% satisfaction rate") # converts their answer to how much they enjoyed the game
            friend = input("Would you recommend this game to a friend? (yes/no) ").lower()# asks user if they'd reccomend this to a friend
            if friend == "yes" or friend == "maybe":
                print("Thanks, we appreciate it!") # will display if user does recommend the game to a friend
            else:
                print("Sorry you did not enjoy it.") # Will display if user doesn't reccomend the game to a friend
            break #will stop the while loop now that the user doesn't want to hear jokes anymore

    return joke_list  # Return the joke list for further processing

# Call the function
result = jokess([])
print("Jokes you heard:", result) # Prints out the statement including all the jokes that you have listened to