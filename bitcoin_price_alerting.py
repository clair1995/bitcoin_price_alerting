from bs4 import BeautifulSoup
import pandas as pd
import requests
import notify2
import logging
from fun_bitcoin_alerting import toast_notification_bitcoin
import os

# URL -> download the current price of the bitcoins
URL = "https://www.soldionline.it/quotazioni/criptovalute/bitcoin"                      
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# search for the current price    
results = soup.find("div", class_ ="info")
        
prezzo_bitcoin = (results.find_all('b')[0].text.strip())
prezzo_bitcoin = pd.to_numeric(prezzo_bitcoin.replace(".","").replace(",", "."))

# initialise the d-bus connection
notify2.init("Cryptocurrency rates notifier")
 
# create Notification object
n = notify2.Notification("Crypto Notifier")
    
# Set the urgency level
n.set_urgency(notify2.URGENCY_NORMAL)
    
# Set the timeout
n.set_timeout(5000)

t = toast_notification_bitcoin(notification = n, bitcoin_price = prezzo_bitcoin, treshold = 19000)

if not os.path.exists("Logs"):
    os.makedirs("Logs")
    
logging.basicConfig(level=logging.DEBUG, filename='Logs/test.log', filemode='w')
logging.debug(t)

