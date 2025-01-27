joke_list =['robber', 'tanks','pencils']# provided list of jokes


jokeAnswer = input(f"do you want to hear a joke?") # questions the user if they want to hear a joke

def rating(rate):# this function calulates the rating provided by the user, 1-10
    final_score = (rate * 10)
    print(str(final_score) + " percent satisfaction rate")
    friend = input("Would you recommend this game to a friend? ")

    if friend == "yes" or friend == "maybe":# if they recommmend this program to a friend or not
        print("Thanks, we appreciate it. ")
    else:
        print("Sorry you did not enjoy it. ")
    return

def questionReponder(*answer):# here asks the user what type of joke they want to hear
    if jokeAnswer == "yes":
        question2 = input(f"what joke would you like to have? List of Jokes:{joke_list}")


        for joke in joke_list:
            if question2 == 'robber':
                input("Knock Knock")
                input("Calder")
                input("Calder police - I've been robbed!")
                rate = int(input("Please rate our game 1-10! "))# each jokes ends asks the user for their rating
                                                                #then calls it into the rating program above
                return rating (rate)
            elif question2 == 'tanks':
                input("Knock Knock")
                input("Tank ")
                input("You are welcome! ")
                rate = int(input("Please rate our game 1-10! "))
                return rating(rate)
            elif question2 == 'pencils':
                input("Knock Knock")
                input("Broken pencil")
                input("Nevermind, it's pointless! ")
                rate = int(input("Please rate our game 1-10! "))
                return rating(rate)
            else:
                input('Error, Try again')
       
               
questionReponder(jokeAnswer, joke_list) # here calls into the function questionResponder if the user answerd yes, they want to hear a joke. 