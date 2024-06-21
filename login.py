import display
from stock import stock

def login(cursor):
    data = cursor.execute("SELECT * FROM user_logins").fetchall()

    while True:
        username = input("Enter your username : ")
        password = input("Enter your password : ")
        for i in data:
            if i[1] == username:
                if i[2] == password:
                    id = i[0]
                    while True:

                        print("*"*10, "Welecome", "*"*10)
                        print("Menu : ")
                        print("1.Stocks\n2.Account\n3.Holdings\n4.Transcations\n5.Exit")

                        try:
                            ch = int(input("Enter your choice : "))
                        except ValueError:
                            print("-"*10, "\nPlease enter the valid number.\n", "-"*10)
                            continue
                        else:
                            if ch == 1:
                                stock(cursor, id)
                            elif ch == 2:
                                display.account(cursor, id)
                            elif ch == 3:
                                display.holdings(cursor, id)
                            elif ch == 4:
                                display.transcations(cursor, id)
                            elif ch == 5:
                                print("\nExiting...\n")
                                return True
                            else:
                                print("please enter the number between 1 & 5.")

        print("-"*10, "\nUsername or Password is  incorrect!\n", "-"*10)
