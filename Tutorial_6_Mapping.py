from elasticsearch import Elasticsearch

#Instantiate Elasticsearch
es = Elasticsearch(HOST="http://localhost", PORT=9200)
es = Elasticsearch()


#documents to insert in the elasticsearch index "cities"
doc1 = {"city":"Bangalore", "country":"India","datetime":"2018,01,01,10,20,00"} #datetime format: yyyy,MM,dd,hh,mm,ss
doc2 = {"city":"London", "country":"England","datetime":"2018,01,02,03,12,00"}
doc3 = {"city":"Los Angeles", "country":"USA","datetime":"2018,04,19,21,02,00"}

#insert doc1
es.index(index="travel", id=1, body=doc1)

#get mapping
map = es.indices.get_mapping(index="travel")
print(map)

#We will create custom mapping before doing that we need to delete current index
#We can not change mapping once we insert data, so we need to delete data first
es.indices.delete(index="travel")

#Create custom mapping
#We create custom mapping for datetime, because you can see default get_mapping
#could not infer datetime schema as datetime, other properties are same as default one

#We need to create index again
es.indices.create(index='travel')

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

map2 = es.indices.get_mapping(index="travel")
print(map2)

#When you execute the code you will see type of datetime will change from
#text to datetime with custom mapping we have created
