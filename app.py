import os

# 定义可执行文件路径
exe_path = "D:/Acaconda/Acaconda/envs/BOC_py3.11/Scripts/streamlit.exe"

res = os.system(exe_path)
args = "run D:/BOC_Intership/CSV_Show_YunLong/view.py"

# 构建完整的命令字符串
command = f"{exe_path} {args}"

# 调用可执行文件并传递参数
os.system(command)
