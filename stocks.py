DAX_kuerzel = ["ADS", "ALV", "BAS", "BAYN", "BMW", "BEI", "CBK", "CON", "DAI",
               "DBK", "DB1", "LHA", "DPW", "DTE", "EOAN", "FME", "FRE", "HEI",
               "HEN3", "IFX", "SDF", "LXS", "LIN", "MRK", "MUV2", "RWE", "SAP",
               "SIE", "TKA", "VOW3"]

import bs4 
import requests
from bs4 import BeautifulSoup


def get_price():
    r = requests.get('https://de.finance.yahoo.com/quote/DAI.DE?p=DAI.DE')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    price = soup.find_all("div", {"class" : "My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
    return price

#while True:
#    print("current Price is " + str(get_price()))
    


def get_priceDE(kuerzel):
    kuerzel = kuerzel+".DE"
    r = requests.get('https://de.finance.yahoo.com/quote/{}?p={}'.format(kuerzel,kuerzel))
    soup = bs4.BeautifulSoup(r.text,"lxml")
    price2 = soup.find_all("div", {"class" : "My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
    return price2
    

def get_all_DAX_prices():

    price_list = []
    
    for x in DAX_kuerzel:
        price = get_priceDE(x)
        price_list.extend([x, price])
    
    return price_list

print(get_all_DAX_prices())
