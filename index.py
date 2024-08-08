# import numpy as np
import requests
# import xlsxwriter 
import math
# from secrets import API_KEY
# import psycopg2
import SwingTop , SwingBottom,HighSquce,LowSquce
import datetime

stocks = ["ASIANPAINT"]

# conn = psycopg2.connect(database ="trading",
#                         user="postgres",
#                         host ="localhost",
#                         password="123",
#                         port="5432")


# for symbols in stocks:

#     symbol = f"{symbols}.BSE"
#     function = "TIME_SERIES_DAILY"
#     outputsize = "compact"
#     base_url =f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&outputsize={symbol}&apikey={API_KEY}"
#     r = requests.get(base_url)
#     # print(r.csv())
#     data = r.json()
#     print(data)


base_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=RELIANCE.BSE&outputsize=full&apikey=demo"
response = requests.get(base_url)
data = response.json()

start_year = int(input("Start Year: "))
end_year = int(input("End Year: "))


times = data['Time Series (Daily)']


filter_dates=[]
for years in times.keys():
    year,month,date = (years.split('-'))
    # print(year)
    if start_year <= int(year) and int(year) <=end_year:
        filter_dates.append(years)
        
    

dates = []
Highs = []
Low =[]

for items in filter_dates:
    dates.append(items)
    Highs.append(times[items]['2. high'])
    Low.append(times[items]['3. low'])

dates = dates[::-1]
Highs = Highs[::-1]
Low = Low[::-1]

collection_with_high = zip(dates,Highs)
values_of_High = list(collection_with_high)

collection_with_low = zip(dates,Low)
values_of_Low = list(collection_with_low)


High_data= SwingTop.swingTop(values_of_High)
Low_data = SwingBottom.swingBottom(values_of_Low)


High_sequance =  HighSquce.highSquce(High_data)
Low_sequance = LowSquce.lowSquce(Low_data)

Highest = list(zip(High_sequance,High_data))
Lowest = list(zip(Low_sequance,Low_data))


for i,datees in enumerate(zip(Highest,Lowest)):
    print(i,datees)
# for i,datees in enumerate(zip(High_sequance,High_data)):
#     print(i,datees)