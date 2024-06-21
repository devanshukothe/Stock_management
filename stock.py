from datetime import datetime

def stock(cursor, user_id):

    query = f"""SELECT * FROM user_details WHERE id = {user_id}"""
    user_data = cursor.execute(query).fetchone()

    print(user_data)

    balance = user_data[7]

    while True:
        print("_"*10)
        print("Do you want to ")
        print("1.Buy\n2.Sell")
        try:
            ch = int(input(" : "))
        except ValueError:
            print("-"*10, "\nPlease enter the valid number.\n", "-"*10)
            continue
        else:
            if ch == 1:
                print("_"*10, "All stocks : ", "_"*10)
                query = "SELECT * FROM stock_details;"
                data = cursor.execute(query).fetchall()
                print("Stock_id|Stock_name|Current_Prize|Quantity_Avalible")
                for i in data:
                    for j in i:
                        print(j, "\t", end="")
                    print("")

                print("_"*10, "Your toatl balance : ", balance, " ", "_"*10)
                id = int(input("Enter the id of stock that you want to buy : "))
                quantity = int(input("Enter the  quantity : "))

                for i in data:
                    if id == i[0]:

                        amount = i[2] * quantity
                        if amount < balance:

                            query = f"""UPDATE stock_details SET quantity = {i[3] - quantity} WHERE id = {id};"""
                            cursor.execute(query)

                            query = f"""UPDATE user_details SET balance = {balance - amount} WHERE id = {user_data[0]};"""
                            cursor.execute(query)

                            query = f"""INSERT INTO {"holdings" + str(user_data[0])} VALUES ({id}, '{i[1]}', {i[2]}, {quantity}, {amount});"""
                            cursor.execute(query)

                            date_time = str(datetime.now())
                            bos = "B"

                            query = f"""INSERT INTO {"transcations" + str(user_data[0])} VALUES ({id}, '{i[1]}', '{date_time}', '{bos}', {i[2]}, {quantity}, {amount});"""
                            cursor.execute(query)

                            print("Transcation Successful!")

                        else:
                            print("You dont have enough money!")
                            continue

                return True
            elif ch == 2:
                print("_"*10, "All stocks : ", "_"*10)
                query = f"SELECT * FROM {"holdings" + str(user_data[0])};"
                data = cursor.execute(query).fetchall()
                print("Stock_id|Stock_name|At_Prize|Quantity|Total_amount")
                for i in data:
                    for j in i:
                        print(j, "\t", end="")
                    print("")

                print("_"*10, "Your toatl balance : ", balance, " ", "_"*10)
                id = int(input("Enter the id of stock that you want to sell : "))
                quantity = int(input("Enter the  quantity : "))

                for i in data:
                    if id == i[0]:

                        if quantity < i[3]:

                            amount = i[2] * quantity

                            query = f"""UPDATE stock_details SET quantity = {i[3] + quantity} WHERE id = {id};"""
                            cursor.execute(query)

                            query = f"""UPDATE user_details SET balance = {balance + amount} WHERE id = {user_data[0]};"""
                            cursor.execute(query)

                            query = f"""DELETE FROM {"holdings" + str(user_data[0])} WHERE id = {id};"""
                            cursor.execute(query)

                            date_time = str(datetime.now())
                            bos = "S"

                            query = f"""INSERT INTO {"transcations" + str(user_data[0])} VALUES ({id}, '{i[1]}', '{date_time}', '{bos}', {i[2]}, {quantity}, {amount});"""
                            cursor.execute(query)

                            print("Transcation Successful!")

                        else:
                            print("You dont have enough holdings!")

                return True
            else:
                print("please enter the number 1 or 2.")
