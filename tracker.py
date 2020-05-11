import requests
from bs4 import BeautifulSoup
import smtplib
import time

def check_price():
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()

    raw_price_array = list(price)
    price_array = []
    for number in raw_price_array:
        if number.isdigit():
            price_array.append(number)


    price_array.pop(-1)
    price_array.pop(-1)
    converted_price = ""
    converted_price = float(converted_price.join(price_array))

    print(converted_price)
    print(title.strip())

    if(converted_price < 10995):
        send_mail()

def send_mail():
    server = smtplib.SMTP('qwer5t.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    subject = 'Price drop'
    body = 'The price on your recently marked item dropped'

    msg = f"Subject: {subject}\n\n{body}"

    server.quit()




