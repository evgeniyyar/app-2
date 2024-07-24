import streamlit


streamlit.set_page_config(layout="wide")

col1, col2 = streamlit.columns(2)

with col1:
    streamlit.image("images/photo.png")

with col2:
    streamlit.title("I am Sam")
    content = "123123123132"
    streamlit.info(content)





