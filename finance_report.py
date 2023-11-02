

import os
import openai
import yfinance as yf
from dotenv import load_dotenv

# Configure API key - OpenAI
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key


# Get yfinance data
stock = input("Select stock: ").upper()
period = input("Select the time period: ").upper()

# select financials and take querterly income:
selected_stock = yf.Ticker(stock)
stock_quarterly_income = (selected_stock.quarterly_income_stmt)


# Create OpenAI promt
prompt = f"Based on the following company financial data, how did this company performed? {stock_quarterly_income}"


# Configure OpenAI response
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1000  
)

# Print OpenAI needed response 
print(response.choices[0].text)
