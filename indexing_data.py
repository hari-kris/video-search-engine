import os
import re
from elasticsearch import helpers
from elasticsearch import Elasticsearch
es = Elasticsearch()
input_path = "/data/BITS/SEM-3/ASSIGNMENT-2/TEXT-2/"
video_path = "/data/BITS/SEM-3/ASSIGNMENT-2/VIDEO/"
file_name_regex = r"(.*\.mp4)_Frame_(\d+)"
index_array = []
bulk_size = 500


def elasticsearch_bulk_indexing(action):
    """
    Perform Bulk Indexing on the document
    :param action: array containing data to be indexed
    :return: None
    """
    print("Processing")
    helpers.bulk(es, action)


def process_document_in_folder(input_path):
    """
    Process the text file present in the folder and convert into JSON object
    which can be indexed by the Elasticsearach
    :param input_path:
    :return:
    """
    files = os.listdir(input_path)
    for file in files:
        input_dict = {
            "_index": "video-recommendation",
            "_source":
                {
            "file_name": "",
            "file_content": "",
            "file_location": "",
            "frame_number": ""
            }
        }
        file_content = open(input_path+file).read()
        input_dict["_source"]["file_content"] = file_content
        pattern = re.search(file_name_regex, file)
        file_name = pattern.group(1)
        frame_number = pattern.group(2)
        input_dict["_source"]['file_name'] = file_name
        input_dict["_source"]["file_location"] = video_path + file_name
        input_dict["_source"]["frame_number"] = frame_number
        # print(input_dict)
        print("Indexing")
        # es.index(index="video-recommendation", body=input_dict)
        index_array.append(input_dict)
        if (len(index_array) == bulk_size):
            elasticsearch_bulk_indexing(index_array)
            index_array = []
    elasticsearch_bulk_indexing(index_array)
    actions = []


if __name__ == '__main__':
    process_document_in_folder(input_path)