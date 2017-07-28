# es_study

## Setup

### Create environment
`mkvirtualenv -p python3 es_study`
### Install requirements
`pip install -r ./requirements.txt`
### Create .env file with private settitngs
`cp .env.example .env`
### Setup elasticsearch cluster with docker-compose
`docker-compose -f ./docker/docker-compose.yml` up
### Runscripts
* `cd ./src`
* `python github_data.py`
