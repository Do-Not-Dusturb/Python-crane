import itertools
import string

def crack_password(password):
    characters = string.ascii_letters + string.digits + string.punctuation  # Include letters, digits, and special characters
    attempts = 0

    for length in range(1, len(password) + 1):
        for guess in itertools.product(characters, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
                print(f"Password '{password}' cracked in {attempts} attempts.")
                return

if __name__ == "__main__":
    password = input("Enter the password to crack: ")
    crack_password(password)
