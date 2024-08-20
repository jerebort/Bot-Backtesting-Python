import backtrader as bt
 
class StochRSI(bt.Indicator):
    lines = ('stochrsi',)
    params = {
        'period': 14
    }

    def __init__(self):
        period = self.params.period
        rsi = bt.indicators.RSI(self.data, period=period)
        maxrsi = bt.indicators.Highest(rsi, period=period)
        minrsi = bt.indicators.Lowest(rsi, period=period)
        self.lines.stochrsi = (rsi - minrsi) / (maxrsi - minrsi)

class StochRSIStrategy(bt.Strategy):
    def __init__(self):
        self.stochrsi_indicator = StochRSI()   
        self.order_exist = False  

    def next(self):
        previous_stochrsi = self.stochrsi_indicator.lines.stochrsi[-1]
        current_stochrsi = self.stochrsi_indicator.lines.stochrsi[0]
        buy_signal = previous_stochrsi < current_stochrsi and current_stochrsi < 0.2
        sell_signal = previous_stochrsi > current_stochrsi and current_stochrsi > 0.8

        if buy_signal and not self.order_exist:
            print(buy_signal)
            print(f'BUY: {current_stochrsi}')
            self.buy()
            self.order_exist = True

        if sell_signal and self.order_exist:
            print(f'SELL: {current_stochrsi}')
            self.sell()
            self.order_exist = False