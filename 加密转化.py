import pandas as pd

df = pd.read_csv("d23.csv", encoding="utf-8", sep="\t")

df.to_excel("d22.xlsx", index=False)