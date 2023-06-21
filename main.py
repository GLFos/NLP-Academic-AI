from article import Article
from bart import BARTSummarizer
from keywords import Custom_Keyword_Extract

# This compiles all three of the main classes

summarizer = BARTSummarizer()
keyword_extractor = Custom_Keyword_Extract()

article_content = input("Enter your URL, file, or text: ")

article = Article(article_content)
article.fetch_text()
content = article.get_text()  
summary = summarizer.summarize(content)

print(summary)

keywords = keyword_extractor.extract_keywords(content)
for keyword, score in keywords:
    print(keyword, score)
