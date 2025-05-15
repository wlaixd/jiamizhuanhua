import pandas as pd
#
# 读取CSV文件
df1 = pd.read_csv('报告数据excel (21).csv')
df2 = pd.read_csv('报告数据excel (22).csv')

# 合并数据
# 假设两个CSV文件有相同的列名
df = pd.concat([df1, df2], ignore_index=True)
#
# 保存合并后的CSV文件
# merged_df.to_csv('报告数据excel (20).csv', index=False)
# import pandas as pd

#读取CSV文件
# df = pd.read_csv('产品信息.csv')  # 假设你的CSV文件名为"产品信息.csv"

# # 筛选出产品名称为"喜炎平注射液"的行
filtered_df = df[df['产品信息=>产品名称'] == '喜炎平注射液']
#
# # 将筛选后的数据导出到新的Excel文件
filtered_df.to_csv('报告数据excel (23).csv', index=False)
# # import pandas as pd
#

# 读取CSV文件
df = pd.read_csv('报告数据excel (23).csv')

# 删除最后107行数据
df = df.iloc[:-4554]
df = df.iloc[:-202]

# 将结果保存回CSV文件
df.to_csv('报告数据excel (24).csv', index=False)

# df = df.iloc[:20000]