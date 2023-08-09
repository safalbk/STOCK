import requests
import pandas  as pd
import json
from tabulate import tabulate
import color_terminal as ct
import color_table as ctab
cap=4911
lcap=4*cap

def find_sector(symbol):
    sector = ""
    with open("nifty50.json","r") as f:
        n50_data = json.loads(f.read())
        n50_data["Nifty50"][symbol]["sector"]
        sector = n50_data["Nifty50"][symbol]["sector"]
    return str(sector)
def fetch_data():
    headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
    res=requests.get(r"https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050",headers=headers)
    advance =""
    decline =""
    nochange =""
    with open("data.json" ,"w") as f:
        f.write(json.dumps(res.json()))
    # print("data saved")


    advances=res.json()['advance']

    advance = advances["advances"]
    decline = advances["declines"]
    nochange = advances["unchanged"]
    sell_data=[]
    buy_data=[]
    all_data=res.json()['data']
    for stock  in all_data:
        # if stock["symbol"] == "DRREDDY":
        #     print("time ",stock["lastUpdateTime"])
        #     print(stock["lastPrice"])
        symbol = stock["symbol"]
        open_value = stock["open"]
        high = stock["dayHigh"]
        low = stock["dayLow"]
        ltp = stock["lastPrice"]
        change = stock["change"]
        p_change = stock["pChange"]
        last_updated_time = stock["lastUpdateTime"]
        if open_value == low:
            sector = find_sector(symbol)
            buy_data.append([symbol, ltp, int(lcap / float(ltp)), sector])
        if open_value == high:
            sector = find_sector(symbol)
            sell_data.append([symbol, ltp, int(lcap / float(ltp)), sector])

    print("")
    print("                                       "+"09-Aug-2023 16:00:00"+"                                                 \n")
    print("                 Nifty 50  ",
          ct.green_font("   Advances : "+advance),
         ct.red_font("  Declines : "+decline),
         "  Unchaged : "+nochange
          )
    print("")
    headers = ["Name", "LTP", "Stocks", "Sector"]
    ctab.green_table(headers,buy_data)
    # tabulate(buy_data, headers=headers, tablefmt="grid")

    headers = ["Name", "LTP", "Stocks", "Sector"]
    print(tabulate(sell_data, headers=headers, tablefmt="grid"))




fetch_data()
input()