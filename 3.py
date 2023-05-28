import random

days = int(input("input days: "))

def ListCreation(num):
    list1 = []
    for i in range(days):
        list1.append(random.randint(-50, 50))
        i += 1
    return list1

def PrintPositive(list):
    newList = []
    for i in range(len(list)):
        if list[i] > 0:
            newList.append(list[i])
        i += 1
    print(newList)

PrintPositive(ListCreation(days))