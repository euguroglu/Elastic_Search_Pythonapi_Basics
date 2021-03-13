from elasticsearch import Elasticsearch

#Instantiate Elasticsearch
es = Elasticsearch(HOST="http://localhost", PORT=9200)
es = Elasticsearch()

#Create index
es.indices.create(index="first_index", ignore=400)

#Check if index exist
es.indices.exists(index="first_index")

#Delete index
es.indices.delete(index="first_index")
