import yake

# Simple keyword extractor using YAKE, this finds 4 prominent keywords with a max of one engram per keyword.

language = "en"
max_ngram_size = 1
deduplication_threshold = 0.7
deduplication_algo = "seqm"
numOfKeywords = 4

class Custom_Keyword_Extract:
    def __init__(self):
        self.custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, dedupFunc=deduplication_algo, top=numOfKeywords, features=None)
    
    def extract_keywords(self, text):
        keywords = self.custom_kw_extractor.extract_keywords(text)
        return [(kw, score) for kw, score in keywords]



