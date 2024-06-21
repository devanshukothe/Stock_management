def account(cursor, id):
    query = f"SELECT * FROM user_details WHERE id = {id};"
    data = cursor.execute(query).fetchall()[0]
    print("id  : ", data[0])
    print("name  : ", data[1])
    print("age  : ", data[2])
    print("gender  : ", data[3])
    print("phone number  : ", data[4])
    print("email  : ", data[5])
    print("pan card number  : ", data[6])
    print("total balance  : ", data[7])

def holdings(cursor, id):
    query = f"SELECT * FROM {"holdings" + str(id)};"
    data = cursor.execute(query).fetchall()
    if len(data) != 0:
        print("Stock_id|Stock_name|At_Prize|Quantity|Total_amount")
        for i in data:
            for j in i:
                print(j, "\t", end="")
            print("")
    else:
        print("Sorry! You have no holdings.")

def transcations(cursor, id):
    query = f"SELECT * FROM {"transcations" + str(id)};"
    data = cursor.execute(query).fetchall()
    if len(data) != 0:
        print("Stock_id|Stock_name|Date&Time|BuyOrSell|At_Prize|Quantity|Total_amount")
        for i in data:
            for j in i:
                print(j, "\t", end="")
            print("")
    else:
        print("Sorry! You have not buy or sell anything yet.")
        