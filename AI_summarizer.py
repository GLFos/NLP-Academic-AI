from transformers import TFAutoModelForSeq2SeqLM, AutoTokenizer
import requests
from bs4 import BeautifulSoup
import tensorflow as tf
import logging
import nltk

logging.getLogger("transformers").setLevel(logging.WARNING)

summarizing_model = "t5-base"
model = TFAutoModelForSeq2SeqLM.from_pretrained(summarizing_model)
tokenizer = AutoTokenizer.from_pretrained(summarizing_model, model_max_length=1024)

#article_urls = ["https://www.annualreviews.org/doi/abs/10.1146/annurev.so.13.080187.001021"]
text_file = "C:\\Users\\GLFos\\Documents\\Abstract.txt"
with open(text_file, "r", encoding="utf-8") as file:
    text = file.read()

'''
for url in article_urls:
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")
    article_text = soup.get_text(separator=" ")
'''
abstract_length = len(text)
if abstract_length < 1000:
    max_summary_length = 50
elif 1000 <= abstract_length < 2000:
    max_summary_length = 80
else:
    max_summary_length = 100

#Remeber to change text_file when going back to articles!
inputs = tokenizer.encode(text, return_tensors="tf")
inputs = tf.reshape(inputs, (1, -1))
outputs = model.generate(inputs, max_length=max_summary_length)
summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

#Cleaning the summary
sentences = nltk.sent_tokenize(summary)
fixed_sentences = [sentence.capitalize() for sentence in sentences]
fixed_summary = ' '.join(fixed_sentences)

#Add proper punctuation
if fixed_summary[-1] not in [".", "?", "!"]:
    fixed_summary += "."

#Splitting long sentences
fixed_summary = fixed_summary.replace(".", ". ")
fixed_summary = fixed_summary.replace("  ", " ")

#print('URL:', url)
print("Summary:", fixed_summary)
#print()
