import random
import string

def generate_password(length=12):
    """Generate a random password."""
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    print("Please specify the length and number of passwords you'd like to generate.")

    # User input for password length and number of passwords
    length = int(input("Enter the length of the password: "))
    num_passwords = int(input("Enter the number of passwords to generate: "))

    # Generate passwords
    passwords = [generate_password(length) for _ in range(num_passwords)]

    # Display generated passwords
    print("\nGenerated Passwords:")
    for password in passwords:
        print(password)

if __name__ == "__main__":
    main()
