import streamlit
import pandas


streamlit.set_page_config(layout="wide")

col1, col2 = streamlit.columns(2)

with col1:
    streamlit.image("images/photo.png")

with col2:
    streamlit.title("I am Sam")
    content_1 = "123123123132"
    streamlit.info(content_1)


content_2 = "Какой-то текст"
streamlit.info(content_2)

col3, empty_col, col4 = streamlit.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row_3 in df[:10].iterrows():
        streamlit.subheader(f"{index+1} - {row_3['title']}")
        streamlit.write(row_3["description"])
        streamlit.image("images/" + row_3["image"])
        streamlit.write(f"Ссылка на гит:{row_3['url']}")

with col4:
    for index, row_4 in df[10:].iterrows():
        streamlit.subheader(f"{index+1} - {row_4['title']}")
        streamlit.write(row_4['description'])
        streamlit.image("images/" + row_4["image"])
        streamlit.write(f"Ссылка на гит:{row_4['url']}")





# 0:{'title':'aaa', 'descr':'ddddd', 'url':"fffff", 'image':"fqqqqqqqqqq"}
# 1:{'title':'aaa', 'descr':'ddddd', 'url':"fffff", 'image':"fqqqqqqqqqq"}
# 2:{'title':'aaa', 'descr':'ddddd', 'url':"fffff", 'image':"fqqqqqqqqqq"}
