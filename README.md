# AutoPostFacebook 🤖📢

**AutoPostFacebook** is an automated content pipeline that scrapes daily information from the web, summarizes it using AI, generates an illustrative image, and publishes a fully composed post to Facebook at a scheduled time.

---

## 🚀 Overview

This project aims to:
- Automate content generation using LLMs and image models
- Reduce manual effort for daily page content
- Maintain consistent social media engagement with minimal input

---
## 📸 Demo 
![Screenshot of my post](images/image_1.png)

---
## 🧩 Key Features

- 🔍 **Scraper** *(planned)*: Automatically fetch daily news, articles, or data from the internet.
- ✂️ **Summarizer**: Uses AI to shorten raw content into concise, readable summaries.
- 🧠 **Text Prompt Generator**: Transforms the summary into an image prompt suitable for visual storytelling.
- 🖼️ **Image Generator**: Uses the prompt to create an image using AI models (e.g., DALL·E or Stable Diffusion).
- 📤 **Facebook Poster**: Publishes the post (summary + generated image) directly to a Facebook page using the Graph API.
- ⏰ **Scheduler**: Runs the entire pipeline automatically every day at 8:00 AM (can be customized).

---

## 📂 Project Structure
```
AutoPostFacebook/
│
├── facebook_poster/           # Handles Facebook Graph API posting
│   ├── init.py
│   └── fb_api.py
│
├── image_generator/           # Generates images from text prompts
│   ├── init.py
│   └── generate_image.py
│
├── scraper/                   # (Planned) Web scraper module
│
├── text_processing/           # Text summarization and prompt generation
│   ├── init.py
│   ├── summarizer.py          # Reduces raw text to a short summary
│   └── text_generator.py      # Converts summary into an image-style prompt
│
├── utils/                     # Common utilities and logging
│   ├── init.py
│   ├── helpers.py
│   └── logger.py
│
├── venv/                      # Python virtual environment (optional)
├── .env                       # Environment variables (not committed)
├── main.py                    # Entry point for the pipeline
├── requirements.txt           # Python package dependencies
└── README.md                  # Project documentation

```
---

## ⚙️ Setup Guide

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AutoPostFacebook.git
cd AutoPostFacebook
```
### 2. Set up the Python Environment
```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Configure Environment Variables
Create a .env file in the root directory with the following keys:
```bash
OPENAI_API_KEY=your_openai_key
FACEBOOK_PAGE_TOKEN=your_facebook_page_token
FACEBOOK_PAGE_ID=your_facebook_page_id
```
> 🔒 Make sure not to commit .env to version control.
---
# 🧪 How It Works

> 1.	**Scrape or manually input content** (e.g., article, daily update).	
> 2.	summarizer.py condenses the content to 5–10 concise sentences.
> 3. text_generator.py creates an image prompt from that summary.
> 4.	generate_image.py uses an AI model to create a relevant image.
> 5.	fb_api.py posts the summary + image to your Facebook page.
> 6.	main.py ties it all together and runs on a daily schedule.
---
# 🕒 Automation
The system uses Python’s schedule library to run automatically every day at 08:00 AM. You can customize the time inside main.py.
```
    job(main, at_time="8:30")
```
---
# 🔧 Requirements
- Python 3.12+
- OpenAI account (for summarization and prompt generation)
- ebook Page & Access Token (via Facebook Graph API)
- image model access (DALL·E, Stable Diffusion, etc.)
