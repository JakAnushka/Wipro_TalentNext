# Perfore Text Preprocessing on SMSSpamCollection Dataset.
# Step 1: Import libraries
import pandas as pd
import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')


df = pd.read_csv("spam.csv", encoding='latin-1')


df = df[['v1', 'v2']]
df.columns = ['label', 'message']

print(df.head())


def clean_text(text):
    
    text = text.lower()
    
    text = re.sub(r'\d+', '', text)
    
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    text = text.strip()
    return text

df["cleaned"] = df["message"].apply(clean_text)


stop_words = set(stopwords.words('english'))

def remove_stopwords(text):
    tokens = text.split()
    filtered = [word for word in tokens if word not in stop_words]
    return " ".join(filtered)

df["cleaned"] = df["cleaned"].apply(remove_stopwords)


lemmatizer = WordNetLemmatizer()

def lemmatize_text(text):
    tokens = text.split()
    lemmas = [lemmatizer.lemmatize(word) for word in tokens]
    return " ".join(lemmas)

df["cleaned"] = df["cleaned"].apply(lemmatize_text)

df.to_csv("spam_cleaned.csv", index=False)

print(df.head(10))
