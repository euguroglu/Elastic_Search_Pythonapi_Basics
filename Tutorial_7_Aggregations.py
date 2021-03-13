from elasticsearch import Elasticsearch

#Instantiate Elasticsearch
es = Elasticsearch(HOST="http://localhost", PORT=9200)
es = Elasticsearch()

#documents to insert in the elasticsearch index "cities"
doc1 = {"city":"Bangalore", "country":"India","datetime":"2018,01,01,10,20,00"} #datetime format: yyyy,MM,dd,hh,mm,ss
doc2 = {"city":"London", "country":"England","datetime":"2018,01,02,03,12,00"}
doc3 = {"city":"Los Angeles", "country":"USA","datetime":"2018,04,19,05,02,00"}

#es.indices.create(index='travel')

es.indices.put_mapping(
    index="travel",
    body=
        {
            'properties': {
                'city': {
                    'type': 'text',
                    'fields': {
                        'keyword': {
                            'type': 'keyword',
                            'ignore_above': 256
                                    }
                              }
                         },
            'country': {
                'type': 'text',
                'fields': {
                    'keyword': {
                        'type': 'keyword',
                        'ignore_above': 256
                            }
                        }
                    },
            'datetime': {
                'type': 'date',
                'format': "yyyy,MM,dd,hh,mm,ss"
                    }
                }
            }
)

es.index(index="travel", id=1, body=doc1)
es.index(index="travel", id=2, body=doc2)
es.index(index="travel", id=3, body=doc3)

#Match_all query to see if docs are inserted
res = es.search(index="travel", body={"from":0, "size":5, "query": {"match_all": {}}})
print(res)

#Query with date_histogram aggregation
res2 = es.search(index="travel", body={"from":0, "size":0, "query": {"match_all": {}},
                "aggs": {
                    "country":{
                            "date_histogram": {"field":"datetime", "calendar_interval":"year"}
                              }
                        }
                })
print(res2)

#Add another document
doc4 = {"city":"Paris", "country":"France","datetime":"2019,04,19,05,02,00"}

es.index(index="travel", id=4, body=doc4)

#Query with date_histogram aggregation again
res3 = es.search(index="travel", body={"from":0, "size":0, "query": {"match_all": {}},
                "aggs": {
                    "country":{
                            "date_histogram": {"field":"datetime", "calendar_interval":"year"}
                              }
                        }
                })
print(res3)
