import itertools
import string
import time

def brute_force_password(target_password, max_length=4):
    """
    Tries to brute force a password by iterating through all possible
    combinations of characters up to a specified length.
    """
    # Define the character set to use (lowercase, uppercase, digits, and common symbols)
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    
    print(f"Starting brute force for password: '{target_password}'")
    print(f"Max length: {max_length}, Character set size: {len(characters)}")
    
    start_time = time.time()
    attempts = 0

    for length in range(1, max_length + 1):
        # Generate all combinations of the current length
        for guess_tuple in itertools.product(characters, repeat=length):
            guess = ''.join(guess_tuple)
            attempts += 1
            
            # Print progress every 1,000,000 attempts
            if attempts % 1_000_000 == 0:
                elapsed = time.time() - start_time
                print(f"Attempt #{attempts}: '{guess}' (Elapsed: {elapsed:.2f}s)")
            
            if guess == target_password:
                end_time = time.time()
                print("\n" + "="*40)
                print(f"SUCCESS! Password found: '{guess}'")
                print(f"Total attempts: {attempts}")
                print(f"Time taken: {end_time - start_time:.2f} seconds")
                return guess

    end_time = time.time()
    print("\n" + "="*40)
    print("FAILED! Password not found within the given constraints.")
    print(f"Total attempts: {attempts}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    return None

# --- USAGE EXAMPLE ---
if __name__ == "__main__":
    # Get the password to guess from user input
    password_to_guess = input("Enter the password to brute force: ")
    
    # Get the maximum length for the password guess from user input
    try:
        max_password_length = int(input("Enter the maximum length to try (e.g., 4): "))
    except ValueError:
        print("Invalid input. Using default length of 4.")
        max_password_length = 4
    
     # Run the brute force attack
    brute_force_password(password_to_guess, max_password_length)
