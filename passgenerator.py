import random
import string

def gen_pass(length):
    if length < 8:
        return "Password too short Must Have  at least 8 characters."
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter password length: "))
print("Generated Password:", gen_pass(length))
