from elasticsearch import Elasticsearch

#Instantiate Elasticsearch
es = Elasticsearch(HOST="http://localhost", PORT=9200)
es = Elasticsearch()

doc1 = {"city":"Istanbul", "country":"Turkey"}
doc2 = {"city":"New York", "country":"USA"}
doc3 = {"city":"Bergamo", "country":"Italy"}

#Insert data into es
es.index(index="cities",  id=1, body=doc1)
es.index(index="cities",  id=2, body=doc2)
es.index(index="cities",  id=3, body=doc3)

#Get data
res = es.get(index="cities", id=2)
print(res['_source'])
