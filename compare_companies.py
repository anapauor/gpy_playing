

import os
import openai
import textwrap
import yfinance as yf
from dotenv import load_dotenv

# Configure API key - OpenAI
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

def get_quarterly_income(company_name):
    company = yf.Ticker(company_name)
    return company.quarterly_income_stmt

def compare_companies(first_company, second_company):
    """
    Function for comparing two companies performance in last quarter period
    """
    first_company_income = get_quarterly_income(first_company)
    second_company_income = get_quarterly_income(second_company)

    return first_company_income, second_company_income

    return first_stock_quarterly_income, seccond_stock_quarterly_income

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
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1000  
)

# Give Format to text
formatted_response = textwrap.fill(response.choices[0].text, width=80)

# Print OpenAI response 
print(formatted_response)

