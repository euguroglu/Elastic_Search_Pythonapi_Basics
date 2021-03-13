from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import time

#Instantiate Elasticsearch
es = Elasticsearch(HOST="http://localhost", PORT=9200)
es = Elasticsearch()

actions = [
  {
    "_index": "chapter8",
    "_id": j,
    "_source": {
        "any":"data" + str(j),
        "timestamp": datetime.now()}
  }
  for j in range(0, 10000)
]
#Start time
st = time.time()
#Insert action list data as bulk
helpers.bulk(es, actions)
#End time
end = time.time()
print("total time:{} sec".format(end-st))

#Scanning over large data quickly using helpers.scan
results = helpers.scan(es, index="chapter8", query={"query": {"match_all":{}}})
for item in results:
    print(item['_id'], item['_source'])
