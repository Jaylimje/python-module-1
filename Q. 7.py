num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))

for i in range(1,num1):
    if num1%i == 0 and num2%i == 0:
        GCD = i
print(f"the GCD of {num1} and {num2} is {GCD}.")