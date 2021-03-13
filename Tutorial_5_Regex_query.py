from elasticsearch import Elasticsearch

#Instantiate Elasticsearch
es = Elasticsearch(HOST="http://localhost", PORT=9200)
es = Elasticsearch()

doc1 = {"sentence" : "What a wonderful world!"}
doc2 = {"sentence" : "Fenerbahce is the greatest football club in Turkey"}
doc3 = {"sentence" : "Mesut Ozil is the great number 10"}
doc4 = {"sentence" : "Mesut Ozil is the one of greatest assist maker"}

#Inserting 4 documents to index english
es.index(index="english", id=1, body=doc1)
es.index(index="english", id=2, body=doc2)
es.index(index="english", id=3, body=doc3)
es.index(index="english", id=4, body=doc4)

#Regex search 1
res = es.search(index="english", body={"from":0, "size":4, "query":{"regexp": {"sentence":".*"}}})

print(res)

#Regext search 2
res2 = es.search(index="english", body={"from":0, "size":4, "query":{"regexp": {"sentence":"wonder.*"}}})

print(res2)
