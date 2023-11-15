import requests
from bs4 import BeautifulSoup

def get_cwe_information(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract View ID and Type
        view_id_div = soup.find('div', class_='status')
        view_id = view_id_div.find('div', style='font-weight:bold').text.strip() if view_id_div else "N/A"
        view_type = view_id_div.find('span', style='font-size:80%').text.strip() if view_id_div else "N/A"

        # Extract Objective
        objective_div = soup.find('div', id='Objective')
        objective = objective_div.find('div', class_='detail').text.strip() if objective_div and objective_div.find('div', class_='detail') else "N/A"

        # Extract Audience
        audience_div = soup.find('div', id='Audience')
        if audience_div:
            audience_table = audience_div.find('table', class_='Detail')
            audience_rows = audience_table.find_all('tr')
            audience_data = [(row.find('td', valign='middle').text.strip(), row.find_all('td')[1].text.strip()) for row in audience_rows[1:]]  # Skip the header row
        else:
            audience_data = []

        # Extract Relationships
        relationships_div = soup.find('div', id='Relationships')
        relationships_text = relationships_div.find('div', class_='indent').text.strip() if relationships_div and relationships_div.find('div', class_='indent') else "N/A"

        # Return the extracted information
        return {
            'View ID': view_id,
            'Type': view_type,
            'Objective': objective,
            'Audience': audience_data,
            'Relationships': relationships_text
        }
    else:
        print(f'Failed to fetch the URL. Status code: {response.status_code}')
        return None

def print_cwe_information(cwe_info):
    if cwe_info:
        print(f'View ID: {cwe_info["View ID"]}')
        print(f'Type: {cwe_info["Type"]}')
        print(f'Objective: {cwe_info["Objective"]}')
        print('Audience:')
        for stakeholder, description in cwe_info['Audience']:
            print(f'  - {stakeholder}: {description}')
        print(f'Relationships: {cwe_info["Relationships"]}')

# Replace 'your_url_here' with the actual URL containing the CWE information
url = 'https://cwe.mitre.org/data/definitions/888.html'

# User prompt
choice = input("Do you want to view all IDs (A) or a specific one (S)? ").upper()

if choice == 'A':
    # Extract and print information for all IDs
    # Modify the URL pattern based on how the IDs are structured on the website
    for cwe_id in range(1, 1000):  # Assuming IDs are between 1 and 1000
        url = f'https://cwe.mitre.org/data/definitions/{cwe_id}.html'
        cwe_info = get_cwe_information(url)
        print_cwe_information(cwe_info)
elif choice == 'S':
    # Allow the user to input a specific ID
    specific_id = input("Enter the specific ID you want to view: ")
    url = f'https://cwe.mitre.org/data/definitions/{specific_id}.html'
    cwe_info = get_cwe_information(url)
    print_cwe_information(cwe_info)
else:
    print("Invalid choice. Please choose 'A' or 'S'.")
