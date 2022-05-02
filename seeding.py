import pandas as pd
import database

import finpie.price_data as fp
import re

def seedStockTable():
    url = 'https://www.macrotrends.net/stocks/research'
    raw = pd.read_html(url)
    topMarketCap = raw[0]


    for i in range(len(topMarketCap)):
        print('ticker: ', topMarketCap.iloc[i, 0])
        print('company: ', topMarketCap.iloc[i, 1])

        database.insertIntoStockTable(topMarketCap.iloc[i,0], topMarketCap.iloc[i,1])

def seedStockPrices(conn, inclusive, exclusive):
    tickers = database.select_all_stocks()
    tickerList = []

    for ticker in tickers:
        tickerList.append((re.findall('[A-Z]+[-]?[A-Z]?', str(ticker)))[0])



    for j in range(len(tickerList)):
        df = fp.historical_prices(tickerList[j])
        for i in range(len(df)):
            database.insertIntoStockPrices(df.iloc[i], j, conn)


        conn.commit()
        print('Completed: ', tickerList[j])
        c = input("continue?(y/n)")
        if c == 'y':
            pass
        else:
            break


# fill pe table with data
def seedPETable(conn):
    tickerList = getTickers()
    companyList = getCompanies()



    for i in range(len(companyList)):

        url = f'https://www.macrotrends.net/stocks/charts/{tickerList[i]}/{companyList[i]}/pe-ratio'

        print('Ticker: ', tickerList[i])

        df = pd.read_html(url)[0] # date, stockprice, eps, pe

        for j in range(1, len(df)):
            #print(df.iloc[j])
            database.insertIntoPETable(df.iloc[j], i, conn)

        conn.commit()


def seedPSTable(conn):
    tickerList = getTickers()
    companyList = getCompanies()


    for j in range(len(tickerList)):

        url = f'https://www.macrotrends.net/stocks/charts/{tickerList[j]}/{companyList[j]}/price-sales'
        print(url)

        try:
            df = pd.read_html(url)[0]
        except:
            print('error')
            continue

        for i in range(1, len(df)):
            database.insertIntoPSTable(df.iloc[i], j, conn)

        conn.commit()


def getCompanies():
    companies = database.select_all_companies()
    companyList = []

    for company in companies:
        companyList.append((re.findall('[aA-zZ]+[ ]?[&]?[ ]?[aA-zZ]+[ ]?[aA-zZ]+', str(company)))[0])

    #formats string to be used in url
    for i in range(len(companyList)):
        companyList[i] = companyList[i].replace(' & ', '-')
        companyList[i] = companyList[i].replace(' ', '-')

    return companyList

def getTickers():
    tickers = database.select_all_stocks()
    tickerList = []


    for ticker in tickers:
        tickerList.append((re.findall('[A-Z]+[-]?[A-Z]?', str(ticker)))[0])


    for i in range(len(tickerList)):
        # format ticker for the url string
        tickerList[i] = tickerList[i].replace('-', '.')

    return tickerList