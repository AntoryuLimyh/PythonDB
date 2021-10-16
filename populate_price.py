#https://app.alpaca.markets/paper/dashboard/overview

import config
import sqlite3
import alpaca_trade_api as tradeapi


connection = sqlite3.connect('stock.db')

cursor = connection.cursor ()

#Query select all id,symbol,company and exchange from stock TABLE
cursor.execute("""SELECT id,symbol, company, exchange FROM stock""")

rows = cursor.fetchall()


#This is done so that the price data can get the stock id by referring to the stock symbol
symbols=[]
stock_dict={}

for row in rows:
    #print('id :',row[0],'symbol :',  row[1],'company :' ,row[2],'exchange :',row[3])
    symbol = row[1]
    symbols.append(symbol)
    stock_dict[symbol] = row[0]


#print(stock_dict)




api = tradeapi.REST(config.API_ID,config.API_KEY,base_url = 'https://paper-api.alpaca.markets')

#https://github.com/alpacahq/alpaca-trade-api-python

#Please note that the API is throttled, currently 200 requests per minute, per account (API Limitation)
chunk_size = 199
for i in range(0, len(symbols), chunk_size):
    symbol_chunk = symbols[i:i+chunk_size]

    barsets = api.get_barset(symbol_chunk, 'day')

    for symbol in barsets:
        print(f"processing symbol {symbol}")
        for bar in barsets[symbol]:
            stock_id = stock_dict[symbol]
            cursor.execute("""INSERT INTO stock_price (stock_id, date, open, high, low, close, volume) VALUES (?, ?, ?, ?, ?, ?, ?) """, (stock_id, bar.t.date(), bar.o, bar.h, bar.l, bar.c, bar.v))
            
           
connection.commit()



