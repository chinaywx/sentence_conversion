import os

# 定义存储文件路径的列表
file_paths = []

# 指定存储文本文件的文件夹路径
folder_path = '../sentences'  # 替换为实际文件夹路径

# 遍历文件夹，将文本文件路径存入列表
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_paths.append(os.path.join(folder_path, filename))

# 读取文本文件内容并存储为字典
file_data = {}
for path in file_paths:
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            index, text = line.strip().split('\t')
            if index not in file_data:
                file_data[index] = []
            file_data[index].append((path, text))

# 查找相同文本数据的文档和索引
duplicate_data = {}
for index, data_list in file_data.items():
    seen_texts = set()  # todo 根据集合将结果写入txt文档
    for path, text in data_list:
        if text in seen_texts:
            if text not in duplicate_data:
                duplicate_data[text] = []
            duplicate_data[text].append((index, path))
        seen_texts.add(text)
    # 打开或创建一个txt文件供写入
    file_path = '../results/output.txt'
    with open(file_path, 'a', encoding='utf-8') as file:
        # 将集合内容按照所需格式写入txt文件
        # 使用制表符分隔元素并写入文件
        file.write(index + '\t')
        count = 0
        for item in seen_texts:
            file.write(item + '\t')
            count += 1
            if count >= 10:
                break
        file.write('\n')
result = {}
# 输出相同文本数据的文档和索引
for text, duplicate_list in duplicate_data.items():
    # print(f"相同文本数据：{text}")
    for index, path in duplicate_list:
        if index not in result:
            result[index] = []
        result[index].append(path)
        # print(f"  文档：{path}\n  索引：{index}\n")
# 将字典内容整理为以tab为分隔符的文本
formatted_text = ""
for key, values in result.items():
    tag = 10 - (11 - len(values))
    if tag > 0:
        formatted_text += key + '\t' + str(tag) + '\n'

# 指定要写入的txt文件名
output_file = '../results/duplicate_data.txt'

# 将整理好的文本写入txt文件
with open(output_file, 'w') as file:
    file.write(formatted_text)
if not duplicate_data:
    print("没有找到相同文本数据的文档")
