
import os
from google.generativeai import configure, GenerativeModel
import datetime

configure(api_key=os.environ['GEMINI_API_KEY'])
model = GenerativeModel('gemini-1.5-flash')
affiliate_id = os.environ['AFFILIATE_ID']

niche = 'tech-ai'
lang = 'pt'
prompt = f"Article SEO quotidien 1500 mots pour tech-ai en pt, keywords, affiliates https://amazon.com/product?tag={affiliate_id}"
content = model.generate_content(prompt).text

date = datetime.date.today().strftime("%Y-%m-%d")
os.makedirs('articles', exist_ok=True)
with open(f'articles/{date}.html', 'w', encoding='utf-8') as f:
    f.write(f"<h1>Daily tech-ai Tip</h1>{content}")

# Backlinks (exemple simple)
import requests
requests.post('https://www.freebacklink.net/submit', data={'url': f'https://tech-ai-pt-newtech70.vercel.app'})
