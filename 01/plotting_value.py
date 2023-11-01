import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_colwidth = 150

file = "un-general-debates-blueprint.csv.gz"
df = pd.read_csv(file)

df['length'] = df['text'].str.len()

df['length'].plot(kind='box', vert=False, figsize=(8, 1))
plt.show()

df['length'].plot(kind='hist', bins=30, figsize=(8,2))
plt.show()

import seaborn as sns
plt.figure(figsize=(8, 2))  # ？
sns.distplot(df['length'], bins=30, kde=True)
plt.show()
