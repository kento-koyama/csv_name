import streamlit as st
import datetime
import pandas as pd

# 'start_time'がst.session_stateにまだ存在しない場合、現在の時刻を保存
if 'start_time' not in st.session_state:
    st.session_state['start_time'] = datetime.datetime.now()

# session_stateから開始時刻を取得
start_time = st.session_state['start_time']
start_time_move = datetime.datetime.now()#←動的な時間名

# 日時を文字列にフォーマットする（例: '2024-03-23_15-30-00'）
formatted_start_time = start_time.strftime('%Y-%m-%d_%H-%M-%S')
formatted_start_time_move = start_time_move.strftime('%Y-%m-%d_%H-%M-%S')#←動的な時間名

# CSVファイル名を設定（例: 'data_2024-03-23_15-30-00.csv'）
filename = f'data_{formatted_start_time}.csv'
filename_move = f'data_{formatted_start_time_move}.csv'#←動的な時間名

# 以下のコードは省略します...
# データフレームの作成、CSVファイルへの保存、ボタンの表示など

# ボタンが押されたら 'button_clicked' を True に設定
if st.button('ボタン'):
    st.session_state.button_clicked = True

# 'button_clicked' が True の場合、何らかの処理を実行
if st.session_state.get('button_clicked', False):
    st.write('ボタンが押されました！')
    st.write(filename)
    st.write(filename_move) #←動的な時間名