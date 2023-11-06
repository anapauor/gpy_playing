

import os
import openai
import textwrap
import yfinance as yf
from dotenv import load_dotenv

# Configure API key - OpenAI
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key


# Get yfinance data
stock = input("Select stock: ").upper()

# select financials and take querterly income:
selected_stock = yf.Ticker(stock)
stock_quarterly_income = (selected_stock.quarterly_income_stmt)
msft_stock = selected_stock = yf.Ticker("MSFT")
msft_quarterly_income = (msft_stock.quarterly_income_stmt)

# Create OpenAI promt
prompt = f"Based on the following two companies financial data, which company performed better? Firts company: {stock_quarterly_income} Seccond company: {msft_quarterly_income}"


# Configure OpenAI response
response = openai.chat.completions.create(
    model="gpt-3.5-turbo-16k",
    messages=[{ "role": "user", "content": prompt}],
    max_tokens=1000  
)

# Give Format to text
formatted_response = textwrap.fill(response.choices[0].message.content, width=80)

# Print OpenAI response 
print(formatted_response)
