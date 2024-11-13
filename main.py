def crack_password(password):
    guess = 0
    attempts = 0

    while True:
        attempts += 1
        if str(guess) == password:
            print(f"Password '{password}' cracked in {attempts} attempts.")
            break
        guess += 1

if __name__ == "__main__":
    password = input("Enter the password (numeric) to crack: ")
    crack_password(password)
