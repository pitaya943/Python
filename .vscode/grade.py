# coding=utf-8
import sys

allStudent = []

for i in range(0, 10):
    print(allStudent)
    studentInput = str(input("student:"))
    scoreInput = int(input("score:"))
    if scoreInput < 0 or scoreInput > 100:
        print("Error: Score must be 0 - 100")
        continue
    student = [studentInput, scoreInput]
    allStudent.append(student)
    print(allStudent)
