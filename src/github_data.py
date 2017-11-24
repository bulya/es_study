import os

from dotenv import load_dotenv
from github import Github
from elasticsearch import Elasticsearch

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
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

INDEX_NAME = 'github_data'

es = Elasticsearch([ES_URL])


def ensure_index():
    es.indices.create(index=INDEX_NAME, ignore=400)

def get_github_commits():



if __name__ == '__main__':
    ensure_index()

    print(GITHUB_TOKEN)
    g = Github(GITHUB_TOKEN)
    r = g.get_repo('diviac/diviac')
    print(r)
    print(r.__dict__)
    commits = r.get_commits()
    print(commits[0].__dict__)

