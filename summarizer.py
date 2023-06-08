from transformers import TFAutoModelForSeq2SeqLM, AutoTokenizer
import requests
from bs4 import BeautifulSoup
import tensorflow as tf
import logging
import nltk

class Summarizer:
    def __init__(self):
        self.summarizing_model = "t5-base"
        self.model = TFAutoModelForSeq2SeqLM.from_pretrained(self.summarizing_model)
        self.tokenizer = AutoTokenizer.from_pretrained(self.summarizing_model, model_max_length=1024)
    
    def summarize(self, text):
        inputs = self.tokenizer.encode(text, return_tensors="tf")
        inputs = tf.reshape(inputs, (1, -1))
        outputs = self.model.generate(inputs, max_length=100)
        summary = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        sentences = nltk.sent_tokenize(summary)
        fixed_sentences = [sentence.capitalize() for sentence in sentences]
        fixed_summary = ' '.join(fixed_sentences)

        if fixed_summary[-1] not in [".", "?", "!"]:
            fixed_summary += "."
        
        fixed_summary = fixed_summary.replace(".", ". ")
        fixed_summary = fixed_summary.replace("  ", " ")
    
        return fixed_summary