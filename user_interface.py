import streamlit as st
from elasticsearch import Elasticsearch
es = Elasticsearch()


def main():
    st.title('Video Recommendation Engine')
    query = st.text_input('Enter search words:')

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
    print(result['hits']['total']['value'])
    print(unique_file_location)
    print(unique_file_name)

    for each in unique_file_location:
        video_file = open(each, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        st.write(each)
    for each in unique_file_name:
        st.write(each)


if __name__ == '__main__':
    main()