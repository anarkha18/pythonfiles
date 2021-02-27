# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over

n = 18
number_of_guesses = 1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses <= 9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number < 18:
        print("you enter less number please input greater number.\n")
    elif guess_number > 18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses, "no.of guesses he took to finish.")
        break
    print(9 - number_of_guesses, "no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if (number_of_guesses > 9):
    print("Game Over")

#############
# my solution

n = 18
g = 1
while (g <= 5):
    i = int(input("enter the no: "))
    if i == n:
        print("yes u predicted crct")
        break
    else:
        while (i != n):
            if i > 18:
                print("ur close","gussesleft:",5-g)
            else:
                print("hmnn lil far","gussesleft",5-g)
            break
    g = g + 1
    continue
    break
print("ur out of chances")




