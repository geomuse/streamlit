import streamlit as st

# 页面标题
st.title('简单的Streamlit示例')

# 文本输入框
user_input = st.text_input("请输入您的名字", "John Doe")

# 按钮
button_clicked = st.button("打招呼")

# 根据按钮点击状态执行操作
if button_clicked:
    st.write(f"你好，{user_input}!")

# 添加静态文本
st.text("这是一个简单的Streamlit应用。")
