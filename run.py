import backtrader as bt
import os
from vix_strategy import VIXStrategy
import pandas as pd 


cerebro = bt.Cerebro()
cerebro.broker.setcash(100000)

class SPYVIXData(bt.feeds.GenericCSVData):
    lines = ('vixopen', 'vixhigh', 'vixlow', 'vixclose')

    params = (
        ('dtformat', %Y-%m-%d'), 
        ('date', 0), 
        ('spyopen', 1),
        ('spyhigh', 2),
        ('spylow', 3), 
        ('spyclose', 4), 
        ('spyadjclose', 5), 
        ('spyvolume', 6), 
        ('vixopen', 7), 
        ('vixhigh', 8), 
        ('vixlow', 9), 
        ('vixclose', 10)
    )

spy_vix_src = 'https://raw.githubusercontent.com/hackingthemarkets/vix-strategy/master/spy_vix.csv'
vix_src = 'https://raw.githubusercontent.com/hackingthemarkets/vix-strategy/master/vix.csv'
spy_vix = pd.read_csv(spy_vix_src, index_col=0) 
vix = pd.read_csv(vix_src, index_col=0)

spyVixDataFeed = SPYVIXData(dataname=spy_vix)
vixDataFeed = VIXData(dataname=vix)
cerebro.adddata(spyVixDataFeed)
cerebro.adddata(vixDataFeed)

cerebro.addstrategy(VIXStrategy)

cerebro.run()
cerebro.plot(volume=False)