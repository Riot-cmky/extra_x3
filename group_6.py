jokes = ['robber','tank','pencil']
def allJokes(jokes):  
   
    for joke in jokes:
        choice_of_joke = input("Choose from a list of jokes, robbers, tanks, or pencils: ") #asks user to input and choose which joke they want

        if choice_of_joke == "robber": #if user chooses robber joke
            input("Knock Knock ")     #allows user to respond (whos there)
            input("Calder")    #allows user to respond
            print("Calder police - I've been robbed!") #final output
        elif choice_of_joke == "tank": #if user chooses tank joke
            input("Knock Knock ")     #allows user to respond (whos there)
            input("tank")    #allows user to respond    
            print("You are welcome!") #final output
       
        elif choice_of_joke == "pencil":
            input("Knock Knock ")     #allows user to respond (whos there)  
            input("Broken pencil ")   #allows user to respond
            input("Nevermind, it's pointless! ")    #final output
        else:   #if word that is not listed is called
            print("Sorry, we cannot find a joke like that, choose from the list of robber, tank, or pencil. ")
def average_joke_percentage():  
    first = int(input("Rate the our game 1-10: "))# asks user to rate joke
    second = (first * 10)  #converts users satisfaction to a percentage
    print(f"Your satisfaction rate was {second}") #repeats to user
# joke_average2 = sum(joke_average1,third)

    print(f'Your average satisfaction rate was {second}%') #repeats percentage to user




           
allJokes(jokes)
average_joke_percentage()