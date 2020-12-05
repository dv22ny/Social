import sys
import time
print("Welcome to the simulation. Please answer a few quick questions to determine yourself.")
age = int(input("How old are you? "))
if age< 10:
    print("Unfortunately, you're too young. Please leave")
    sys.exit()
cool = int(input("How cool are you on a scale of 1 to 10? "))
if cool < 5:
    print("Unfortunately, you're not cool enough to continue. Thank you!")
    sys.exit()
if cool > 10:
    print("Yo buddy did you read the instructions? Bye!")
    sys.exit()
ego = int(input("Do you think you rule over everyone? Please answer 1 for yes and 2 for no."))
if ego == 1:
    print("Your ego is too big. Thank you!")
    sys.exit()
if ego > 2:
    print("Please start again")
girlfriend = int(input("Do you have a girlfriend or boyfriend? Enter 1 for yes and 2 for no. "))
if girlfriend == 2:
    print("No one is willing to date you. Please leave.")
    sys.exit()
if girlfriend > 2:
    print("Yo buddy did you read the instructions? Bye!")
    sys.exit()
time.sleep(0.5)
print("Congrats for making it this far bruv. Almost there!")
time.sleep(2)
siblings = int(input("Do you have any siblings? Please enter the amount that you have (Enter a number from zero to 10) "))
if siblings == 0:
    print("Your parents only conceived one child get out.")
    sys.exit()
if siblings <= 2:
    print("Shaking my head smh bye")
    sys.exit()
if siblings <=10:
    print("Bud OwO 😎")
    time.sleep(2)
else:
    print("Yo buddy did you not read the instructions? Byeeeee")
    sys.exit()
print("Congrats! You have finished")
if age + cool + ego + girlfriend + siblings >= 25:
    time.sleep(3)
    print("Calculating how awesome you are")
    time.sleep(3)
    print("Still calculating, sit tight")
    time.sleep(2)
    print("Bro you're actually the best ngl. Now out lol.")
    sys.exit()
else:
    print("Calculating how awesome you are")
    time.sleep(4)
    print("Eh you're ok")
sys.exit()