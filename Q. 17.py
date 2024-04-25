def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
n = int(input("Enter the sequence : "))

sum1 = 0
for i in range(1, 2*n, 2):
    sum1 = sum1 + (i**2)/ fact(i)
    print(f"{i}^2/{i}! +", end=' ')
print("=", sum1)

n1 = int(input("Enter the sequence : "))
sum2 = 0
for j in range(2, 2*n1+1, 2):
    sum2 = sum2 + (j**2)/fact(i)
    print(f"{j}^2/{j}! +", end=' ')
print("=", sum2)


