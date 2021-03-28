#David Urzua A00354893
#imports
import random
#limits for random generation number
lowerLimit = 1
upperLimit = 30

#variables initialization for game
number = random.randint(lowerLimit, upperLimit)
exitFlag = ""
userNumber = 0
count = 0
while exitFlag != "exit":
    try:
        userNumber = int(input("Guess a number 1-30: "))
        count += 1
    except ValueError as e:
        print("Error: Number not valid: {}".format(e))

    if userNumber < number:
        print("too low")
    elif userNumber > number:
        print("too high")
    else:
        print("Exactly! the number is: {}".format(number))
        print("tries: {}".format(count))
        #write the attempts in file
        with open("GuessingSteps.txt", "w") as GuessingSteps_file:
            GuessingSteps_file.write("The number of attempts was: {}".format(str(count)))
        break
    exitFlag = (input("Type exit to terminate  -  enter to continue\n")).lower()
