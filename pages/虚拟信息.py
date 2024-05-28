import streamlit as st
from faker import Faker
import pandas as pd

fake = Faker(locale='zh_CN')

st.title('虛擬信息')
tab1, tab2, tab3, tab4 = st.tabs(['個人信息', '地址信息', '公司信息', '銀行信息'])


def generate_fake_data(column_name, function, num_rows=10):
    return [function() for _ in range(num_rows)]


with tab1:
    df = pd.DataFrame({
        "姓名": generate_fake_data("姓名", fake.name),
        "男生姓名": generate_fake_data("男生姓名", fake.name_male),
        "女生姓名": generate_fake_data("女生姓名", fake.name_female),
        "電子信箱": generate_fake_data("電子信箱", fake.email),
        "手機號碼": generate_fake_data("手機號碼", fake.phone_number),
        "手機區號": generate_fake_data("手機區號", fake.phonenumber_prefix),
        "身份證": generate_fake_data("身份證", fake.ssn),
    })
    st.table(df)

with tab2:
    df = pd.DataFrame({
        "国家名称": generate_fake_data("国家名称", fake.country),
        "国家编号": generate_fake_data("国家编号", fake.country_code),
        "省": generate_fake_data("省", fake.province),
        "城市名字(不带市县)": generate_fake_data("城市名字(不带市县)", fake.city_name),
        "城市后缀名": generate_fake_data("城市后缀名", fake.city_suffix),
        "地区": generate_fake_data("地区", fake.district),
        "邮编": generate_fake_data("邮编", fake.postcode),
        "地址": generate_fake_data("地址", fake.address),
        "楼名": generate_fake_data("楼名", fake.building_number),
        "完整城市名": generate_fake_data("完整城市名", fake.city),
        "街道地址": generate_fake_data("街道地址", fake.street_address),
        "街道名称": generate_fake_data("街道名称", fake.street_name),
        "街道后缀名": generate_fake_data("街道后缀名", fake.street_suffix),
    })

    st.table(df)

with tab3:
    df = pd.DataFrame({
        "公司名称": generate_fake_data("公司名称", fake.company),
        "公司名称前缀": generate_fake_data("公司名称前缀", fake.company_prefix),
        "公司名称后缀": generate_fake_data("公司名称后缀", fake.company_suffix),
        "商业用词": generate_fake_data("商业用词", fake.bs),
        "口号": generate_fake_data("口号", fake.catch_phrase),
    })
    st.table(df)

with tab4:
    df = pd.DataFrame({
        "完整信用卡信息": [fake.credit_card_full(card_type=None) for _ in range(7)],
        "信用卡卡号": [fake.credit_card_number(card_type=None) for _ in range(7)],
        "信用卡提供商": [fake.credit_card_provider(card_type=None) for _ in range(7)],
        "信用卡安全码": [fake.credit_card_security_code(card_type=None) for _ in range(7)],
        "过期年月": [fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y") for _ in range(7)]
    })

    st.table(df)
