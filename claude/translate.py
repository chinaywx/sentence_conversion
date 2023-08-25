import csv
import os
import random
import re
import pandas as pd
from claude_api import Client
import json
from prompt import generate_user_input


def load_cookies_from_file(file_path):
    with open(file_path, 'r') as f:
        cookies = set(f.read().splitlines())
        if not cookies:
            raise ValueError("Cookie资源池文件为空.")
        return cookies


cookies = load_cookies_from_file("cookies.txt")


def get_one_cookie():
    if cookies:
        return cookies.pop()
    else:
        raise ValueError("Cookie资源池为空.")


def remove_invalid_cookie(cookie):
    if cookie in cookies:
        cookies.remove(cookie)
        print("失效cookie已从集合中删除.")
    else:
        print("该cookie不存在于集合中.")


def store(index, claude, conversation_id):
    response = claude.chat_conversation_history(conversation_id)
    response_ls = [res['text'] for res in response['chat_messages']]
    for response in response_ls:
        # Define a regular expression pattern to match JSON data
        pattern = r'\[.*?\]'

        # Find all matches of the pattern in the input text
        matches = re.findall(pattern, response, re.DOTALL)

        # Loop through the matches and process each one as JSON data
        with open("../sentences/sentences.txt", "a", encoding='utf-8') as file:
            for match in matches:
                try:
                    data = json.loads(match)
                    sentences = [item["sentence"] for item in data]
                    file.write(index)
                    for sentence in sentences:
                        file.write("\t" + sentence)  # Write sentence with a tab separator
                    file.write("\n")
                except:
                    print("Invalid JSON data:", match)


def read_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            yield (line.strip().split('\t'))


def main():
    cookie = get_one_cookie()
    claude = Client(cookie, True)
    # conversation_id = None
    counter = 0
    print("欢迎使用claude2!")
    file_path = '../results/duplicate_data.txt'
    lines_generator = read_lines(file_path)
    for index, num in lines_generator:
        user_input = generate_user_input(index, num)
        # print(user_input)
        conversation_id = None
        if not conversation_id:
            conversation = claude.create_new_chat()
            conversation_id = conversation['uuid']
        counter += 1
        try:
            response = claude.send_message(user_input, conversation_id)
        except json.decoder.JSONDecodeError:
            continue
        # store(index, claude, conversation_id)
        with open("../sentences/sentences.txt", "a", encoding='utf-8') as file:
            file.write(index)
            file.write("\t" + response.replace('\n', '\t'))  # Write sentence with a tab separator
            file.write("\n")
    print("提取完成，并已保存到sentences.txt文件中。")


def reset(claude_api):
    reset = claude_api.reset_all()
    if reset:
        print("All conversations reset successfully")
    else:
        print("Failed to reset conversations")


def read_clean_map(csv_file):
    chunk = pd.read_csv(csv_file, sep='\t', header=None)

    a = pd.read_csv('../sentences/sentences.txt', sep='\t', header=None)
    # seta = set(chunk.iloc[:, 0])
    # setb = set(a.iloc[:, 0])
    intersection = set(a.iloc[:, 0]).intersection(set(chunk.iloc[:, 0]))
    result = chunk[~chunk.iloc[:, 0].isin(intersection)]
    result.to_csv('news.eng_with_id.txt', encoding='utf-8', index=False, sep='\t', header=False, quoting=csv.QUOTE_NONE,
                  quotechar='=', )
    # os.remove('map.csv')


if __name__ == "__main__":
    main()
