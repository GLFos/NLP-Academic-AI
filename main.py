from article import Article
from summarizer import Summarizer

#Add error handling, the option for users to proceed if there is a warning (y/n), and the breakdown of larger texts into chunks so the AI can be more effecient. 
summarizer = Summarizer()

article_content = " "

article = Article(article_content)
article.fetch_text()

content = article.get_text()  
summary = summarizer.summarize(content)

print(summary)

