
passwordFile = open('password.txt')
password = passwordFile.read()

print("Enter your password: ")

res = input()

if res == password:
    print("Your in")
else:
    print("try again")