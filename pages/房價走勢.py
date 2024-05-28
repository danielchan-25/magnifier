import streamlit as st
import pymysql
import pandas as pd


# 日期：2024年3月12日
# 作者：陈某
# 说明：获取数据库中的信宜平均房价

def get_data():
    # 获取数据库数据
    def get_db_data():
        conn = pymysql.connect(host='192.168.2.11', user='root', password='Ba100132087974!@#', database='XY_HousePrice')
        cursor = conn.cursor()
        cursor.execute(f'SELECT date,price FROM XY_HousePrice_1D;')
        conn.commit()
        result = cursor.fetchall()
        cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    data_list = [i for i in get_db_data()]
    date_list = [i[0] for i in data_list]
    price_list = [float(i[1]) for i in data_list]
    df = pd.DataFrame({'date': date_list, 'price': price_list})
    return df


if __name__ == '__main__':
    st.title('房價走勢')
    tab1, tab2, tab3, tab4 = st.tabs(['信宜', '佛山', '中山', '惠州'])

    with tab1:
        df = get_data()
        st.info('從安居客爬取的數據，是信宜房價的平均走勢。')
        st.line_chart(data=df, x='date', y='price')

    with tab2:
        st.warning('小編正在加班，請稍後回來')

    with tab3:
        st.warning('小編正在加班，請稍後回來')

    with tab4:
        st.warning('小編正在加班，請稍後回來')
