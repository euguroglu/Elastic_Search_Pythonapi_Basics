from elasticsearch import Elasticsearch, helpers
import pandas as pd


#Instantiate Elasticsearch
es = Elasticsearch(HOST="http://localhost", PORT=9200)
es = Elasticsearch()

df = pd.read_csv("BostonHousing.csv")
print(df.shape)
print(df.isnull().sum())
print(df.columns)


c = 0

def func(x):
    global c
    c = c + 1
    return c

df["ID"] = df["crim"].apply(func)

df2 = df.to_dict("records")

def generator(df):
    for c, line in enumerate(df):
        yield {
    '_index': 'bostonhousing',
    '_id': line.get('ID'),
    '_source': {

        'crim':line.get('crim',["No Data"])

    }

        }


try:
    res = helpers.bulk(es, generator(df2))
    print('Working')
except Exception as e:
    print("Exception")

print(df.columns)
