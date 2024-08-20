# Sorting a list
mylist = [23, 5, 30, -8, 10, 15, 50, 31, -22, 22]
length = len(mylist)
for i in range(length):
    for j in range(length-i-1):
        if mylist[j] > mylist[j+1]:
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
print(mylist)            