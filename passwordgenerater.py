import string
import random

characters = list(string.ascii_letters + string.digits + "!#@$%^&*()")

def generatePassword():
    random.shuffle(characters)
    password = characters[:12]
    return "".join(password)

password = generatePassword()

print(password)