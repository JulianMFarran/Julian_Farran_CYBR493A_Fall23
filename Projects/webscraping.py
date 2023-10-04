import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL you want to scrape
url = 'https://wvrnboard.wv.gov/Pages/Search.aspx?q=workforce%20data'  # Replace with the URL of the website you want to scrape

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the elements you want to scrape (e.g., <div> tags with specific class names)
    # For example, let's extract all the links on the page
    links = soup.find_all('a')

    # Create a list to store the extracted data
    data_list = []

    # Iterate through the links and extract their text and href attributes
    for link in links:
        link_text = link.text
        link_href = link.get('href')
        data_list.append([link_text, link_href])

    # Create a Pandas DataFrame from the data list
    df = pd.DataFrame(data_list, columns=['Link Text', 'Link Href'])

    # Define the name of the Excel file you want to create
    excel_file = 'web_data.xlsx'

    # Save the DataFrame to an Excel file
    df.to_excel(excel_file, index=False)

    print(f'Data has been scraped and saved to {excel_file}')
else:
    print('Failed to retrieve the web page.')

