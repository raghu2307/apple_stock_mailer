import requests
import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def get_apple_stock_price():
    url = "https://query1.finance.yahoo.com/v8/finance/chart/AAPL"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    data = response.json()
    price = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
    return price

def send_email(price):
    sender = os.getenv("SENDER_EMAIL")
    password = os.getenv("SENDER_PASSWORD")
    receiver = os.getenv("RECEIVER_EMAIL")

    body = f"Apple (AAPL) current stock price: ${price:.2f} USD"
    msg = MIMEText(body)
    msg["Subject"] = "AAPL Stock Price Update"
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
    print(f"Email sent! Price was ${price:.2f}")

if __name__ == "__main__":
    price = get_apple_stock_price()
    send_email(price)