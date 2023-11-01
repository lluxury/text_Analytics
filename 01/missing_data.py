import pandas as pd
pd.options.display.max_colwidth = 150

file = "un-general-debates-blueprint.csv.gz"
df = pd.read_csv(file)

print("\ncheck out:\n")
print(df.isna().sum())

print("\nfillna:\n")
print(df['speaker'].fillna('unkown', inplace=True))  # 27 speaker

print("\ncheck out:\n")
print(df[df['speaker'].str.contains('Bush')]['speaker'].value_counts())