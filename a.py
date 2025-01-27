def get_joke(): # Function gets the type of joke that the user wants to hear
    joke_types = [robbers, tanks, "pencils" ] #list of jokes available

    question = input("Do you want to hear a joke about robbers, tanks, or pencils? ") # Allows user to input if they want to hear a robber, tank, or pencil joke
    if question == "robbers":
            robbers() # Will run if user wanted to hear a joke about robbers
   
    elif question == "tanks":
            tanks() #will run the dialouge for tanks joke


    elif question == "pencils":
        pencils() #will run the dialouge for pencils joke




def want_jokes(): # Function asks user if they want to hear a joke
    joke = input("Do you want to hear a joke? ")
    if joke == "no": # If user didn't want to hear the joke, this will print and the code will end
        print("Okay suit yourself!")
    elif joke == "yes":# If user wanted to hear joke, will run the get_joke() function defined above
        print("Great, Let's Play")
        get_joke()

def finished(): #function asks user to rate the game and whether user would recommen the game
    rate = int(input("Please rate our game 1-10! ")) #ask user to input 1-10
    final_score = int(rate * 10) #takes user rating and times by 10
    print(str(final_score) + " percent satisfaction rate")
    friend = input("Would you recommend this game to a friend? ") #ask user if they would recommend


    if friend == "yes" or friend == "maybe": #takes diff paths depending on user's input
        print("Thanks, we appreciate it. ") #if user answers yes or maybe, this dialouge will run
    else:
        print("Sorry you did not enjoy it. ") #anything else besides yes or maybe will print this dialouge
    return #ends code

def robbers(): # Function runs the dialogue for robbers joke.
    robbers_list = ["Knock Knock ", "Calder ", "Calder police - I've been robbed! "] # list of the dialogue for the robbers joke
    input(robbers_list[0]) # Runs the first element of the list and allows reader to respond/interact with joke
    input(robbers_list[1]) # Runs the second element, input allows user to respond/interact with jokes
    print(robbers_list[2]) # Prints out last piece of joke dialogue. Ends the joke.
    joke = input("Do you want to hear another joke or are you finished? ") # Asks user if they want to continue hearing jokes.
    if joke == "finished": # If user doesn't want to hear anymore jokes, runs finished() and code ends.
        finished()
    elif joke == "yes": # If user still wants to hear jokes, will restart the game
        get_joke()

def tanks(): # Function runs the dialogue for tanks joke.
    tanks_list = ["Knock Knock ", "Tank ", "You are welcome! "] # List of the pieces of dialogue that will run in the tanks joke.
    input(tanks_list[0]) # Prints out the first element in the list above and allows user to interact/respond to joke.
    input(tanks_list[1]) # Prints out the second element in the list above and allows user to interact/respond to joke.
    print(tanks_list[2]) # Prints out the last piece of joke dialogue. Ends the joke.
    joke = input("Do you want to hear another joke or are you finished? ") # Asks user if they want to continue hearing jokes.
    if joke == "finished": # If user does't want to hear anymore jokes, runs finished() and code ends.
        finished()
    elif joke == "yes": # If user still wants to hear jokes, will restart the game
        get_joke()

def pencils(): #Function runs the dialogue for pencils joke
    pencils_list = ["Knock Knock ", "Broken pencil ", "Nevermind, it's pointless! "] # List of pieces of dialoge that will run the pencils joke.
    input(pencils_list[0]) #prints out the first element in the list above and allows user to respond to joke
    input(pencils_list[1]) #prints out the second element in the list and allows user to respond to joke
    print(pencils_list[2]) # Prints out the last piece of joke dialogue. Ends the joke.
    joke = input("Do you want to hear another joke or are you finished? ") # Asks user if they want to continue hearing jokes.
    if joke == "finished": # If user does't want to hear anymore jokes, runs finished() and code ends.
        finished() #runs the code inside finished function
    elif joke == "yes": # If user still wants to hear jokes, will restart the game
        get_joke()

def multi_jokes(**jokes): #function runs the whole game
   


    want_jokes()
    while jokes == "yes": # If statement runs different functions based off of user's answer of yes or no
        get_joke()
    if jokes == "finished":
        finished()
       
multi_jokes() 