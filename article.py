import requests
from readability import Document
from bs4 import BeautifulSoup
from docx import Document

class Article:
    def __init__(self, source):
        self.source = source
        self.text = ""

    def fetch_text(self):
        if self.is_url():
            self.extract_text_from_wikipedia()
        elif self.is_file():
            self.fetch_text_from_file()
        else:
            self.set_text(self.source)

    def is_url(self):
        return self.source.startswith("http") or self.source.startswith("https")

    def is_file(self):
        return isinstance(self.source, str) and (self.source.endswith(".txt") or self.source.endswith(".docx"))

    def extract_text_from_wikipedia(self):
        page_title = self.source.split('/')[-1]

        api_endpoint = f"https://en.wikipedia.org/api/rest_v1/page/summary/{page_title}"

        response = requests.get(api_endpoint)

        if response.status_code == 200:
            page_data = response.json()

            if 'extract' in page_data:
                self.set_text(page_data['extract'])
            else:
                self.set_text("Error: Unable to extract article text.")
        else:
            self.set_text("Error: Failed to retrieve the Wikipedia page.")

    def fetch_text_from_file(self):
        if self.source.endswith(".txt"):
            with open(self.source, "r", encoding="utf-8") as file:
                self.set_text(file.read())
        elif self.source.endswith(".docx"):
            document = Document(self.source)
            paragraphs = [paragraph.text for paragraph in document.paragraphs]
            self.set_text("\n".join(paragraphs))

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text