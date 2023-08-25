import os
import pandas as pd


def read_txt_files_in_folder(folder_path):
    merged_dict = {}
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            # 创建一个新的字典用于存储合并后的结果
            # 读取文本文件并将其添加到DataFrame中
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if lines:
                    multi_values_dict1 = {parts[0]: {value.strip('\n') for value in parts[1:] if
                                                     not any('\u4e00' <= char <= '\u9fff' for char in value)} for line
                                          in lines for parts in [line.split('\t')]}
                    # 遍历字典并合并值
                    for key, values in multi_values_dict1.items():
                        merged_dict.setdefault(key, set()).update(values)

    return merged_dict


def write_combined_data(multi_values_dict1, output_file):
    with open(output_file, 'w', encoding='utf-8') as file1, open('../results/duplicate_data.txt', 'w',
                                                                 encoding='utf-8') as file2:
        # 遍历字典的键值对
        for key, values in multi_values_dict1.items():
            # 将集合内的值用制表符分隔，然后写入文件
            values_str = '\t'.join(list(values)[:10])
            file1.write(f"{key}\t{values_str}\n")
            if len(values) < 10:
                file2.write(f"{key}\t{10 - len(values)}\n")


if __name__ == '__main__':
    # 指定文件夹路径
    folder_path = '../sentences'
    output_file = '../sentences/emerge.txt'

    # 调用函数读取所有txt文件
    all_txt_data = read_txt_files_in_folder(folder_path)
    write_combined_data(all_txt_data, output_file)
