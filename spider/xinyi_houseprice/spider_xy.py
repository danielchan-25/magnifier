import schedule
import requests
import json
import pandas as pd
import datetime
from time import sleep


def main():
    url = 'https://maoming.anjuke.com/esf-ajax/houseprice/pc/trend/report/?city_id=129&id=3294&type=2'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers)

    if response.status_code == 200:
        json_data = json.loads(response.text)
        today_data = json_data["data"]["priceTrend"][0]["area"][0]
        date = f'{datetime.datetime.now().year}-{today_data["date"]}'
        price = today_data['price']

        data = pd.DataFrame({'date': [date], 'price': [price]})
        data.to_csv('XY_HousePrice_1D.csv', mode='a', index=False, header=False)
        print(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - [{date}] 房价为：[{price}]')


schedule.every().day.at("23:50").do(main)
if __name__ == '__main__':
    schedule.run_pending()
    sleep(59)
