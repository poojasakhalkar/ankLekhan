import streamlit as st
import time
from NumToWordConvertor import NumberToWord

if __name__ == '__main__':
    st.header("AnkLekhan")
    obj_NumberToWord = NumberToWord()
    number = st.text_input("Enter number")
    if number:
        with st.spinner("Number is processing", show_time=True):
            time.sleep(1)
            value = obj_NumberToWord.getValue(number)
            st.write(value)

    st.button("Rerun")