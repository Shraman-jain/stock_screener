import streamlit as st

st.session_state
st.title('Cal')

r=st.text_input('Risk',key='r')
ep=st.text_input('Entry Price',key='w')

incr = st.button('Increment')
dec = st.button('DEC')
try:
    if incr:
        for i in range(int(st.session_state.r)):
            st.write(i)

    if dec:
        for i in range(int(st.session_state.w)):
            st.write(i)
except Exception as e:
    st.exception(e)
