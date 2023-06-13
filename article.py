import requests
from bs4 import BeautifulSoup

# This class handles the articles provided by the user. It is able to differentiate between URLs, files, and text entries.

class Article:
    def __init__(self, source):
        self.source = source
        self.text = ""
    
    def fetch_text(self):
        if self.source.startswith("http"):
            self.fetch_text_from_url()
        else:
            self.fetch_text_from_file()

    def fetch_text_from_url(self):
        response = requests.get(self.source)
        html_content = response.text

        soup = BeautifulSoup(html_content, "html.parser")
        article_text = soup.get_text(separator=" ")
        self.text = article_text

    def fetch_text_from_file(self):
        with open(self.source, "r", encoding="utf-8") as file:
            self.text = file.read()

    def get_text(self):
        return self.text