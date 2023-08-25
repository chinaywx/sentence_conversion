import csv

import pandas as pd

"""
给csv添加id列
"""
# 读取CSV文件
df = pd.read_csv('../results/news.eng.txt', header=None, sep='\t')

# 添加ID列
df.insert(0, 'id', range(1, len(df) + 1))

# 写入新的CSV文件
df.to_csv('news.eng_with_id.txt', encoding='utf-8', sep='\t', index=False, quoting=csv.QUOTE_NONE, quotechar='=', header=False)
