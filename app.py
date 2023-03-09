import streamlit as st

st.title("GIẢI PHƯƠNG TRÌNH BẬC NHẤT")
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')
if st.button('Giải'):
  if a==0:
    if b==0:
      st.success('Vô số nghiệm')
    else:
      st.success('Vô nghiệm')
  else:
    st.success(f'Phương trình có 1 nghiệm {-b/a}')