import tensorflow as tf
from transformers import TFBartForConditionalGeneration, BartTokenizer

class BARTSummarizer:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        self.model = TFBartForConditionalGeneration.from_pretrained(model_name)
        self.tokenizer = BartTokenizer.from_pretrained(model_name)

    def summarize(self, text):
        inputs = self.tokenizer.encode_plus(text, truncation=True, max_length=1024, padding="longest", return_tensors="tf")
        input_ids = tf.cast(inputs["input_ids"], dtype=tf.int32)
        summary_ids = self.model.generate(input_ids, num_beams=4, max_length=150, early_stopping=True)
        summary = self.tokenizer.decode(summary_ids.numpy()[0], skip_special_tokens=True)
        return summary


