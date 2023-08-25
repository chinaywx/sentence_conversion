import os


# 定义函数来检查句子是否满足条件
def check_sentence(sentence):
    return "1500" in sentence or len(sentence) < 10


def count_newlines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            newline_count = content.count('\n')
            return newline_count
    except FileNotFoundError:
        return -1  # 表示文件不存在
    except Exception as e:
        print("发生错误：", e)
        return -2  # 表示其他错误


def count_sentences(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            sentences = content.split('\n')

            # 过滤空行
            sentences = [sentence for sentence in sentences if sentence.strip() != '']

            return len(sentences)
    except FileNotFoundError:
        print("文件未找到")
        return 0


# 获取文件夹路径
folder_path = "E:\生成10个同义句"

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):  # 假设你只处理文本文件，根据实际情况调整
        file_path = os.path.join(folder_path, filename)

        sentence_count = count_sentences(file_path)
        if sentence_count < 11:
            print(f"{filename}句子个数:", sentence_count)
