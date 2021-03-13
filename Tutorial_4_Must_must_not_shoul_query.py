from elasticsearch import Elasticsearch

#Instantiate Elasticsearch
es = Elasticsearch(HOST="http://localhost", PORT=9200)
es = Elasticsearch()

doc3 = {"sentence" : "Mesut Ozil is the great number 10"}
doc4 = {"sentence" : "Mesut Ozil is the one of greatest assist maker"}

es.index(index="english", id=3, body=doc3)
es.index(index="english", id=4, body=doc4)

res = es.search(index="english",
                body={"from": 0, "size": 1, "query": \
                        {"bool": \
                            {"must_not": \
                                {"match":{"sentence":"assist"}}, \
                                    "should":{"match": \
                                            {"sentence":"Mesut"} \
                                                                }}}})

print(res)
