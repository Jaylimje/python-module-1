list1 = []

n = int(input("How many number you want to enter the list: "))

for i in range(n):
    num = int(input("Enter the number: "))
    list1.append(num)
list1.sort()
list2 = set(list1)
list3 = list(list2)
print(list3)
print("the second smallest value in he list: ",list3[1] )