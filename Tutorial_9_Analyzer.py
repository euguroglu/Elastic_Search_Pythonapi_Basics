from elasticsearch import Elasticsearch

#Instantiate Elasticsearch
es = Elasticsearch(HOST="http://localhost", PORT=9200)
es = Elasticsearch()

# Analyzers can be specified per-query, per-field or per-index.
# Types of Analysers:
#
#     Standard Analyzer
#     Simple Analyzer
#     Whitespace Analyzer
#     Stop Analyzer
#     Keyword Analyzer
#     Pattern Analyzer
#     Language Analyzers
#     Fingerprint Analyzer
#
# NOTE ON FINGERPRINT ALGORITHM:
#
# It implements fingerprint algorithm which
#
#     remove leading and trailing whitespace
#     change all characters to their lowercase representation
#     remove all punctuation and control characters
#     normalize extended western characters to their ASCII representation (for example "gödel" → "godel")
#     split the string into whitespace-separated tokens
#     sort the tokens and remove duplicates and join the tokens back together
#     Hence, Fenerbahceli Enes will be represented as enes fenerbahceli

res =   es.indices.analyze(body={
          "analyzer" : "standard",
          "text" : ["HELLO today is A GREAT DAY"]
        })
print(res)

#output is
# {'tokens':
#  [{'token': 'hello', 'start_offset': 0, 'end_offset': 5, 'type': '<ALPHANUM>', 'position': 0},
#   {'token': 'today', 'start_offset': 6, 'end_offset': 11, 'type': '<ALPHANUM>', 'position': 1},
#   {'token': 'is', 'start_offset': 12, 'end_offset': 14, 'type': '<ALPHANUM>', 'position': 2},
#   {'token': 'a', 'start_offset': 15, 'end_offset': 16, 'type': '<ALPHANUM>', 'position': 3},
#   {'token': 'great', 'start_offset': 17, 'end_offset': 22, 'type': '<ALPHANUM>', 'position': 4},
#   {'token': 'day', 'start_offset': 23, 'end_offset': 26, 'type': '<ALPHANUM>', 'position': 5}]}

analyzer = ['standard','simple','whitespace','stop','keyword','pattern','fingerprint']

for analyze in analyzer:
    res = es.indices.analyze(body={
      "analyzer" : analyze,
      "text" : ["HELLO WORLD. Today is the 2nd day of the week!!!!     it is Monday."]
    })
    print("======",analyze,"========")
    for i in res['tokens']:
        print(i['token'])
    print("\n")

#When we need to create index with analyzer;

body = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
            "properties": {
                "text": {
                    "type": "text",
                    "fields": {
                      "english": {
                        "type":     "text",
                        "analyzer": "whitespace"
                      }
                    }
                }
            }
        }
}
# create index
es.indices.create(index="tutorial_9", ignore=400, body=body)


res = es.indices.analyze(index="tutorial_9", body = {
  "field": "text.whitespace",
  "text": "The quick Brown Foxes   ."
})
for i in res['tokens']:
    print(i['token'])
