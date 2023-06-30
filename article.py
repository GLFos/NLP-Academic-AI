import requests
from readability import Document
from bs4 import BeautifulSoup
from docx import Document
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
        return isinstance(self.source, str) and (self.source.endswith(".txt") or self.source.endswith(".docx"))

    def process_html_content(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        self.text = self.extract_article_text(soup)

    def extract_article_text(self, soup):
        return ""

    def fetch_text_from_url(self):
        response = requests.get(self.source)
        html_content = response.text

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_cores) as executor:
            future = executor.submit(self.process_html_content, html_content)
            concurrent.futures.wait([future])

        article_text = self.extract_text_from_html(html_content)
        self.set_text(article_text)

    def fetch_text_from_file(self):
        if self.source.endswith(".txt"):
            with open(self.source, "r", encoding="utf-8") as file:
                self.set_text(file.read())
        elif self.source.endswith(".docx"):
            document = Document(self.source)
            paragraphs = [paragraph.text for paragraph in document.paragraphs]
            self.set_text("\n".join(paragraphs))

    def extract_text_from_html(self, html):
        document = Document(html)
        article_html = document.summary()
        soup = BeautifulSoup(article_html, "html.parser")
        article_text = soup.get_text(separator=" ")
        return article_text

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text

