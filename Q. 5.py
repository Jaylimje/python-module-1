string = input("Enter the single string: ")

if len(string) > 2:

    if string.endswith('ing'):
        string = string + 'ly'

    else:
        string = string + 'ing'

print(string)