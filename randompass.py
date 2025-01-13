import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    
    if length < 1:
        raise ValueError("Password length must be at least 1.")
    
    # Character pools
    char_pool = ""
    if use_letters:
        char_pool += string.ascii_letters  # A-Z, a-z
    if use_numbers:
        char_pool += string.digits  # 0-9
    if use_symbols:
        char_pool += string.punctuation  # Special characters

    if not char_pool:
        raise ValueError("No character types selected. Enable at least one type.")
    
    # Generate password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    """Command-line interface for the password generator."""
    print("Welcome to the Password Generator!")
    try:
        # Get user input for password length
        length = int(input("Enter the desired password length (e.g., 12): "))
        if length < 1:
            raise ValueError("Length must be at least 1.")

        # Get user preferences for character types
        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        # Validate at least one character type is selected
        if not (use_letters or use_numbers or use_symbols):
            print("You must enable at least one character type!")
            return

        # Generate and display the password
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print("\nYour generated password is:")
        print(password)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
