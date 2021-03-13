from elasticsearch import Elasticsearch

#Instantiate Elasticsearch
es = Elasticsearch(HOST="http://localhost", PORT=9200)
es = Elasticsearch()

doc1 = {"sentence" : "What a wonderful world!"}
doc2 = {"sentence" : "Fenerbahce is the greatest football club in Turkey"}

es.index(index="english", id=1, body=doc1)
es.index(index="english", id=2, body=doc2)

#Match query will match exactly what we are looking for inside any other object
res = es.search(index="english", body={"from":0, "size":1, "query": {"match":{"sentence":"Fenerbahce"}}})
print(res)
print(res['hits']['hits'])
#Match phrase query looks for exactly match of the phrase
#So below query will match
res2 = es.search(index="english", body={"from":0, "size":1, "query": {"match_phrase":{"sentence":"Fenerbahce is the"}}})
print(res2)
print(res2['hits']['hits'])
#Below query will not mactch
res3 = es.search(index="english", body={"from":0, "size":1, "query": {"match_phrase":{"sentence":"Fenerbahce is th"}}})
print(res3)
print(res3['hits']['hits'])
