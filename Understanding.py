import sys
import time
name = str(input("What is your name? "))
print("Hello, " + name)
time.sleep(1)
print("Nice to meet you")
age = int(input("How old are you?" ))
if age < 13:
    print("Unfortunately, you're too young for this. Thank you!")
    time.sleep(1)
    sys.exit
elif age >= 13 or age <= 15:
    oui = str(input("This may contain sensitive material. Would you like to continue? "))
    if oui == 'Yes' or oui == 'yes' :
        print("You have chosen to continue, nice!")
    else:
        print("You have chosen to leave, totally ok, tata!")
        time.sleep(1)
        sys.exit()
else:
    print("Yeah buddy!")
time.sleep(1)
print("Aight peeps let's get into this shall we")
time.sleep(1)
print("Here's how it's going to work")
time.sleep(1)
print("You're going to be asked a series of questions, which will help you determine what kind of girl is ideal for you OwO")
time.sleep(2)
buddy_cool = str(input("Buddy are you cool with that?"))
if buddy_cool == 'Yes' or  buddy_cool == 'yes' :
    print("Ok bet let's start")
    time.sleep(2)
else:
    print("OK that's fine you suck but bye")
    time.sleep(1)
    sys.exit()
q1 = int(input("How important do danyou think a girl's beauty is? 1 for lowest, 10 for highest. "))
time.sleep(1)
print("Muchas Gracias")
q2 = int(input("How important do you think a girl's body is? 1 for lowest, 10 for highest. "))
time.sleep(1)
print("Again, Muchas Gracias")
