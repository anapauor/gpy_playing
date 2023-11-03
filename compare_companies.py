

import os
from posixpath import split
import openai
import textwrap
import yfinance as yf
from dotenv import load_dotenv

# Configure API key - OpenAI
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

# Select financials and take querterly income and Get yfinance data

def select_stocks():
    """
    Function for creating a list of stocks from an input string separeted by commas
    """
    stocks = input("Select stock: ")
    stocks_list = stocks.split(",")
    return stocks_list


def get_quarterly_income(company_name):
    """
    Function for getting quarterly income table report for company
    """
    print(company_name)
    company = yf.Ticker(company_name.strip())
    return company.quarterly_income_stmt


def compare_companies(companies):
    """
    Function for compailing each companie info in a dict
    """
    companies_dict = {}
    for c in companies:  
        companies_dict[c.strip()] = get_quarterly_income(c)

    return companies_dict


companies = select_stocks()
companies_dict = compare_companies(companies)



# Create OpenAI promt
prompt = f"Based on the following cosmpanies financial data, which company performed better and why?: {companies_dict}"

print(prompt)

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

