from elasticsearch import Elasticsearch
import json
#Instantiate Elasticsearch
es = Elasticsearch(HOST="http://localhost", PORT=9200, http_auth=('elastic', '*******'))

res = es.search(index="orders", body={"query": {"match_all": {}}})


with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(res['hits']['hits'], f, ensure_ascii=False, indent=4)
