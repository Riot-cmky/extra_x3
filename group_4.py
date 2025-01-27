#create a function that accepts a list parameter and has iteration
# sequencing and selection
# List of available joke categories

joke_categories = ['robbers', 'tanks', 'pencils']


# Function to tell jokes based on the user's choice

def tell_jokes(joke_categories):

   

    # Start an infinite loop for telling jokes

    while True:

        # Ask the user to choose a joke category and convert to lowercase for case-insensitivity

        joke_choice = input("Please choose a joke category (robbers, tanks, pencils): ").lower()


        # Check if the user's choice is a valid category

        if joke_choice in joke_categories:

            # If the user chose 'robbers', tell a robbers-related joke

            if joke_choice == 'robbers':

                joke = "Why don't robbers ever use social media? Because they hate being tagged!"

            # If the user chose 'tanks', tell a tanks-related joke

            elif joke_choice == 'tanks':

                joke = "Why don't tanks ever get invited to parties? Because they always crash!"

            # If the user chose 'pencils', tell a pencils-related joke

            elif joke_choice == 'pencils':

                joke = "Why did the pencil go to the party? Because it was sharp!"


            # Print the joke

            print(joke)

           

            # Ask the user if they want to hear another joke

            continue_jokes = input("Do you want to hear another joke? (yes/no) ").lower()

            # If the user chooses 'no', break the loop and end the joke session

            if continue_jokes == 'no':

                break

        else:

            # If the user entered an invalid category, show an error message and prompt again

            print("Sorry, we don't have those type of jokes. Please choose from robbers, tanks, or pencils.")

   

    # Ask the user to rate the jokes on a scale of 1 to 10

    rate = int(input("Please rate our jokes from 1-10! "))

    # Calculate the final satisfaction score as a percentage

    final_score = int(rate * 10)

    # Print the final satisfaction rate

    print(f"{final_score} percent satisfaction rate")

   

    # Ask the user if they'd recommend the joke game to a friend

    friend = input("Would you recommend this game to a friend? (choose from yes/maybe/no) ").lower()

    # If the user answers 'yes' or 'maybe', thank them for their feedback

    if friend == "yes" or friend == "maybe":

        print("Thanks, we appreciate it.")

    else:

        # If the user answers 'no', apologize for not meeting their expectations

        print("Sorry you did not enjoy it.")


# Call the function to start the joke interaction

tell_jokes(joke_categories)