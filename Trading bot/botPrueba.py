from __future__ import (absolute_import, division, print_function, unicode_literals)
import datetime
from GoldenCross import GoldenCross
import backtrader as bt 
from StochRSI import StochRSIStrategy

if __name__ == '__main__':
    cerebro = bt.Cerebro()


dataDAY = bt.feeds.YahooFinanceCSVData(
    dataname = 'BTC-USD-DAY.csv',
    #do not pass values before this date
    fromdate = datetime.datetime(2018,11,1),
    #do not pass values after this date
    todate= datetime.datetime(2023,11,29),
    reverse = False
)

dataMONTH = bt.feeds.YahooFinanceCSVData(
    dataname = 'BTC-USD-MONTH.csv',
    #do not pass values before this date
    fromdate = datetime.datetime(2018,11,1),
    #do not pass values after this date
    todate= datetime.datetime(2023,11,29),
    reverse = False
)

dataCAKE = bt.feeds.YahooFinanceCSVData(
    dataname = 'CAKE-USD.csv',
    #do not pass values before this date
    fromdate = datetime.datetime(2020,9,30),
    #do not pass values after this date
    todate= datetime.datetime(2022,9,30),
    reverse = False
)

dataORCL = bt.feeds.YahooFinanceCSVData(
    dataname = 'ORCL.csv',
    #do not pass values before this date
    fromdate = datetime.datetime(1995,1,1),
    #do not pass values after this date
    todate= datetime.datetime(2014,1,1),
    reverse = False
)

def run():
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(10000.0)
    saldoInicial = cerebro.broker.getvalue()
    print('Saldo Inicial: %.2f' % saldoInicial)

    cerebro.adddata(dataORCL)
    cerebro.addstrategy(StochRSIStrategy)
    #cerebro.addstrategy(GoldenCross)


    cerebro.broker.setcommission(commission=0.001)
    cerebro.run()
    cerebro.plot()

    saldoFinal= cerebro.broker.getvalue()
    print('Saldo Final: %.2f' % saldoFinal)

    saldoFinal=  (saldoFinal*100/saldoInicial)-100
    print('Porcentaje de ganancias: %.2f' % saldoFinal)

run()