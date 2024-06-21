from random import randint

def is_field_ava(cursor, field, i):
    data = cursor.execute("SELECT * FROM user_logins").fetchall()
    for i in data:
        if i[1] == field:
            return False
    return True


def  create_login(cursor):
    while True:
        print("_"*10, "Create your Account", "_"*10)
        username = input("Enter your username : ")
        if  is_field_ava(cursor, username, 1) : 
            password = input("Genrate your password : ")
            pass2 = input("Conform your password : ")
            if password == pass2:
                while True:
                    id = randint(1000, 9999)
                    if is_field_ava(cursor, id,  0):
                        query = f"INSERT INTO user_logins (id, username, password) VALUES ({id}, '{username}', '{password}');"
                        cursor.execute(query)
                        return id
            else:
                print("Your password does not match conform password, please enter again")
        else:
            print("Your username is taken, please enter again.")
    

def signup(cursor):

    id = create_login(cursor)

    while True:
        print("_"*10, "Please fill the  following details to proceed.", "_"*10)
        name = input("Enter your name : ")
        if name.isalpha(): 
            try:
                age = int(input("Enter the age : "))
            except ValueError:
                print("Please enter the valid age.")
                continue
            else:
                print("your gender : ")
                print("1.Male\n2.Female")
                sex = int(input(" : "))
                sex = "M" if sex == 1 else "F"
                try:
                    number = int(input("Enter your phone number : "))
                except ValueError:
                    print("Invalid phone number, enter again")
                    continue
                else:
                    email = input("Enter your email : ")
                    if "@" in email and ".com" in email:
                        pan_no = input("Enter your pan card number : ")
                        balance = 100000
                        break
                    else:
                        print("Enter valid email.")
                        continue

        else:
            print("Invalid name, enter again")
            continue

    query = f"""INSERT INTO user_details VALUES 
    ({id}, '{name}', {age}, '{sex}', {number}, '{email}', '{pan_no}', {balance})"""
    cursor.execute(query)

    query = f"""CREATE TABLE {"holdings" + str(id)} (id INTEGER PRIMARY KEY, name TEXT, prize INTEGER, quantity INTEGER, total INTEGER);"""
    cursor.execute(query)

    query = f"""CREATE TABLE {"transcations" + str(id)} (id, name TEXT, dateandtime TEXT, buyorsell CHAR, prize INTEGER, quantity INTEGER,  total INTEGER);"""
    cursor.execute(query)
    
    print("_"*10, "Your account is created Susseccfully!", "_"*10)
