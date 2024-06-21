import sqlite3

connection = sqlite3.connect("stock_market.db")
cursor = connection.cursor()

query = """CREATE TABLE user_details (id INTEGER PRIMARY KEY, name VARCHAR(255), age INTEGER, sex CAHR, 
number NUMBER, email VARCHAR(255), pan_no TEXT, balance INTEGER)"""
cursor.execute(query)

query = """CREATE TABLE user_logins (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"""
cursor.execute(query)

query = """CREATE TABLE stock_details (id INTEGER, name TEXT, prize INTEGER, quantity INTEGER)"""
cursor.execute(query)

query = """INSERT INTO stock_details VALUES 
(01, 'Reliance Industries', 2905, 1000),
(02, 'TCS', 3821, 1500),
(03, 'HDFC Bank', 1509, 800),
(04, 'Bharti Airtel', 1326, 700),
(05, 'ICICI Bank', 1107, 1200),
(06, 'SBI', 801, 800),
(07, 'Infosys', 1430, 1000),
(08, 'ITC', 440, 890),
(09, 'Hidustan unilever', 2222, 1300),
(10, 'Bajaj Finance', 6731, 1270);
"""
cursor.execute(query)


connection.commit()
cursor.close()
connection.close()
