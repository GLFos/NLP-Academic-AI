import requests
from readability import Document
from bs4 import BeautifulSoup
import concurrent.futures

max_cores = 2

class Article:
    def __init__(self, source):
        self.source = source
        self.text = ""

    def fetch_text(self):
        if self.is_url():
            self.fetch_text_from_url()
        elif self.is_file():
            self.fetch_text_from_file()
        else:
            self.set_text(self.source)

    def is_url(self):
        return self.source.startswith("http") or self.source.startswith("https")

    def is_file(self):
        return isinstance(self.source, str) and self.source.endswith(".txt")

    def fetch_text_from_url(self):
        response = requests.get(self.source)
        html_content = response.text

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_cores) as executor:
            futures = [
                executor.submit(self.process_html_content, html_content),
                executor.submit(self.extract_article_text, html_content)
            ]
            concurrent.futures.wait(futures)

            processed_html_content = [future.result() for future in futures]

        document = Document(processed_html_content)
        article_html = document.summary()

        soup = BeautifulSoup(article_html, "html.parser")
        article_text = soup.get_text(separator=" ")
        self.set_text(article_text)

    def fetch_text_from_file(self):
        with open(self.source, "r", encoding="utf-8") as file:
            self.set_text(file.read())

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text
