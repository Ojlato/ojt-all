import streamlit as st
#import time
st.header(f"سایت ثبت نام")
st.write("جهت رفرش صفحه اینجا کلیک کنید😉👇")

if "counter" not in st.session_state:
    st.session_state.counter = 0
st.session_state.counter += 1

#st.header(f"This page has run {st.session_state.counter} times.")
st.button("اینجا")

st.text_input("نام:", key="name")
st.text_input("نام خانوادگی:", key="fname")
st.number_input("معدل ترم قبل", key="Pass")
st.session_state.fname

#st.markdown("# Main page 🎈")
st.sidebar.markdown("# ارتباط با ما 🎈")

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)
#st.sidebar(st.text_input()
#st.sidebar.slider('Select a range of values',0.0, 100.0, (25.0, 75.0)

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('OK')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'جنسیت',
        ("مرد", "زن", "دوست ندارم بگویم"))
    #st.write(f"You are {chosen} !")

latest_iteration = st.empty()
bar = st.progress(0)

#for i in range(100):
  # Update the progress bar with each iteration.
#  latest_iteration.text(f'Iteration {i+1}')
#  bar.progress(i + 1)
#  time.sleep(0.01)

#'...and now we\'re done!'

# Add a slider to the sidebar:
#add_slider = st.sidebar.slider(
#    'Select a range of values',
#    0.0, 100.0, (25.0, 75.0)

x = st.slider('ضرب اعداد در خودشان:')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

import pandas as pd
df = pd.DataFrame({
  'first column': [60, 50, 30, 40],
  'second column': [10, 20, 30, 40],
  'third column': [600,1000,900,1600]
})

df

number = st.slider("Pick a number: ", min_value=1, max_value=100)
st.text("Your age is " + str(number))