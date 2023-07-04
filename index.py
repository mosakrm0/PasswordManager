from cryptography.fernet import Fernet



'''
def writeKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as keyFile:
        keyFile.write(key)

writeKey()
'''

def LoadKey():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = LoadKey()
fer = Fernet(key)

def view():
    with open('Password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split('|')
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())
        

def add():
    print("Enter UserName : ")
    UserName = input(" > ")
    print("Enter Password : ")
    pwd = input(" > ")

    with open('Password.txt' , 'a') as f:
        f.write(f"{UserName}|{(fer.encrypt(pwd.encode())).decode()}\n")

    

while True:
    UserInput = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if UserInput == "q":
        break

    elif UserInput == "view":
        view()
    elif UserInput == "add":
        add()
    else:
        print("Invalid Input.")
        continue