import json
import pandas as pd

# 示例 JSON 数据
json_data = '''
[
  {"sentence": "A 1,500-year-old stone stele bearing the earliest discovered chiselled text of the Ten Commandments was auctioned off in the United States on Wednesday for $850,000."},
  {"sentence": "A 1,500-year-old stone slab etched with the oldest known carved writing of the Ten Commandments went for $850,000 at a U.S. auction held on Wednesday."},
  {"sentence": "A 1,500-year-old stone plaque inscribed with the earliest known engraving of the Ten Commandments was sold at an American auction on Wednesday for $850,000."},
  {"sentence": "A 1,500-year-old stone tablet carved with the earliest extant chiseled version of the Ten Commandments fetched $850,000 at a U.S. auction held on Wednesday."},
  {"sentence": "A 1,500-year-old stone monument engraved with the oldest discovered inscription of the Ten Commandments was hammered down for $850,000 at an American auction on Wednesday."},
  {"sentence": "A 1,500-year-old stone inscription chiseled with the earliest known rendering of the Ten Commandments went for $850,000 at a Wednesday auction in the United States."},
  {"sentence": "A 1,500-year-old stone relic chiselled with the oldest discovered engraving of the Ten Commandments sold at a U.S. auction for $850,000 on Wednesday."},
  {"sentence": "A 1,500-year-old stone tablet sculpted with the earliest known carved text of the Ten Commandments fetched $850,000 at an American auction held on Wednesday."},
  {"sentence": "A 1,500-year-old stone inscription etched with the earliest extant engraved version of the Ten Commandments was auctioned off in the U.S. on Wednesday for $850,000."},
  {"sentence": "A 1,500-year-old stone plaque carved with the oldest discovered chiseled text of the Ten Commandments went for $850,000 at a United States auction on Wednesday."}
]
'''


def generate_user_input(index, num):
    def display_n_key_value_pairs(json_str, num):
        data = json.loads(json_str)
        result = data[:num]
        return result

    file_path="../results/news.eng_with_id.txt"
    df = pd.read_csv(file_path, header=None, encoding='utf-8', sep='\t')
    row_index = df.index[df.iloc[:, 0] == int(index)][0]
    line = df.iloc[row_index, 1]

    result = display_n_key_value_pairs(json_data, int(num))

    user_input = f"""
Now you want to give {num} synonyms of the following sentences.No additional explanation is required, just give the result directly. 
input:"{line}"
    """
    return user_input
