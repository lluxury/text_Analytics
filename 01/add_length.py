import pandas as pd
pd.options.display.max_colwidth = 150

file = "un-general-debates-blueprint.csv.gz"
df = pd.read_csv(file)

print("\nfind columns:\n",df.columns)

print("\nadd length:")
df['length'] = df['text'].str.len()

print("\ncheck out:\n",df.describe().T)

print("\nstring summary:")
print(df[['country', 'speaker']].describe(include='O').T)