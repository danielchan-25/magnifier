import streamlit as st
import pandas as pd

csv_file = './spider/xinyi_houseprice/XY_HousePrice_1D.csv'

if __name__ == '__main__':
    st.title('房價走勢')
    tab1, tab2, tab3, tab4 = st.tabs(['信宜', '佛山', '中山', '惠州'])

    with tab1:
        df = pd.read_csv(csv_file)
        st.info('從安居客爬取的數據，是信宜房價的平均走勢。')
        st.line_chart(data=df, x='date', y='price')

    with tab2:
        st.warning('小編正在加班，請稍後回來')

    with tab3:
        st.warning('小編正在加班，請稍後回來')

    with tab4:
        st.warning('小編正在加班，請稍後回來')
