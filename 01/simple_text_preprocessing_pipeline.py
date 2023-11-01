import regex as re
import nltk
from tqdm import tqdm
import pandas as pd

file = "un-general-debates-blueprint.csv.gz"
df = pd.read_csv(file)

df['length'] = df['text'].str.len()

# nltk.download('stopwords')
def tokenize(text):
	return re.findall(r'[\w-]*\p{L}[\w-]*', text)


text = "Let's defeat SARS-CoV-2 together in 2020!"
# tokens = tokenize(text)
# print("|".join(tokens))	

stopwords = set(nltk.corpus.stopwords.words('english'))

def remove_stop(tokens):
	return [t for t in tokens if t.lower() not in stopwords]

include_stopwords = {'dear', 'regards', 'must', 'would', 'also'}
exclude_stopwords = {'against'}

stopwords |= include_stopwords
stopwords -= exclude_stopwords

def remove_stop(tokens):
	return [t for t in tokens if t.lower() not in stopwords]

pipeline = [str.lower, tokenize, remove_stop]	

def prepare(text, pipeline):
	tokens = text
	for transform in pipeline:
		tokens = transform(tokens)
	return tokens

# print(prepare(text,pipeline))	
# ['let', 'defeat', 'sars-cov-2', 'together']



tqdm.pandas()
df['tokens'] = df['text'].progress_apply(prepare, pipeline=pipeline)

df['num_tokens'] = df['tokens'].progress_map(len)
print("num_tokens\n")
print(df.describe().T)