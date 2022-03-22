import myClass

name = input('name: ')
age = int(input('age: '))
height = int(input('height: '))
weight = int(input('weight: '))
Me = myClass.BMI(name, age, height, weight)
Me.getInfo()
