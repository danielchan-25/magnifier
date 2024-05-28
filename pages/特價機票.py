import time
import requests
import re
import json
import pandas as pd
import streamlit as st
from function.refresh import prevent_malicious_refresh

now_time = time.time()  # 生成时间戳
url = f'https://ws.qunar.com/lowerPrice.jcp?callback=jQuery17209515388475276634_1699863125197&_={now_time}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}


def get_response(url, headers):
    try:
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)


def parse_data(response):
    try:
        query_data = re.findall(r'\((.*?)\)', response.text)
        json_data = json.loads(query_data[0])
        data = json_data['data']
        return data
    except Exception as e:
        print(f'解析数据失败，失败原因： {e}')


def get_data(location):
    response = get_response(url=url, headers=headers)
    if response:
        data = parse_data(response)
        df = pd.DataFrame(data[location]['records'])
        return df


if __name__ == '__main__':
    st.title('特價機票')
    st.info('數據源：去哪兒網(https://flight.qunar.com/)')
    prevent_malicious_refresh()

    menu = st.sidebar.selectbox('請選擇', ['國內', '國際'])

    if menu == '國內':
        tab1, tab2 = st.tabs(['廣州', '深圳'])

        with tab1:
            df = get_data(location='广州')
            st.dataframe(df, 1500, 600)

        with tab2:
            df = get_data(location='深圳')
            st.dataframe(df, 1500, 600)

    elif menu == '國際':
        st.warning('小编正在加班，请稍后回来')
