import random

randomnumber = random.randint(1, 10)

while True:
    userinput = int(input("Guess the random number generated: "))

    if userinput == randomnumber:
        print(f"Congratulations! The correct number was {userinput}")
        break
    else:
        yn = input("Wrong :( Would you like to try again? ")
        if yn.lower() == "no":
            break