from elasticsearch import Elasticsearch
es = Elasticsearch()


def query_parser(query):
    """
    Understand the query raised by the user and convert into Elasticsearch format
    :param query: user query
    :return: number of hits, unique file name and file location back to the user
    """
    query_body = {
        "size": 100,
      "query": {
          "match_phrase": {
              "file_content": query
          }
      }
    }
    result = es.search(index="video-recommendation", body=query_body)
    unique_file_name = set()
    unique_file_location = set()
    for each in result['hits']['hits']:
        unique_file_name.add(each['_source']['file_name'])
        unique_file_location.add(each['_source']['file_location'])
        # print(each['_source']['file_name'])
    number_of_occurence = result['hits']['total']['value']

    return (number_of_occurence, unique_file_name, unique_file_location)


if __name__ == '__main__':
    query = "data mining"
    query_parser()