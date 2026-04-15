import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
from datetime import datetime, timedelta

def scrap_data():
    base_url = "http://quotes.toscrape.com/page/{}/"
    data = []

    for page in range(1, 6):  # scrape 5 pages
        url = base_url.format(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")

        for q in quotes:
            author = q.find("small", class_="author").text
            
            # Convert to sales-like data
            sales_amount = random.randint(100, 1000)
            order_date = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 180))

            data.append({
                "customer_id": author,
                "order_date": order_date,
                "sales_amount": sales_amount
            })

    df = pd.DataFrame(data)
    df.to_csv("sales_data.csv", index=False)

    print("Scraped & transformed data saved!")

if __name__ == "__main__":
    scrap_data()

    