import time
import schedule
import requests
import json
import pymysql
import logging

# 日期：2023-11-14
# 作者：陈某
# 功能：信宜房价爬虫

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger()


# 爬取当天的日期和房价
def get_Data():
    url = 'https://maoming.anjuke.com/esf-ajax/houseprice/pc/trend/report/?city_id=129&id=3294&type=2'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    json_data = json.loads(response.text)
    today_data = json_data["data"]["priceTrend"][0]["area"][0]
    date = f'2024-{today_data["date"]}'
    price = today_data['price']
    logger.info(f'{date}的房价为：{price}')
    return date, price


# 将当天的房价写进数据库
def insert_db():
    date, price = get_Data()
    conn = pymysql.connect(host='192.168.2.11', user='root', password='Ba100132087974!@#', database='XY_HousePrice',
                           port=3306)
    cursor = conn.cursor()
    sql = f'INSERT INTO XY_HousePrice_1D (date,price) VALUES ("{date}","{price}");'
    cursor.execute(sql)
    conn.commit()
    cursor.fetchall()
    cursor.fetchone()
    cursor.close()
    conn.close()
    logger.info(f'已将{date},{price}成功写入数据库!')


if __name__ == '__main__':
    logger.info('爬虫已启动，等待23:30运行')
    schedule.every().day.at("23:30").do(insert_db)
    while True:
        schedule.run_pending()
        time.sleep(60)
