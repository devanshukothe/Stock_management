import sqlite3
from signup import signup
from login import login

connection = sqlite3.connect("stock_market.db")
cursor = connection.cursor()

while True:

    print("*"*10, "Welecome to the  Stock market", "*"*10)
    print("Selecte the operation : ")
    print("1.Login\n2.SignUp\n3.Exit")

    try:
        ch = int(input("Enter your choice : "))
    except ValueError:
        print("-"*10, "\nPlease enter the valid number.\n", "-"*10)
        continue
    else:
        if ch == 1:
            login(cursor)
            connection.commit()
            break
        elif ch == 2:
            signup(cursor)
            connection.commit()
        elif ch == 3:
            print("\nExiting...\n")
            break
        else:
            print("please enter the number between 1 & 3.")
