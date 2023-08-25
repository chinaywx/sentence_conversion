import pandas as pd

df = pd.read_csv('../sentences/emerge.txt', sep='\t', encoding='utf-8', header=None)
# 查找含有NaN值的行
rows_with_nan = df[df.isnull().any(axis=1)]

# 获取这些行对应的第一列的值
first_column_values = rows_with_nan.index.tolist()

# 统计每行含有NaN值的数量
nan_counts = rows_with_nan.isnull().sum(axis=1)

# 创建一个字典，键是索引，值是对应的NaN值个数
index_nan_count_dict = nan_counts.to_dict()
for index in index_nan_count_dict.keys():
    first_column_value = df.loc[index].iloc[0]
    with open('output3.txt', 'a', encoding='utf-8') as file:
        file.write(f"{first_column_value}\t{index_nan_count_dict[index]}\n")
