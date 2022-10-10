import streamlit as st
import time


st.title('Hello World')

st.write('DataFrame')


st.write('progress bar')
'Start'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)







left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button :
  right_column.write('ここは右からむ')

expander = st.expander('問い合わせ')
expander.write('問い合わせを書く')