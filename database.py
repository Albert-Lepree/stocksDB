import mysql.connector

# connect to database on local host with login
def connect():
    mydb = mysql.connector.connect(
        host="localhost",
        user="finn244",
        password="secret",
        database="finance"
    )

    return mydb



#######################################################
# InsertIntoStockTable: insert record into stock table
# param:
#       ticker: ticker symbol -> 'AAPL'
#       company: company name -> 'Apple'
#######################################################
def insertIntoStockTable(ticker, company):
    conn = connect()

    cur = conn.cursor()

    sql = f"""INSERT INTO stocktable (ticker, company)
            VALUES('{ticker}', '{company}');
            """
    cur.execute(sql)

    conn.commit()

import pandas as pd
# creates a single record in the database
def insertIntoStockPrices(record, id):
    conn = connect()


    date = record.name.date()
    # print(date)


    # print(volume)
    # print(record[:4])
    open = record.open
    high = record.high
    low = record.low
    close = record.close
    volume = int(record.volume)
    print(date, open, high, low, close, volume)


    # columns of the database
    sql = f''' INSERT INTO stockprices(id, date, open, high, low, close, volume)
              VALUES({id + 1}, '{date}',{open},{high},{low},{close},{volume}) ''' # for some reason volume can only be inserted in this way with an f string

    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


# insert record into the PETable
def insertIntoPETable(record, id):
    conn = connect()

    date = record[0]

    eps = record[2][1:]
    eps = float(eps.replace(',', ''))

    pe = float(record[3])

    #date = datetime.datetime.strptime(date, '%Y-%m-%d').date()

    print(date, eps, pe)

    sql = f''' INSERT INTO petable(id, date, eps, pe)
               values({id+1}, '{date}', {eps}, {pe});'''

    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def insertIntoPSTable(record, id):
    conn = connect()

    date = record[0]
    sps = record[2][1:]
    sps = float(sps)
    ps = float(record[3])

    print(id+1, date, ps, sps)

    sql = f'''INSERT INTO pstable(id, date, psRatio, sps)
              VALUES({id + 1}, '{date}', {ps}, {sps})
    '''

    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()




def select_all_stocks():
    """
    Query all rows in the task table
    :param conn: The connection object
    :return:
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT ticker FROM stocktable")

    rows = cur.fetchall()

    return rows

def select_all_companies():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT company from stocktable")

    rows = cur.fetchall()

    return rows


