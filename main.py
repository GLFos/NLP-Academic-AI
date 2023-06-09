from article import Article
from bart import BARTSummarizer

#Add error handling, the option for users to proceed if there is a warning (y/n), and the breakdown of larger texts into chunks so the AI can be more effecient. 
summarizer = BARTSummarizer()

article_content = "https://www.usatoday.com/story/news/world/2023/06/09/billions-in-military-aid-for-ukraine-announced-by-biden-administration/70306190007/"

article = Article(article_content)
article.fetch_text()
content = article.get_text()  
summary = summarizer.summarize(content)

print(summary)

