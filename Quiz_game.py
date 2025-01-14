print("Welcome To the Game !!")

playing = input("Do you want to play this game ??")

if playing.lower() != "yes":
    quit()

print("Okay !, Lets play :) !!")
score = 0

answer = input("What does CPU stand for ?").lower()
if answer == "central processing unit":
    print('Correct')
    score += 1
else:
    print("Incorrect !")

answer = input("What does GPU stand for ? ").lower()
if answer == "graphics processing unit":
    print('Correct')
    score += 1
else:
    print("Incorrect !")

answer = input("What does RAM stands for ? ").lower()
if answer == "random access memory":
    print('Correct')
    score += 1
else:
    print("Incorrect !")

answer = input("What does ROM stands for ? ").lower()
if answer == "read only memory":
    print('Correct')
    score += 1
else:
    print("Incorrect !")

answer = input("What does PSU stands for ? ").lower()
if answer == "power supply":
    print('Correct')
    score += 1
else:
    print("Incorrect !")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/5)*100) + " % .")
