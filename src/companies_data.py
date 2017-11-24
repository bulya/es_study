import os
from collections import deque
from itertools import starmap

import requests
from elasticsearch import Elasticsearch

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)


ES_HOST = os.environ.get("ES_HOST")
ES_PORT = os.environ.get("ES_PORT")
ES_USER = os.environ.get("ES_USER")
ES_PASSWORD = os.environ.get("ES_PASSWORD")

ES_URL = 'http://{user}:{password}@{host}:{port}/'.format(
    user=ES_USER,
    password=ES_PASSWORD,
    host=ES_HOST,
    port=ES_PORT
)

INDEX_NAME = 'companies_data'

es = Elasticsearch([ES_URL])

url = os.environ.get("API_OPENCORPORATE_URL")


def ensure_index():
    es.indices.create(index=INDEX_NAME, ignore=400)


# API provides basic info about companies with paginated result,
# function will index all companies from selected page in elastic
def index_companies(page):
    data = requests.get(url + "?page={}".format(page)).json()

    print("Indexing companies page {} ........".format(page))

    deque(starmap(
        lambda index, company:
            es.index(
                index="open-corporate-{}-{}".format(page, index),
                doc_type="company",
                id="{}-{}".format(page, index),
                body=company
            ),
        enumerate(data['results']['companies'])
    ))


if __name__ == '__main__':
    ensure_index()

    deque(map(
        lambda page:
            index_companies(page),
            range(int(os.environ.get("DEFAULT_OPENCORPORATE_INDEX_PAGES")))
    ))
