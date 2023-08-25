import ast
import json
import re
import traceback
from unittest import TestCase
import json


class Test(TestCase):

    def test_read_clean_map(self):
        def replace_possible_escapes(input_string):
            replacements = {
                r"\n": r"\\\\n",
                r"\t": r"\\\\t",
                r"\\": r"\\\\",
                r"\'": r"\\\\'",
                r"\"": r"\\\\\"",
            }
            for key, value in replacements.items():
                input_string = re.sub(re.escape(key), value, input_string)

            return input_string

        # read_clean_map('../results/news.eng_with_id.txt')
        decoded_data = """data: {"completion":" Here","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" is","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" the","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" output","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" in","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" json","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" format","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" for","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" the","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" input","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" sentence","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":":","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":"\n\n[","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":"{\"","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":"sentence","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":"\":\"","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":"However","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" a","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" small","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" closed","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" room","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" is","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" very","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" different","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" from","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" an","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" actual","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" interior","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" setting","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" in","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" a","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" large","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":" ed","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":"if","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":"ice","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":".\"","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":"}]","stop_reason":null,"model":"claude-2.0","stop":null,"log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

data: {"completion":"","stop_reason":"stop_sequence","model":"claude-2.0","stop":"\n\nHuman:","log_id":"c4c54dfaa48550adb52d0004534793e501d32783b9fe0e432855d7649b230779","messageLimit":{"type":"within_limit"}}

"""

        # 原始字符串片段
        data_strings = decoded_data.split('data:')[1:]

        # 提取每个片段中的"data"字段
        data_objects = []
        for data_string in data_strings:
            try:
                data_start = data_string.index("{")
                data_end = data_string.rindex("}") + 1
                data_json = eval(replace_possible_escapes(repr(data_string[data_start:data_end])))
                data_objects.append(json.loads(data_json)["completion"])
            except:
                traceback.print_exc()
                pass
        print(''.join(data_objects))

    def test_a(self):
        def replace_possible_escapes(input_string):
            replacements = {
                b'\\': b'\\\\',  # \
                b'\x0A': b'\\n',  # \n
                b'\x09': b'\\t',  # \t
                b"/'":b"//'",
                # b'\'': b'\"' , # \'

            }
            for key, value in replacements.items():
                input_string = input_string.replace(key, value)
            return input_string

        import json

        # 一个包含 JSON 数据的字符串
        json_data = '{"name": "a\nb\tc\\d\'fg", "age": 30, "city": "New York"}'.encode('raw_unicode_escape')
        a = replace_possible_escapes(json_data)
        b = replace_possible_escapes(json_data).decode('utf-8')
        # 使用 json.loads() 解析 JSON 字符串
        parsed_data = json.loads(a)

        # 打印解析后的 Python 对象
        # print(parsed_data)
        # normal_string = "This is a line\'And this is another line"
        # raw_string = normal_string.encode('raw_unicode_escape').replace(b'\x27', b'666').decode('utf-8')
        # print(raw_string)
