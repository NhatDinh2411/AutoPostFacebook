from transformers import pipeline
from typing import List

def summarize(text_papers: List ) -> List:
    model = pipeline("summarization", model="VietAI/vit5-large-vietnews-summarization")
    summarized_papers = [item['summary_text'] for item in model(text_papers)]
    return summarized_papers