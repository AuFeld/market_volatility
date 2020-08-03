import backtrader as bt
import datetime 


class VIXStrategy(bt.Strategy):
    
    def __init__(self):
        self.vix = self.datas[0].vixclose
        self.spyopen = self.datas[0].open
        self.spyclose = self.datas[0].close 

    def log(self, txt, dt=None):
        ''' Logging function for this strategy ''' 
        dt = dt or self.datas[0].datetime.data(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def next(self):
        if self.vix[0] > 35:
            self.log('Previous VIX, %.2f' % self.vix[0])
            self.log('SPY Open, %.2f' % self.spyopen[0])

            if not self.position or self.broker.getcash() > 5000:
                size = int(self.broker.getcash() / self.spyopen[0])
                print('Buying {} SPY at {}'.format(size, self.spyopen[0]))
                self.buy(size=size)
