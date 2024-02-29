import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "The url of the item to be tracked"

# Enter Your browser info in the headers
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 "
                  "Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br",
    "sec-ch-ua-platform": "Windows",
    "sec-ch-ua": 'Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115',
}

response = requests.get(URL, headers=headers)
ebay_web = response.text
soup = BeautifulSoup(ebay_web, "html.parser")
price = float(
    soup.select_one("div.x-bin-price__content  div.x-price-primary  span.ux-textspans").get_text().split("$")[1])

while True:
    time.sleep(0.1)
    if price < 400:  # instead of the 400 specify the price when you want to be notified
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user="Your email", password="password")
            connection.sendmail(from_addr="Your email", to_addrs="receiver name", msg=f"Subject:Ebay "
                                f"Price "
                                f"Alert!\n"
                                f"\nSevenFriday "
                                f"Men's Q1-03 "
                                f"Q-Series 47.6 "
                                f"Automatic "
                                f"Watch is now "
                                f"${price}\n{URL}")
