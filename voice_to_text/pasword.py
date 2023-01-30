import random
import string

def generate_password(num_letters, num_symbols, num_digits):
    password = ""

    # Add letters to password
    for i in range(num_letters):
        password += random.choice(string.ascii_letters)

    # Add symbols to password
    for i in range(num_symbols):
        password += random.choice(string.punctuation)

    # Add digits to password
    for i in range(num_digits):
        password += random.choice(string.digits)

    # Shuffle password to increase randomness
    password_list = list(password)
    random.shuffle(password_list)
    password = "".join(password_list)

    return password

# Get user input for number of letters, symbols, and digits
num_letters = int(input("How many letters do you want in your password? "))
num_symbols = int(input("How many symbols do you want in your password? "))
num_digits = int(input("How many digits do you want in your password? "))

# Generate password
password = generate_password(num_letters, num_symbols, num_digits)

# Print password
print("Your generated password is:", password)
