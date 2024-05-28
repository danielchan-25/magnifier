import requests
import streamlit as st
from bs4 import BeautifulSoup
from function.refresh import prevent_malicious_refresh


def get_data():
    url = 'https://weibo.cn/pub/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')

    news_list = []  # 用于存储文字

    for link in links:
        if link.text == '登录' or link.text == '注册' or link.text == '反馈' or link.text == '客户端' or link.text == '京ICP备12002058号':
            pass
        else:
            news_list.append(link.text)
    return news_list


if __name__ == '__main__':
    st.title('微博热点')

    prevent_malicious_refresh()
    news_list = get_data()
    for news in news_list:
        st.error(news)
