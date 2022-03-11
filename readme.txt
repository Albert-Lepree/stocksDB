Stock database project

Seeding:
    these functions are used to fill the database using web scraper via macrotrends.net

Database:
    functions used to define the database and insert data gathered from the seeding functions

LocalDB:
    this was an inital test to get an understanding of database creation using a database file "stockDB.db"

SQL-Commands:
    A couple SQL commands used to query, create, and update various aspects of the database

###################################################################################

CREATE TABLE stockTable (
  id int not null auto_increment primary key ,
  ticker varchar(6),
  company varchar(100)
);

drop table stocktable;

###################################################################################

CREATE TABLE peTable (
  id int,
  date date,
  eps float,
  pe float
);

drop table peTable;

###################################################################################

CREATE TABLE psTable (
  id int,
  date date,
  psRatio float,
  sps float,
  sharePrice float
);

drop table pstable;

###################################################################################

CREATE TABLE stockPrices (
  id int,
  date date,
  open float,
  high float,
  low float,
  close float,
  volume bigint
);

drop table stockPrices;

###################################################################################

CREATE TABLE treasuryYields (
    date date,
    2Year float,
    5Year float,
    10year float,
    30year float
);

###################################################################################

INSERT INTO stocktable (id, ticker, company) VALUES
(1 ,'AAPL', 'Apple');

select * from stocktable;
select * from stockprices;

DELETE FROM finance.stockprices WHERE id = 1 AND date = '1980-12-12';

###################################################################################

-- join priceTable and stockTable
Select
    stockPrices.date AS date,
    stocktable.company AS company,
    stockprices.open AS open,
    stockPrices.close AS close
    from stockprices
    inner join stocktable ON stocktable.id = stockPrices.id
    where date > '2018-12-20' and stockPrices.id = 6; -- on dates past this one

###################################################################################

UPDATE stocktable
SET ticker = 'BRK-B'
WHERE ticker = 'BRK.B';


UPDATE stocktable
SET ticker = 'BRK-A'
WHERE ticker = 'BRK.A';

###################################################################################

Select * from stockPrices
where id = 2;

delete from stockPrices where id = 7;

select * from stockPrices order by volume desc;

###################################################################################

Select -- sort by volume descending excluding aapl (it has a lot of volume)
    stockPrices.date AS date,
    stocktable.ticker AS ticker,
    stockprices.open AS open,
    stockPrices.close AS close,
    stockPrices.volume as volume,
    ROUND((close-open)*100/open, 2) as percentChange -- percent change as a column
    from stockprices
    inner join stocktable ON stocktable.id = stockPrices.id
    where stockPrices.id != 1 order by volume desc;

###################################################################################

select * from stockPrices where id = 6 order by date asc;

delete from stockPrices where id = 6;

select * from peTable where pe > 1000;
select * from peTable;


delete from peTable where id <= 25;

SELECT VERSION();

###################################################################################

select
        stocktable.ticker as ticker,
        petable.eps as EPS,
        petable.pe as PE,
        petable.date as DATE
        from petable
        inner join stocktable on stocktable.id = peTable.id
        where date >'2018-01-01' and date <'2019-01-01';

###################################################################################

select * from pstable;

select
        stocktable.ticker as ticker,
        pstable.psRatio as PS,
        pstable.sps as SPS,
        psTable.date as Date
        from pstable
        inner join stocktable on stockTable.id = psTable.id
        where pstable.psRatio>1 and psTable.psRatio<2 and psTable.date > '2019-01-01';

###################################################################################

select stocktable.ticker, pstable.psratio, stockPrices.close, psTable.date
    from stockTable
    inner join pstable on stocktable.id = pstable.id
    inner join stockPrices on stockPrices.date = pstable.date and stockPrices.id = psTable.id
    where pstable.psRatio>1 and psTable.psRatio<2 and psTable.date > '2019-01-01'
    order by date asc;

###################################################################################

select
stocktable.ticker as Ticker,
stockprices.date as Date,
stockPrices.close as Close,
peTable.pe as PERatio,
peTable.eps as EarningsPerShare,
round(stockPrices.close/petable.eps, 2) as calculatedEPS
from stocktable
inner join stockprices
on stockTable.id = stockPrices.id
inner join petable
on stocktable.id = petable.id and stockPrices.date = peTable.date;







