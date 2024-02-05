print("Welcome to my Quiz!")

playing = input("Do you want to play my Quiz? ")

if playing != "yes":
    print("Goodbye!")
    quit()

print("Awesome! Let's start :)")

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer == "power supply":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")