import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_colwidth = 150

file = "un-general-debates-blueprint.csv.gz"
df = pd.read_csv(file)

df['length'] = df['text'].str.len()

import seaborn as sns
where = df['country'].isin(['USA', 'FRA', 'GBR', 'CHN', 'RUS'])
g = sns.catplot(data=df[where], x="country", y="length", kind='box')
g.fig.set_size_inches(4, 3) ###
g.fig.set_dpi(100)
plt.show()

g = sns.catplot(data=df[where], x="country", y="length", kind='violin')
g.fig.set_size_inches(4, 3) ###
g.fig.set_dpi(100)
plt.show()

df.groupby('year').size().plot(title="Number of Countries", figsize=(6,2))
plt.show()

df.groupby('year').agg({'length': 'mean'}) \
  .plot(title="Avg. Speech Length", ylim=(0,30000), figsize=(6,2))
plt.show()  