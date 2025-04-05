import os
from facebook_poster.fb_api import post_facebook
from image_generator.generate_image import generate_image
from scraper.scraper import get_paper
from text_processing.text_generator import createAnalysis
from text_processing.summarizer import summarize
from datetime import datetime
from dotenv import load_dotenv
from utils.helpers import job

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_TOKEN")
FACEBOOK_TOKEN = os.getenv("FACEBOOK_TOKEN")
FACEBOOK_PAGEID = os.getenv("PAGE_ID")
os.makedirs("images", exist_ok=True)

def main():
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    save_path = f"images/{now}.png"

    text_papers = get_paper()
    summarized_papers = summarize(text_papers=text_papers)
    llm_output = createAnalysis(detail_papers=summarized_papers, OPENAI_KEY=OPENAI_KEY)
    generate_image(prompt=llm_output['prompt'], OPENAI_KEY=OPENAI_KEY, save_path=save_path)
    post_facebook(llm_output['phân tích'], access_token=FACEBOOK_TOKEN, page_id=FACEBOOK_PAGEID, image_path=save_path)

if __name__ == "__main__":
    job(main, at_time="8:30")

