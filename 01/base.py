import pandas as pd
pd.options.display.max_colwidth = 150

file = "un-general-debates-blueprint.csv.gz"
df = pd.read_csv(file)

# print("base 2: \n",df.sample(2, random_state=53))
# print("df sample: \n",df.sample(frac=0.1))
# print("df info: \n",df.info())
print("df info memory_usage: \n",df.info(memory_usage='deep'))