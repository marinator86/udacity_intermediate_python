INVALID_PASSWORDS = (
    'password',
    'abc123',
    '123abc',
)

class InvalidPasswordError(ValueError):
    pass

def validate_password(username, password):
    if password == username:
        raise InvalidPasswordError("password equals username")
    if password not in INVALID_PASSWORDS:
        raise InvalidPasswordError("password is not valid")

def create_account(username, password):
    return (username, password)

def checkAndCreate(username, password):
    try:
        validate_password(username, password)
    except InvalidPasswordError as e:
        print(f"Error: {e}")
    else:
        print(f"Created: {create_account(username, password)}")

if __name__ == '__main__':
    # Asking for forgiveness is better than asking for permission
    checkAndCreate('jim', 'jam')
    checkAndCreate('admin', 'password')  # Oh no!
    checkAndCreate('guest', 'guest')  # Oh no!
    #main()

    # other stuff
def main():
    try:
        int(input("Input: "))
    except KeyboardInterrupt as e:
        print("Interrupted!")
        exit()
    except ValueError as e:
        print(f"Exception: {e}")
    else:
        print("else")
        raise BaseException
    finally:
        print("Finally")

