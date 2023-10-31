

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
selected_stock = yf.Ticker(stock)
historical_data = selected_stock.history(period=period)

# Prepare data for OpenAI
historical_data_summary = historical_data.describe()

# Create OpenAI promt
prompt = f"Generate an abtract of the finantial data of {stock} from {period}:\n{historical_data_summary.to_string()}"
prompt = f"Cuáles son las  {stock} from {period}:\n{historical_data_summary.to_string()}"


# Configure OpenAI response
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1000  
)

# Print OpenAI needed response 
print(response.choices[0].text)
