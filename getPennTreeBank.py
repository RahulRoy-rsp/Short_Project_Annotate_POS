import nltk
import requests
from bs4 import BeautifulSoup
import pandas as pd

# nltk.download('tagsets')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# URL of the webpage penn tree bank
url = "https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')

data = []
for row in table.find_all('tr'):
    cols = row.find_all(['td', 'th'])
    cols = [col.text.strip() for col in cols]
    data.append(cols)

df = pd.DataFrame(data[1:], columns=data[0])

def forFamily(desc):
    desc = desc.lower()
    if 'pronoun' in desc:
        return 'Pronoun'
    elif 'noun' in desc:
        return 'Noun'
    elif 'adverb' in desc:
        return 'Adverb'
    elif 'verb' in desc:
        return 'Verb'
    elif 'adjective' in desc:
        return 'Adjective'
    else:
        return 'Misc'

print(df.head(3))

df['Family'] = df['Description'].apply(forFamily)

print(df.tail(3))

df.to_csv('pos_info.csv', columns=['Tag', 'Family', 'Description'])
