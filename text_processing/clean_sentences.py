import csv
import re

import pandas as pd


def clean_data(cell_value):
    if isinstance(cell_value, str):
        cell_value = cell_value.strip()
        # 去除"Synonyms"
        cell_value = re.sub(r'^Synonyms', '', cell_value)
        cell_value = re.sub(r'^synonyms', '', cell_value)
        cell_value = re.sub(r'^Synonym:', '', cell_value)
        cell_value = re.sub(r'^synonym: ', '', cell_value)
        cell_value = re.sub(r'Here are [0-9]+ synonyms for the input sentence:', '', cell_value)
        cell_value = re.sub(r'Here are [0-9]+ synonyms for the sentence:', '', cell_value)
        cell_value = re.sub(r'Here is [0-9]+ synonym for the sentence', '', cell_value)

        # 去除句首的序号范围为1.到10.
        cell_value = re.sub(r'^\d{1,2}\.', '', cell_value)

        # 去除句首的冒号
        cell_value = re.sub(r'^\s*:', '', cell_value)

        return cell_value.strip()  # 移除空格
    else:
        return cell_value


# 读取以制表符分隔的文本文件
file_path = '../duplicate_data.txt'  # 替换为实际的文件路径

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        data_list = []
        line = line.strip()  # 去除行尾换行符和空格
        data = line.split('\t')  # 根据逗号分隔数据
        for d in data:
            cleaned_data = clean_data(d)
            if cleaned_data:
                data_list.append(cleaned_data)

        output_file = "output1.txt"
        with open(output_file, 'a', encoding='utf-8') as f:
            a='\t'.join(data_list)
            f.write(a + '\n')
