# import streamlit as st
# import pandas as pd
# import numpy as np
# from ReadCsv import OptCsv
# from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder
#
#
# oc = OptCsv()
# path = 'test.xlsx'
# datas = oc.read_excel(path=path, sheet='sheet1')
#
# keys = []
# for k in datas[0].keys():
#     keys.append(k)
#
# values = []
# for data in datas:
#     value = data.values()
#     templist = []
#     for v in value:
#         templist.append(v)
#     values.append(tuple(templist))
#
# df = pd.DataFrame(values, columns=keys)
#
# with st.form('example form') as f:
#     ag = AgGrid(df, fit_columns_on_grid_load=True, editable=True)
#
#     st.form_submit_button(label="修改表格数据", help="此按钮是修改表格数据，并不能增加删除", on_click=oc.InsertdataCsv, args=[ag, path, 'sheet1'])

import pandas as pd
import streamlit as st

# 从 Excel 文件中读取数据
df = pd.read_excel('test.xlsx')

headers = df.keys().values

# 遍历每一行，展示数据和操作按钮
for index, row in df.iterrows():
    if index == 0:
        # 创建两个列，每个列占据一半的宽度
        cols = st.columns(len(headers) + 2)
        for i in range(len(headers)):
            cols[i].write(headers[i])
        cols[-2].write('操作')
        cols[-1].write('')

    # 创建两个列，每个列占据一半的宽度
    cols = st.columns(7)

    # 在左侧列中展示一部分数据
    # left_col.write(index)
    for i in range(0, len(cols) - 2):
        cols[i].write(row[i])

    # 在左侧列中添加按钮1
    button1 = cols[-2].button("按钮1", key=f"{index}1")

    # 在右侧列中添加按钮2
    button2 = cols[-1].button("按钮2", key=f"{index}2")

    # 在按钮被点击时执行对应的操作
    if button1:
        # 执行按钮1的代码
        st.write("按钮1被点击")

    if button2:
        # 执行按钮2的代码
        st.write("按钮2被点击")

    st.write("---")  # 添加分隔线
