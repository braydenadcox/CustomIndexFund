import numpy as np
import pandas as pd
import requests
import xlsxwriter as xw
import math
import yfinance as yf

stocks = pd.read_csv("sp500info.csv")

investment = float(input("Amount invested: ")) / 500

stockCheck = input("Stock ticker: ")

def find_symbol(company_name, df):
    matches = df[df['Security'].str.contains(company_name, case=False, na=False)]
    if not matches.empty:
        return matches.iloc[0]['Symbol']
    else:
        return None
    
value = find_symbol(stockCheck, stocks)
price = yf.Ticker(value)
data = price.info
stockVal = data["currentPrice"]
print(stockVal)

shareVal = round((investment / stockVal), 2)
print("You currently own " + str(shareVal) + " shares of " + stockCheck)





