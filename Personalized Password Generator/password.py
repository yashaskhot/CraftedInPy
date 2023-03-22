import random
import string



def generate_password(length=8):
    length=int(input("Enter the password length you want:"))
    if length < 8:
        print("Insecure password length. Generating default 8 character password...")
        length = 8
    
    
    
    # Define a string containing all possible characters
    all_chars = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a password using a random selection of characters
    password = "".join(random.choice(all_chars) for i in range(length))
    
    return password

App=input("Password for which app?: ")
username=input("Enter your username: ")
password = generate_password()
print(password)


# Save the cause and password to a text file
with open("Password Generator\passwords.txt", "a") as file:
    file.write(f"App\Website: {App}\n")
    file.write(f"Username: {username}\n")
    file.write(f"Password: {password}\n\n")

# Print confirmation message
print("Password saved to passwords.txt")
    

