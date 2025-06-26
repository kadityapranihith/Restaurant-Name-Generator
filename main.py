import streamlit as st
from llm import generate_name_and_items
st.title("Restaurant Name Generator")
cuisine=st.sidebar.selectbox("Pick a cuisine",(
    'Indian','Mexican','Itialian','American','Arabic'
))


if cuisine:
    res=generate_name_and_items(cuisine)
    st.header(res['restaurant'])
    menu_items=res['menu_items'].split(',')

    for item in menu_items:
        st.write(item)
