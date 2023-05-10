import nltk
from nltk.corpus import reuters
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from summa import summarizer
from transformers import pipeline


# Download and install the Reuters Corpus dataset
#nltk.download('reuters')

# Get the list of categories
categories = reuters.categories()

# Set up the training and testing categories
training_categories = categories[:10]

# Get the fileids 
training_fileids = reuters.fileids(categories=training_categories)

# Get the raw text for each document 
training_docs = [reuters.raw(fileid) for fileid in training_fileids]

# Tokenize the docs
stop_words = stopwords.words('english')
tokenized_training_docs = [[word.lower() for word in word_tokenize(doc) if word.isalpha() and word.lower() not in stop_words] for doc in training_docs]
tfidf_vectorizer = TfidfVectorizer()
tfidf_training_features = tfidf_vectorizer.fit_transform([' '.join(doc) for doc in tokenized_training_docs])

# Define the summarization pipeline
summarizer = pipeline("summarization")

# Prompt the user to enter a query
query = input("Enter a query: ")

# Find the top k most similar documents for each test doc
tfidf_test_doc = tfidf_vectorizer.transform([query])
cosine_similarities = cosine_similarity(tfidf_training_features)
k = 3
most_similar_indices = cosine_similarities.argsort()[:, :-k-1:-1]

# Define the number of sentences in the summary
summary_length = 3

# Print the most similar documents for each test doc
for i, test_doc in enumerate(training_docs):
    tfidf_test_doc = tfidf_vectorizer.transform([test_doc])
    cosine_similarities = cosine_similarity(tfidf_test_doc, tfidf_training_features)
    most_similar_indices = cosine_similarities.argsort()[:, :-k-1:-1]
    print(f"Most similar documents to test doc {i+1}:")
    
    # Get the summaries of the most similar documents
    summaries = []
    for j, idx in enumerate(most_similar_indices[i]):
        doc = training_docs[idx]
        summary = summarizer(doc, max_length=50, min_length=10, do_sample=False)
        summaries.append(f"{j+1}. {summary[0]['summary_text']}")
    
    # Print the summaries
    print("Summaries:")
    print("\n".join(summaries))