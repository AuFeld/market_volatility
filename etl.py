import pandas as pd  

spy_vix_src = 'https://raw.githubusercontent.com/hackingthemarkets/vix-strategy/master/spy_vix.csv'
spy_vix = pd.read_csv(spy_vix_src, index_col=0) 
spy_vix.to_csv('/home/aufeld/repo/market_volatility/spy_vix.csv', index=True, header=True)

vix_src = 'https://raw.githubusercontent.com/hackingthemarkets/vix-strategy/master/vix.csv'
vix = pd.read_csv(vix_src, index_col=0)
vix.to_csv('/home/aufeld/repo/market_volatility/vix.csv', index=True, header=True)
