import os
import json
import pandas as pd

# 获取当前脚本的绝对路径
current_path = os.path.abspath(__file__)
# 获取当前脚本的父目录
dir_path = os.path.dirname(current_path)
# 获取json文件的路径
json_path = os.path.join(dir_path, 'food_data.json')

with open(json_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df.to_excel(f'{dir_path}\output.xlsx', sheet_name='Sheet1', index=False)


print("|\t食物名\t|\t热量（大卡）\t|\t碳水化合物(克)\t|\t蛋白质(克)\t|\t脂肪(克)\t|\n")
for i in range(len(data)):
    #print(data[i])
    name=data[i]['basic_info']['food_name']
    nutrition_info=data[i]['nutrition_info']
    heat=nutrition_info[0]['热量(大卡)']
    carbh=nutrition_info[1]['碳水化合物(克)']
    protn=nutrition_info[3]['蛋白质(克)']
    fat=nutrition_info[2]['脂肪(克)']
    print(f'|\t{name}\t|\t{heat}\t|\t{carbh}\t|\t{protn}\t|\t{fat}\t|\n') 