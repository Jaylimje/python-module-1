import random
import string

class User:
    def __init__(self, user_id, name, password):
        self.user_id = user_id
        self.name = name
        self.password = password

def generate_password(input_text):

    words = input_text.split()
    
    chosen_words = random.sample(words, min(len(words), 3))
    
    password = ''.join(chosen_words)
    password += ''.join(random.choices(string.digits, k=2))
    password += ''.join(random.choices(string.punctuation, k=2))
    password += ''.join(random.choices(string.ascii_uppercase, k=2))

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

def main():
    try:
        
        user_id = input("Enter user ID: ")
        name = input("Enter name: ")
        input_text = input("Enter some words for password generation: ")

        password = generate_password(input_text)
        
        if len(password) < 8:
            raise ValueError("Password length should be at least 8 characters.")

        user = User(user_id, name, password)

        print("\nUser Details:")
        print("User ID:", user.user_id)
        print("Name:", user.name)
        print("Generated Password:", user.password)
        
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
