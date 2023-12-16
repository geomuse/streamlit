import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.title('simple streamlit example.')

data_of_json = {
    'date' : ['12-09-2023','13-09-2023','14-09-2023','15-09-2023','16-09-2023','17-09-2023','18-09-2023','19-09-2023','20-09-2023','21-09-2023'] , 
    'return' : np.random.normal(size=10)
}

data_of_json['date'] = [ datetime.strptime(data_of_json['date'][_],'%d-%m-%Y') for _ in range(len(data_of_json['return'])) ]

df = pd.DataFrame(data_of_json)
df.index  = df['date']
df = df.drop(columns=['date'],axis=1)

st.dataframe(df)
st.line_chart(df)
st.write('end.')