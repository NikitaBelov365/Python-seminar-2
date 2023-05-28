import random

days = int(input("input days: "))

def ListCreation(num):
    list1 = []
    for i in range(days):
        list1.append(random.randint(-50, 50))

    return list1

def PrintPositive(list):
    sumPosititve = 0
    maxSum = 0
    for i in range(len(list)):
        if sumPosititve > maxSum:
            maxSum = sumPosititve
        if list[i] > 0:
            sumPosititve +=1
        else:
            sumPosititve = 0

    print(maxSum)


list1 = ListCreation(days)
print(list1)
PrintPositive(list1)