import secrets
import string

alphabet = string.ascii_letters + string.digits
random_string = ''.join(secrets.choice(alphabet) for _ in range(15))

with open("Password.txt", "w") as file:
    file.write(random_string)

print(f"\033[36m{random_string}\033[0m")