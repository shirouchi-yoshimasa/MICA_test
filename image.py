import pandas as pd
import openpyxl
from glob import glob
import datetime
import time
import sys
args = sys.argv
import streamlit as st
from PIL import Image

maclist = ['1-1','1-2','2-1','2-2']

with st.form("my_form", clear_on_submit=False):
    today_date = st.text_input('日付を6桁で入力してください 例：2022年12月1日→221201')
    name = st.selectbox(label='MAC機種指定してください', options=[f'RFD{i}' for i in maclist])
    name2 = st.selectbox(label='グラフ種類指定してください', options=['_MAX','MD_SCORE'])
    sb_p = st.text_input(label='MDscore閾値を入力してください(初期設定20)')
    submitted = st.form_submit_button("グラフ表示")

if submitted:
    with st.spinner("処理中です..."):
        time.sleep(1)
    image = Image.open(f'{today_date}_{name}{name2}.png')
    st.image(image, caption=today_date+'_'+name+name2,use_column_width=True)
