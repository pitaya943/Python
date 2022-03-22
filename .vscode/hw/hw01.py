# coding=utf-8
import sys
import random

isContinue = True
allRecord = {}
playTimes = 0
wholeGuessTimes = 0

while isContinue:

    userName = str(input("Your name: "))
    playTimes += 1
    answer = random.randint(0, 100)
    count = 0
    record = []

    while True:
        print("Hint: answer = ", answer)
        guessNum = int(input("Guess a number: "))
        count += 1
        wholeGuessTimes += 1
        record.append(guessNum)
        if guessNum == answer:
            print("Success!")
            allRecord[userName] = count, record
            input_key = str(input("Continue(Y/N)? "))
            isContinue = True if input_key == 'Y' else False
            if isContinue:
                answer = random.randint(0, 99)
                count = 0
                break
            else:
                break
        elif guessNum > answer:
            print("Bigger than answer\t", "Error!\t*" + str(count))
            continue
        elif guessNum < answer:
            print("Smaller than answer\t", "Error!\t*" + str(count))

print()
for user in allRecord.items():
    print("User & Guess times & Guess record\n", user)
print("Average GuessTimes: ", wholeGuessTimes / playTimes, " times\n")
