import tkinter as tk
import textwrap
from article import Article
from bart import BARTSummarizer
from keywords import Custom_Keyword_Extract

class SummarizerUI:
    def __init__(self, root):
        self.root = root
        self.summarizer = BARTSummarizer()
        self.keyword_extractor = Custom_Keyword_Extract()

        # UI elements
        self.label = tk.Label(root, text="Paste your URL or raw text here:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Summarize", command=self.process_input)
        self.button.pack()

        self.summary_label = tk.Label(root, text="Summary:")
        self.summary_label.pack()

        self.summary_text = tk.Text(root, height=10, width=70)
        self.summary_text.pack()

        self.keywords_label = tk.Label(root, text="Keywords:")
        self.keywords_label.pack()

        self.keywords_text = tk.Text(root, height=5, width=50)
        self.keywords_text.pack()

        self.another_button = tk.Button(root, text="Summarize Another", command=self.clear_input)
        self.another_button.pack()

    def process_input(self):
        article_text = self.entry.get()

        # Process the input
        article = Article(article_text)
        article.fetch_text()
        content = article.text
        summary = self.summarizer.summarize(content)

        # Update UI 
        self.summary_text.delete('1.0', tk.END)
        wrapped_summary = textwrap.fill(summary, width=70)
        self.summary_text.insert(tk.END, wrapped_summary)

        keywords = self.keyword_extractor.extract_keywords(content)
        self.keywords_text.delete('1.0', tk.END)
        for keyword, score in keywords:
            self.keywords_text.insert(tk.END, f"{keyword}: {score}\n")
    
    def clear_input(self):
        self.entry.delete(0, tk.END)
        self.summary_text.delete('1.0', tk.END)
        self.keywords_text.delete('1.0', tk.END)

def main():
    root = tk.Tk()
    root.title("REC (Alpha)")

    summarizer_ui = SummarizerUI(root)

    root.mainloop()

if __name__ == "__main__":
    main()
