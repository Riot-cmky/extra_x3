def tell_jokes(): #defines the function to intiate the beginning part
    joke = input("Do you want to hear a joke? Y or N? ") #asks the user if they want to hear a joke, uses y or n to make sure an invalid input is less likely
    if joke == "N": # they say no, move on with the ending part of the program
        print("Okay, suit yourself!")
        return #return the function
    else:
        while joke == "Y": #if the user says Y, then the program will run entirely, thius also makes it so if the user says Y to the question if they want to hear another joke, it'll loop
            print("Great, Let's Play")
            question = input("Do you want to hear a joke about robbers, tanks, or pencils? Please answer with: 'robbers', 'tanks', or 'pencils'. ") #asks for input and gives options to reeduce chances of an invalid input
            if question == "robbers": #if they say robbers, commence thew robbers section
                input("Knock Knock ") # since there are many capitlization and wording variation of these answers, any answer will let the program continue
                input("Calder ")
                print("Calder police - I've been robbed!") # program finishes this section
            elif question == "tanks": #these next ilnes of code repeat what this first one did, just different outcomes for each category the user chose
                input("Knock Knock ")
                input("Tank ")
                input("You are welcome!")
            elif question == "pencils":
                input("Knock Knock ")
                input("Broken pencil ")
                input("Nevermind, it's pointless!")
            else: #here make it so that if the user responds with an option, possibly due to a typo, it causes it to repeat the question
                print("Sorry, I didn't understand that choice. Please choose 'robbers', 'tanks', or 'pencils'.")
            joke = input("Do you want to hear another joke? Y or N? ") #once this section of the program finishes, it asks if the user wants another joke, which ensures a loop
        if joke == "N": #if they say no, it'll continue to the next part
            print("No worries!")
def rate_game(prompt, rating_prompt, invalid_input_msg, satisfaction_msg):
    rate_input = input(prompt) #here we use a parameter to ask if they want to rate the game which will be called later
    if rate_input.upper() == "Y": #we use ..upper to make it case insensitive and then......
        while True: #initiate the loop/
            rate_input = input(rating_prompt) #the parameter ratinbg prompt will be called later on to make this work
            rate = int(rate_input)  #then the input is converted into an integer to then check if....
            if 1 <= rate <= 10:  #......it is within the range and to be able to multiply it tro convert it into a percentage
                final_score = rate * 10  
                print(f"{final_score}% {satisfaction_msg}")   #then we print the results by calling the parameters later
                break
            else:
                print(invalid_input_msg)  # and the parameter here is called to ensure it is a loop and that any invalid answer is given another chance to retry
    else:
        print("No rating provided.")
def recommend_game(): # the next definition here then shows whether the user wants to recommend the game to someone else
    recommend_input = input("Would you recommend this game to a friend? Y or N? ") #the input part
    if recommend_input == "Y": # if they said yes, it'll show appreciation
        print("Thanks, we appreciate it!")
    elif recommend_input == "N": # if they sday no, they apologize
        print("Sorry you did not enjoy it.")
    else:
        print("Invalid input, no recommendation received.") #invalid inputs are then redirected to a loop here, here it makes it so any error are acknnowledged
tell_jokes()
rate_game("Would you like to rate the game? Y or N?", "Please rate our game 1-10!", "Please enter a number between 1 and 10.", "satisfaction rate") #here we call back the parameters from it's function
recommend_game()