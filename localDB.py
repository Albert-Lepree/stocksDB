import pandas as pd


def main():
    # read csv into a pandas dataframe
    AAPL = pd.read_csv('./data/priceHistory/AAPL.csv')


    # creates connection with stockDB.db file in repo
    conn = create_connection(r"./stockDB.db")


##########################creates priceHistory table#########################################

    # sql_create_priceHistory_table = """  CREATE TABLE IF NOT EXISTS priceHistory (
    #                                     id integer PRIMARY KEY,
    #                                     date date,
    #                                     open float,
    #                                     high float,
    #                                     low float,
    #                                     close float,
    #                                     volume integer
    #                                 );  """
    #
    # create_table(conn, sql_create_priceHistory_table)
#############################################################################################


    # loops i times for length of the AAPL data frame
    # for i in range(len(AAPL)):
    #     create_record(conn, AAPL.iloc[i])
    create_record(conn, AAPL.iloc[0])

###############################################
# Database
###############################################
import sqlite3
from sqlite3 import Error

# connect to database method
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

# create table method
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

# creates a single record in the database
def create_record(conn, record):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """



    # columns of the database
    sql = f''' INSERT INTO priceHistory(date, open, high, low, close, volume)
              VALUES(?,?,?,?,?,{record[5]}) ''' # for some reason volume can only be inserted in this way with an f string

    cur = conn.cursor()
    cur.execute(sql, record[:5])
    conn.commit()


if __name__ == '__main__':
    main()

