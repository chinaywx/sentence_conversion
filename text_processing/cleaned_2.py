import os

import pandas as pd

with open('../results/news.eng_with_id.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 初始化一个空字典
data_dict = {}

# 遍历每一行数据
for line in lines:
    columns = line.strip().split('\t')  # 使用制表符进行分割
    if len(columns) >= 2:
        key = columns[0]
        value = columns[1]
        data_dict[key] = value

df = pd.read_csv("../sentences/emerge.txt", sep='\t', encoding='utf-8', header=None)
df_sorted = df.sort_values(by=0)

output_dir = '../the_finished_sentences'
# 按行操作DataFrame，将内容整合并写入文件
for a, row in df.iterrows():
    try:
        index = int(row.tolist()[0])
    except:
        print(f'{a} is not avaliable!')
        continue
    filename = os.path.join(output_dir, f'{index}.txt')
    try:
        content = '\n'.join(row.tolist()[1:])  # 将除了第一列的其余列整合成字符串
    except:
        print(index)
        continue
    with open(filename, 'w',encoding='utf-8') as f:
        f.write(data_dict[str(index)]+'\n')
        f.write(content)
