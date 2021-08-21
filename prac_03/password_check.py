MIN_LENGTH = 2
MAX_LENGTH = 8


def main():
    print("Password must be 2 - 8 characters long")
    password = input("Password: ")
    while not is_valid_password(password):
        print("Password invalid")
        password = input("Password: ")
    print('*' * len(password))


def is_valid_password(password):
    """Determine if the provided password is valid based on length."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    return True



main()

