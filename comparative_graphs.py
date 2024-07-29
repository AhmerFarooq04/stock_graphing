import numpy as np
import pandas as pd
import math
import requests
from scipy import stats
import matplotlib.pyplot as plt
import yfinance as yf
import datetime

stocks = input("what stocks do you want to compare? (separate by commas) ")
ticker = stocks.split(",")
data = yf.download(ticker, period="5y")
close=data.loc[:,"Close"].copy()
percentchange = close.div(close.iloc[0]).mul(100).sub(100)
plt.style.use("seaborn-v0_8-bright")
percentchange.plot(figsize=(15,8),fontsize=12)
plt.grid()
plt.show()