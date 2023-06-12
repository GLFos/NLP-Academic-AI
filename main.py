from article import Article
from bart import BARTSummarizer

summarizer = BARTSummarizer()

article_content = " "

article = Article(article_content)
article.fetch_text()
content = article.get_text()  
summary = summarizer.summarize(content)

print(summary)

