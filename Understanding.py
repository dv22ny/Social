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
gender = str(input("Are you a boy or a girl? "))
if gender == "boy" or gender == "Boy":
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
    q1 = int(input("How important do you think a girl's beauty is? 1 for lowest, 10 for highest. "))
    time.sleep(1)
    print("Muchas Gracias")
    q2 = int(input("How important do you think a girl's body is? 1 for lowest, 10 for highest. "))
    time.sleep(1)
    print("Again, Muchas Gracias")
    q3 = int(input("How important do you think a girl's economic status is? 1 for lowest, 10 for highest. "))
    time.sleep(1)
    q4 = int(input("How important is a girl's personality? 1 for lowest, 10 for highest"))
    time.sleep(1)
    q5 = int(input("How important is a girl's family? 1 for lowest, 10 for highest"))
    time.sleep(1)
    print("Ok, thank you for taking this quiz. We are now analyzing your results")
    if q1 + q2 + q3 + q4 + q5 <= 10:
        print: ("Your perfect girl is Amber Heard. She's shallow on the inside and pretty on the outside")
    if q1 + q2 + q3 + q4 + q5 > 10  and q1 + q2 + q3 + q4 + q5 <= 20 :
        print: ("Your perfect girl is Beyonce. She's decent looking, with a mild character")
    if q1 + q2 + q3 + q4 + q5  > 20 and  q1 + q2 + q3 + q4 + q5 <= 30 :
        print: ("Your perfect girl is Selena Gomez. She's hot on the outside, and perfect on the inside also")
    if q1 + q2 + q3 + q4 + q5 > 30 and q1 + q2 + q3 + q4 + q5 <= 40 :
        print: ("Your perfect girl is Jennie, from Blackpink. She's all-around perfect")
else:
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
    q1 = int(input("How important do you think a guy's handosmeness is? 1 for lowest, 10 for highest. "))
    time.sleep(1)
    print("Muchas Gracias")
    q2 = int(input("How important do you think a guy's body is? 1 for lowest, 10 for highest. "))
    time.sleep(1)
    print("Again, Muchas Gracias")
    q3 = int(input("How important do you think a guy's economic status is? 1 for lowest, 10 for highest. "))
    time.sleep(1)
    q4 = int(input("How important is a guy's personality? 1 for lowest, 10 for highest"))
    time.sleep(1)
    q5 = int(input("How important is a guy's family? 1 for lowest, 10 for highest"))
    time.sleep(1)
    print("Ok, thank you for taking this quiz. We are now analyzing your results")
    if q1 + q2 + q3 + q4 + q5 <= 10:
        print: ("Your perfect guy is Johnny Depp. He's shallow on the inside and pretty on the outside")
    if q1 + q2 + q3 + q4 + q5 > 10  and q1 + q2 + q3 + q4 + q5 <= 20 :
        print: ("Your perfect guy is Kevin Hart. He's decent looking, with a mild character")
    if q1 + q2 + q3 + q4 + q5  > 20 and  q1 + q2 + q3 + q4 + q5 <= 30 :
        print: ("Your perfect guy is Harry Styles. He's hot on the outside, and perfect on the inside also")
    if q1 + q2 + q3 + q4 + q5 > 30 and q1 + q2 + q3 + q4 + q5 <= 40 :
        print: ("Your perfect guy is V, from BTS. He's all-around perfect")