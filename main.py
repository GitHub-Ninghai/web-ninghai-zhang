import streamlit as st

# 读取 index.html 文件
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# 渲染 HTML
st.title("HTML 页面展示")
st.components.v1.html(html_content, weight=1000,height=600, scrolling=True)