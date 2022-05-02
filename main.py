import database
import seeding
import threading

def main():

    conn = database.connect()

    seeding.seedStockPrices(conn)







if __name__ == '__main__':
    main()