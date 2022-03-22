# coding:utf-8

fp = open('test.txt', 'w+')
target = '379 171 23 11 3'
fp.write(target)
fp.seek(0)

copyTarget = fp.read()

# .splite() 以 _ 區分 做成list
# ()中間空白為 '以空白格做區分'
targetList = copyTarget.split()
print('String List: ', targetList)
for index in range(0, len(targetList)):
    targetList[index] = int(targetList[index])

print('Integer List: ', targetList)

total = 0
count = 0  # 跑幾圈
for num in targetList:
    total += num
    count += 1
print('Go through', count, 'numbers &')
print('Total is: ', total)

# output:
# String List:  ['379', '171', '23', '11', '3']
# Integer List:  [379, 171, 23, 11, 3]
# Go through 5 numbers &
# Total is:  587


# .splite() Example:
test = '莊侑/杰/喜歡/林柏/睿'
result = test.split('/')
print('test String:', test)
print('result List', result)

# output:
# test String: 莊侑/杰/喜歡/林柏/睿
# result List ['莊侑', '杰', '喜歡', '林柏', '睿']
