

import os
from posixpath import split
import openai
import textwrap
import urllib
import json
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

def get_companies_names(symbols_list):
    """"
    Function for getting companies names based on stock symbol from prvided symbols list"""
    data_dict = {}
    for c in symbols_list:
        symbol = c.strip()
        response = urllib.request.urlopen(f'https://query2.finance.yahoo.com/v1/finance/search?q={symbol}')
        content = response.read()
        company_name = json.loads(content.decode('utf8'))['quotes'][0]['shortname']
        data_dict[symbol] = company_name
    return data_dict


def get_quarterly_income(company_symbol):
    """
    Function for getting quarterly income table report for company
    """
    company_thicker = yf.Ticker(company_symbol.strip())
    return company_thicker.quarterly_income_stmt


def get_companies_fininfo(companies):
    """
    Function for compailing each company financial info in a dict
    """
    companies_dict = {}
    for c in companies:  
        companies_dict[c.strip()] = get_quarterly_income(c)

    return companies_dict


def get_historical_data(company_symbol, period):
    """"
    Funtion that shows information about the historical stock prices
    """
    company_thicker = yf.Ticker(company_symbol.strip())
    hist_prices = company_thicker.history(period=period)
    return hist_prices


def get_companies_hist_data(companies, period):
    """"
    Funtion compaling historical stock price data for each company in a dict
    """
    companies_hist_data_dict = {}
    for c in companies:  
        companies_dict[c.strip()] = get_historical_data(c, period)

    return companies_hist_data_dict



                                ###### Execution ######

companies = select_stocks()
companies_dict = get_companies_fininfo(companies)
companies_hist_data_dict = get_companies_hist_data(companies, "1mo")
companies_names_dict = get_companies_names(companies)


# Create OpenAI promt
prompt = f""""
Based on the following companies financial data and historical data with complete names based on the provided symbols, which company performed better and based on their stock historical data which is in a lower price?\t 
Companies symbols and names: {companies_names_dict} \t
Finantial data: {companies_dict} \t
Historical data: {companies_hist_data_dict}"""


# Configure OpenAI response
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k",
    messages=[{ "role": "user", "content": prompt}],
    max_tokens=1000  
)

# Give Format to text
formatted_response = textwrap.fill(response.choices[0].message.content, width=80)

# Print OpenAI response 
print(formatted_response)

