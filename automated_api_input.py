import requests
import pyalex
import pysolr
import json

pyalex.config.email = "garrisonlukefoster@outlook.com"

random_work_url = 'http://api.openalex.org/works?sample=14&per-page=14'
response = requests.get(random_work_url)
response.raise_for_status()
data = response.json()

solr = pysolr.Solr('http://localhost:8983/solr/test_1', always_commit=True)

for result in data['results']:
    id = result['id']
    doi = result['doi']
    title = result['title']
    authors = [author['author']['display_name'] for author in result['authorships']]
    publication_year = result['publication_year']
    language = result['language']

    doc = {
        'id': id,
        'doi': doi,
        'title': title,
        'author': ', '.join(authors),
        'publication_year': publication_year,
        'language': language
    }

    solr.add([doc])

solr.commit()
