Python - Create SQL DB and link it to Alpaca API for US stock symbol and its associated price


##### API
Alpaca API
https://alpaca.markets/


##### To check the respective symbol and its associated price via the SQL Command
`SELECT S.symbol, P.date, P.open, P.high, P.low, P.close 
    FROM stock_price P JOIN stock S
    on P.stock_id = S.id
    WHERE S.symbol = 'FB'
    ORDER BY P.date`


