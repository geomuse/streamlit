# 导入Streamlit库
import streamlit as st
import pandas as pd
import numpy as np

# 创建一个标题
st.title('simple streamlit example.')

# 生成一些示例数据
data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})
 
# 在应用程序中显示数据框
st.write('show data:')
st.dataframe(data)

# 绘制折线图
st.write('show line:')
st.line_chart(data)
st.area_chart(data)

# 添加一个交互式小部件（滑块）
x_range = st.slider('choose the x-axis:', min_value=float(data['x'].min()), max_value=float(data['x'].max()))

# 根据滑块值过滤数据
filtered_data = data[data['x'] < x_range]

# 在应用程序中显示过滤后的数据框
st.write('...:')
st.dataframe(filtered_data)