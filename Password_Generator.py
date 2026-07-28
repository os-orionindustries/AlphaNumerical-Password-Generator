import secrets
import string
import sys
import time

version = "1.0.0"
version_pointer = "-^^^-"

length = 15

valid_flags = {"--help", "-an", "-anp", "-length"}
args = sys.argv[1:]

def alpha_numeric_string(length):
    alpha_numeric = string.ascii_letters + string.digits
    Alpha_numeric_string = ''.join(secrets.choice(alpha_numeric) for _ in range(length))
    with open("Password.txt", "w") as file:
        file.write(Alpha_numeric_string)
    print(f"\033[36m{Alpha_numeric_string}\033[0m")

def alpha_numeric_punctual_string(length):
    alpha_numeric_punctual = string.ascii_letters + string.digits + string.punctuation
    Alpha_numeric_punctual_string = ''.join(secrets.choice(alpha_numeric_punctual) for _ in range(length))
    with open("Password.txt", "w") as file:
        file.write(Alpha_numeric_punctual_string)
    print(f"\033[36m{Alpha_numeric_punctual_string}\033[0m")

def help():
    print()
    print("Usage: py Password_Generator.py -length <number> -an | -anp")
    print("-length <number>: Specify the length of the password (default is 15).")
    print("-an: Generate an alphanumeric password.")
    print("-anp: Generate an alphanumeric password with punctuation.")

print(f"""Use "py Password_Generator.py --help" for more information.""")
print()
print("\033[34m" + r"""
    ____                  ______         
   / __ \____ ___________/ ____/__  ____ 
  / /_/ / __ `/ ___/ ___/ / __/ _ \/ __ \
 / ____/ /_/ (__  |__  ) /_/ /  __/ / / /
/_/    \__,_/____/____/\____/\___/_/ /_/ 
                                         
""" + "\033[0m")
print()
print(f"PassGen Version \033[32m{version}\033[0m")
print(f"Tool By: \033[35mOsmium\033[0m")

if "--help" in sys.argv:
    help()
    sys.exit()

if "--version" in sys.argv and not "-an" in sys.argv and not "-anp" in sys.argv:
    print(f"PassGen Version \033[32m{version_pointer}\033[0m")
    sys.exit()

i = 0
while i < len(args):
    arg = args[i]

    if arg not in valid_flags:
        print(f"\033[31mError: Invalid argument '{arg}'. Use '--help' for usage information.\033[0m")
        sys.exit(1)
    
    if arg == "-length":
        i += 1

        if i >= len(args):
            print("Missing value for '-length'. Please specify a number.")
            sys.exit(1)
        if not args[i].isdigit():
            print(f"\033[31mError: Invalid value for '-length'. Please specify a number.\033[0m")
            sys.exit(1)
        length = int(args[i])
    i += 1

if "-an" in sys.argv and "-anp" in sys.argv:
    print(f"\033[31mError: Cannot use both '-an' and '-anp' flags together. Please choose one.\033[0m")
    sys.exit(1)

if "-an" or "-anp" and not "--help" in sys.argv:
    print(f"\033[33mGenerating password...\033[0m")
    time.sleep(3)

print()

if "-length" in sys.argv:
    length = int(sys.argv[sys.argv.index("-length") + 1])
elif "-length" not in sys.argv:
    length = 15
else:
    print("Please specify a length using '-length <number>'.")



if "-an" in sys.argv:
    alpha_numeric_string(length)
elif "-anp" in sys.argv:
    alpha_numeric_punctual_string(length)
elif "-an" not in sys.argv and "-anp" not in sys.argv:
    alpha_numeric_punctual_string(length)
else:
    print("Please specify either '-an' for alphanumeric or '-anp' for alphanumeric with punctuation.")

