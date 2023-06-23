import tensorflow as tf
from transformers import TFBartForConditionalGeneration, BartTokenizer
import concurrent.futures
import tqdm

max_cores = 2

class BARTSummarizer:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        self.model = TFBartForConditionalGeneration.from_pretrained(model_name)
        self.tokenizer = BartTokenizer.from_pretrained(model_name)

    def summarize(self, text):
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_cores) as executor:
            future = executor.submit(self.generate_summary, text)
            summary = future.result()
            return summary
    
    def generate_summary(self, text):
        inputs = self.tokenizer.encode_plus(text, truncation=True, max_length=1024, padding="longest", return_tensors="tf")
        input_ids = tf.cast(inputs["input_ids"], dtype=tf.int32)
        summary_ids = self.model.generate(input_ids, num_beams=4, max_length=150, early_stopping=True)
        summary = self.tokenizer.decode(summary_ids.numpy()[0], skip_special_tokens=True)
        return summary
        
    # This section is designed to handle large amounts of text automatically. It will split content at the threshold and summarize it separately, appending it to the final summary.
    
    def summarize_large_text(self, text):
        chunks = [text[i : i + 1024] for i in range(0, len(text), 1024)]
        summaries = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_cores) as executor:
            futures = [executor.submit(self.summarize, chunk) for chunk in chunks]
            for future in tqdm.tqdm(concurrent.futures.as_completed(futures), total=len(futures)):
                try:
                    summary = future.result()
                    if summary:
                        summaries.append(summary)
                except Exception as e:
                    print(f"An error has occured during summarization: {str(e)}")
                    return None
        
        full_summary = " ".join(summaries)
        return full_summary



