import sys
import time
print("Hello! Thank you for taking the test")
time.sleep(2)
print("Here's how you will be scored")
time.sleep(1)
print("Each question will have a rating from 1 to 10. Depending on your rating, you will be grouped into different categories. They range from Friend to Superhero")
time.sleep(3)
name = str(input("What's your name? "))
print("Nice to meet you, " + name)
time.sleep(2)
print("Let's get to know you " + name)
friendship = int(input("Rate the value of friendship on a scale of 1 to 10. "))
time.sleep(1)
family = int(input("Rate the value of family on a scale of 1 to 10"))
time.sleep(1)
life = int(input("Rate your ability to answer questions on a scale of 1 to 10"))
time.sleep(1)
happiness = int(input("Rate your happiness on a scale of 1 to 10"))
time.sleep(1)
academic = int(input("Rate you level of academics on a scale of 1 to 10"))
time.sleep(1)
sport = int(input("How many teams are you in?"))
time.sleep(1)
if friendship + family + life + happiness + academic + sport < 10:
    print("You are someone who is lacking that special someone of something in life. A soulshell is what you are. ")
if friendship + family + life + happiness + academic + sport > 10
    