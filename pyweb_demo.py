import streamlit as st

st.session_state
st.title('Cal')

r=st.text_input('Risk',key='r')
ep=st.text_input('Entry Price',key='w')

incr = st.button('Increment')
dec = st.button('DEC')
if incr:
    st.write(st.session_state.r+st.session_state.w)

if dec:
    st.write(st.session_state.w+st.session_state.r)
