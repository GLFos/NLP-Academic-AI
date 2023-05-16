import pyalex
from pyalex import Works, Authors, Sources, Institutions, Concepts, Publishers
import requests
import pprint
import json

# Solr Startup command on cmd is "solr start -p 8983"
# Web address once running is " http://localhost:8983/solr/ "


pyalex.config.email = "example@email.com"

Random_Works_Url = 'http://api.openalex.org/works?sample=100&per-page=100'

response = requests.get(url=Random_Works_Url)
response.raise_for_status()
random_work = response.json()

results = random_work['results']
formatted_results = []

for result in results:
    title = result['title']
    authors = [author['author']['display_name'] for author in result['authorships']]
    publication_year = result['publication_year']
    language = result['language']

    formatted_result = {
        'Title': title,
        'Authors': ", ".join(authors),
        'Publication Year': publication_year,
        'Language': language
    }

    formatted_results.append(formatted_result)

current_id = 1

with open('output.txt', 'w', encoding='utf-8') as f:
    for result in formatted_results:
        f.write("{\n")
        f.write(f'  "id": "{current_id}",\n')
        f.write(f'  "Title": "{result["Title"]}",\n')
        f.write(f'  "author": "{result["Authors"]}",\n')
        f.write(f'  "publication_year": "{result["Publication Year"]}",\n')
        f.write(f'  "language": "{result["Language"]}"\n')
        f.write("},\n\n")
        
        current_id += 1
