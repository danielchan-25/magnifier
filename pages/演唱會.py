import streamlit as st
import requests
import json
import pandas as pd
from function.refresh import prevent_malicious_refresh

location = '%E5%B9%BF%E5%B7%9E'  # 广州
url = f'https://search.damai.cn/searchajax.html?keyword=&cty={location}&ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&sctl=&tsg=0&st=&et=&order=1&pageSize=30&currPage=1&tn='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Content-Encoding': 'gzip',
    'Content-Type': 'application/json;charset=UTF-8',
    'Referer': 'https://search.damai.cn/search.htm?spm=a2oeg.home.card_0.dviewall.591b23e12PBsuw&ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&order=1&cty=%E5%B9%BF%E5%B7%9E',
    'Accept': 'application/json, text/plain, */*',
    'Cookie': 'cna=mqSJHa+iRWQCATo+zM1J/a2O; xlly_s=1; destCity=%u5E7F%u5DDE; XSRF-TOKEN=98ddebb3-c9f0-4536-942e-9dee2470e161; isg=BO3tukDddBLYNBAMDbPVi15G_IlnSiEcFqZq3i_yEwTzpgxY9plO7Qw3kHpAJjnU; l=fBSyPTggPrOfeDVOBOfZnurza77T9IRfguPzaNbMi9fP_QfH5QQAW1eFdTYMCnGVEsL9J3RxBjFXBjLghy4e7xv9-et_Cgv8ZdLnwpzHU; tfstk=dtYDjBV5FnSbrnBDAxQjuSdZoemRc-_1BdUOBNBZ4TW7knnfXOVGEplfDmtvqOvlFrKxcGBgsTv4WiLM1Pfw_dGfBjiJGI_17vHKp2dXGqOteh4rvK1uZPMKp23K077invKY1YoAUsUZgZEeRjjdK5ZQH543rGWegtRvGU78p9AVmPzNnsXNnure0aU1afLzflsVN_Xd7ozZS'
}


def get_response(url, headers):
    try:
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()  # 这会抛出HTTPError，如果状态码不是200
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
        response_data = json.loads(response.text)
        return response_data
    except json.JSONDecodeError as e:
        print(f'解析JSON失败，失败原因', e)
    except Exception as e:
        print(f'解析数据失败，失败原因：', e)


def get_data():
    response = get_response(url=url, headers=headers)
    if response:
        data = parse_data(response)['pageData']['resultData']
        df = pd.DataFrame(data)
        df = df[['name', 'actors', 'showtime', 'price_str', 'venue', 'showstatus']]
        return df


if __name__ == '__main__':
    st.title('演唱會')
    tab1, tab2 = st.tabs(['廣州', '深圳'])
    prevent_malicious_refresh()

    with tab1:
        df = get_data()
        st.dataframe(df, 1500, 600)

    with tab2:
        st.warning('小編正在加班，請稍後回來')
