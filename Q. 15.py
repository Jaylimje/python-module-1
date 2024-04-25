num = int(input("Enter the number: "))

a = 0
b = 1

for i in range(0, num+1):

    if i<=1:
        c = i
    else:
        c = a + b
        a = b
        b = c

    print(c, end=' ')