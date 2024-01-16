import os
import json
import pandas as pd
import openpyxl


def read_output():
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
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    fo_data=[["食物名","食物类别","热量（大卡）","碳水化合物(克)","蛋白质(克)","脂肪(克)"]]
    #print("|\t食物名\t|\t食物类别\t|\t热量（大卡）\t|\t碳水化合物(克)\t|\t蛋白质(克)\t|\t脂肪(克)\t|\n")
    for i in range(len(data)):
        #print(data[i])
        name=data[i]['basic_info']['food_name']
        group_name=data[i]['basic_info']['food_group_name']

        nutrition_info=data[i]['nutrition_info']
        heat=nutrition_info[0]['热量(大卡)']
        carbh=nutrition_info[1]['碳水化合物(克)']
        protn=nutrition_info[3]['蛋白质(克)']
        fat=nutrition_info[2]['脂肪(克)']
        fo_data.append([name,group_name,heat,carbh,protn,fat,])
        #print(f'|\t{name}\t|\t{group_name}\t|\t{heat}\t|\t{carbh}\t|\t{protn}\t|\t{fat}\t|\n') 

    for row_index, row_data in enumerate(fo_data):
        for col_index, cell_value in enumerate(row_data):
            # 计算单元格的索引，例如A1、B1、A2、B2等
            cell = sheet.cell(row=row_index + 1, column=col_index + 1)
            cell.value = cell_value

    workbook.save('output2.xlsx')
    return fo_data