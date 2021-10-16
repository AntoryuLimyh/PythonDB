#https://app.alpaca.markets/paper/dashboard/overview

import config
import sqlite3
import alpaca_trade_api as tradeapi


connection = sqlite3.connect('stock.db')

cursor = connection.cursor ()

api = tradeapi.REST(config.API_ID,config.API_KEY,base_url = 'https://paper-api.alpaca.markets')

#https://alpaca.markets/docs/api-documentation/api-v2/assets/
counters = api.list_assets()


#List all the symbols in the database (select * from stock)
cursor.execute("""SELECT symbol, company, exchange FROM stock""")

rows = cursor.fetchall()

#for row in rows:
#  print(row)

symbols = [row[0] for row in rows] # symbol list comprehension


 

#Insert Symbol, Company and Exchange details into database with conditions 
for counter in counters:
  try:
     if counter.status =='active' and counter.tradable and counter.symbol not in symbols: 
        #print(counter)
        #print(counter.symbol ,'|', counter.name ,'|', counter.exchange ,'|')
        cursor.execute("INSERT INTO stock (symbol, company,exchange) VALUES (?, ?, ?)", (counter.symbol, counter.name,counter.exchange))
  except Exception as e:
         print(counter.symbol) 
         print(e)      

#Commit the changes or updates into the SQL DB
connection.commit()