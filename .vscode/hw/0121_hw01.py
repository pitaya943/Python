# coding:utf-8

fruits = ('香蕉', '蘋果', '橘子', '鳳梨', '西瓜')
fruits2 = list(fruits)
print("Tuple:", fruits)
print("List:", fruits2)

fruits2.append('百香果')
print("\nInsert ->", fruits2)
fruits2.remove('蘋果')
print("Delete ->", fruits2)


print("Index of orange is", fruits2.index('橘子'))
