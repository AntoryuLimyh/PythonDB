import sqlite3

connection = sqlite3.connect('stock.db')

cursor = connection.cursor()

#Indicate the table you wish to drop

cursor.execute("""
        DROP TABLE stock_price

""")

cursor.execute("""
    DROP TABLE stock
""")

connection.commit()