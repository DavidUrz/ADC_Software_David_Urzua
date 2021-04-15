# David Urzua A00354893

import random
# limits for random generation number
lower_limit = 1
upper_limit = 30

# variables initialization for game
number = random.randint(lower_limit, upper_limit)
exit_flag = ""
user_number = 0
count = 0
while exit_flag != "exit":
    try:
        user_number = int(input("Guess a number 1-30: "))
        count += 1
    except ValueError as e:
        print("Error: Number not valid: {}".format(e))

    if user_number < number:
        print("too low")
    elif user_number > number:
        print("too high")
    else:
        print("Exactly! the number is: {}".format(number))
        print("tries: {}".format(count))
        # write the attempts in file
        with open("GuessingSteps.txt", "w") as GuessingSteps_file:
            GuessingSteps_file.write("Number of attempts: {}".format(str(count)))
        break
    exit_flag = (input("Type exit to terminate  -  enter to continue\n")).lower()
