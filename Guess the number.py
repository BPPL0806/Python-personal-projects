from random import randint as rint

random_number = rint(1,50)
tries = 0

while True:
    try:

        answer = input("Guess number from 1 to 50: ")
        answer = int(answer)
        tries += 1
        if answer == random_number and tries == 1:
            print("\n" + "You guessed number at first try!")
            break
        elif answer == random_number:
            print("\n" + "Good answer!")
            print("You guessed number at ", tries, " tries!")
            break

        elif random_number < answer:
            print("\n" + "Generated number is smaller than ", answer, ".")
            continue

        elif random_number > answer:
            print("\n" + "Generated number is bigger than ", answer, ".")
            continue

    except ValueError:
        print("It's not a number!" + "\n")
        continue
