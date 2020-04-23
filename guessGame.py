guessTries = 6
guessTries1 = 4
guessTries2 = 3
winNumber = 7
winNumber2 = 17
winNumber3 = 43


try:
    choice = input("Welcome! Would you like to play a game? YES or NO? \nPlease make a choice: ").upper()
    if choice == "NO":
        print("See you soon! Goodbye!!")

    elif choice == "YES":
        print("Lets play a number guessing game")
        choice = input("Please choose a difficulty level \n1) Easy \n2) Medium \n3) Hard \nPlease make a choice: ").upper()

        if choice == "1" or choice == "EASY":
            print("\nGuess a number between 1 - 10 \nYou have 6 tries to guess the correct number \n")
            userChoice = int(input("Enter a guess: "))
            guessTries -= 1

            if userChoice == winNumber:
                print("You got it right")
            elif userChoice != winNumber:
                while guessTries > 0:
                    try:
                        print("That was wrong \nYou have " + str(guessTries) + " tries left")
                        userChoice = int(input("Enter a guess: "))
                        guessTries -= 1
                        if userChoice == winNumber:
                            print("You got it right")
                            break
                        elif guessTries == 0:
                            print("You've used all your tries. Game Over!")
                            break
                    except ValueError:
                        print("This is not a number, Use numbers only!!")

        elif choice == "2" or choice == "MEDIUM":
            print("\nGuess a number between 1 - 20 \nYou have 4 tries to guess the correct number \n")
            userChoice = int(input("Enter a guess: "))
            guessTries1 -= 1

            if userChoice == winNumber2:
                print("You got it right")
            elif userChoice != winNumber2:
                while guessTries1 > 0:
                    try:
                        print("That was wrong \nYou have " + str(guessTries1) + " tries left")
                        userChoice = int(input("Enter a guess: "))
                        guessTries1 -= 1
                        if userChoice == winNumber2:
                            print("You got it right")
                            break
                        elif guessTries1 == 0:
                            print("You've used all your tries. Game Over!")
                            break
                    except ValueError:
                        print("This is not a number, Use numbers only!!")

        elif choice == "3" or choice == "HARD":
            print("\nGuess a number between 1 - 50 \nYou have 3 tries to guess the correct number \n")
            userChoice = int(input("Enter a guess: "))
            guessTries2 -= 1

            if userChoice == winNumber3:
                print("You got it right")
            elif userChoice != winNumber3:
                while guessTries2 > 0:
                    try:
                        print("That was wrong \nYou have " + str(guessTries2) + " tries left")
                        userChoice = int(input("Enter a guess: "))
                        guessTries2 -= 1
                        if userChoice == winNumber3:
                            print("You got it right")
                            break
                        elif guessTries2 == 0:
                            print("You've used all your tries. Game Over!")
                            break
                    except ValueError:
                        print("This is not a number, Use numbers only!!")

        else:
            print("You've made an invalid selection. GoodBye!!")

    else:
        print("You've made an invalid selection. GoodBye!!")
except ValueError:
    print("This is not a number, Use numbers only!!")
