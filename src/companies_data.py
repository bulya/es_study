import os
import requests
from collections import deque
from itertools import starmap
from dotenv import load_dotenv
from elasticsearch import Elasticsearch


dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

es = Elasticsearch()
url = os.environ.get("API_OPENCORPORATE_URL")

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
	deque(map(
		lambda page:
			index_companies(page),
			range(int(os.environ.get("DEFAULT_OPENCORPORATE_INDEX_PAGES")))
	))
