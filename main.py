from article import Article
from bart import BARTSummarizer
from keywords import Custom_Keyword_Extract

summarizer = BARTSummarizer()
keyword_extractor = Custom_Keyword_Extract()

article_content = "https://apnews.com/article/pandemic-fraud-waste-billions-small-business-labor-fb1d9a9eb24857efbe4611344311ae78"

article = Article(article_content)
article.fetch_text()
content = article.get_text()  
summary = summarizer.summarize(content)

print(summary)

keywords = keyword_extractor.extract_keywords(content)
for keyword, score in keywords:
    print(keyword, score)
