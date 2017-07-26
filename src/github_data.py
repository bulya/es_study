import os

from dotenv import load_dotenv
from github import Github

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")


if __name__ == '__main__':
    print(GITHUB_TOKEN)
    g = Github(GITHUB_TOKEN)
    r = g.get_repo('diviac/diviac')
    print(r)
    print(r.__dict__)
    commits = r.get_commits()
    print(commits[0].__dict__)

