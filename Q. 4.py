a = input("Enter the first string: ")
b = input("Enter the second string: ")
c = a+" "+b

print("your original string: "+ c)

a_swap = b[0:2] + a[2:]
b_swap = a[0:2] + b[2:]

z= a_swap + " " + b_swap
print("your string after swapping: " + z )
