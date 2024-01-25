import spacy
from spacy.lang.en.stop_words import STOP_WORDS

STOP_WORDS  # we can print this to see the stop words.


nlp = spacy.load("en_core_web_sm")
doc =nlp("We just opened our wings,the flying part is coming soon")

for token in doc:
    if token.is_stop:
       token  #print the tokens

def preprocess(text):  # doing preprocessing.
    doc = nlp(text)

    no_stop_words = [token.text for token in doc if not token.is_stop]
    return " ".join( no_stop_words)

#print(preprocess("We just opened our wings,the flying part is coming soon"))

import pandas as pd

df = pd.read_json('Jupyter code\doj_press.json',lines = True)
#print(df.shape)

#print(df.head(5))


#print(df.info) # info of data

df = df[df["topics"].str.len()!=0]
#print(df.head(5))

#print(df.shape)# after removing o in topicss.


df = df.head(100)

#print(df["contents"].iloc[4])

#step to remove all stop words in above dataset

df["contents_new"] = df["contents"].apply(preprocess)
#print(df.head(5))

#to checkk old and new contents.
'''print(len(df["contents"].iloc[4]))
print(len(df["contents_new"].iloc[4]))'''

print(df['contents'].iloc[4][:300]) #see the results para
print(df['contents_new'].iloc[4][:300])