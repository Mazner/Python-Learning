from turtle import bgcolor


def isEven(num):
    if num % 2 == 0:
        return True

def checkHighestEven(li):
    evens = []
    for item in li:
        if isEven(item):
            evens.append(item)
    return max(evens)
                   
print(checkHighestEven([1,2,3,4,5,6,11,10]))

