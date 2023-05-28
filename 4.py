import random

def ListCreation(num):
    list1 = []
    for i in range(num):
        list1.append(random.randint(1, 30))
    print(list1)
    return list1

def Select(list):
    list.sort()
    print(list)
    print(list[0], list[-1])

arbuzlar = int(input('arbuzlar: '))
Select(ListCreation(arbuzlar))