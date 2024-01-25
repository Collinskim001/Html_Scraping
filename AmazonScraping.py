import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# Function to fetch HTML content from the file
def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to parse HTML content and extract information
def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all divs with id="search"
    search_divs = soup.find_all('div', id='search')

    samsung_data = []

    for search_div in search_divs:
        # Find all divs with class="puisg-row"
        puisg_row_divs = search_div.find_all('div', class_='puisg-row')

        for puisg_row_div in puisg_row_divs:
            # Find div with class="puisg-col-inner" and store its text in Samsung_name
            puisg_col_inner_div = puisg_row_div.find('div', class_='puisg-col-inner')
            samsung_name = puisg_col_inner_div.text.strip() if puisg_col_inner_div else 'N/A'

            # Find span with class="a-price-whole" and store its text in Price
            price_span = puisg_row_div.find('span', class_='a-price-whole')
            price = price_span.text.strip() if price_span else 'N/A'

            samsung_data.append({'Samsung_name': samsung_name, 'Price': price})

    return samsung_data

# Function to write data to Excel file
def write_to_excel(data, excel_file):
    workbook = Workbook()
    sheet = workbook.active

    # Write headers
    sheet.append(['Samsung_name', 'Price'])

    # Write data
    for row in data:
        sheet.append([row['Samsung_name'], row['Price']])

    # Save the Excel file
    workbook.save(excel_file)

if __name__ == "__main__":
    # File path for the HTML file
    html_file_path = "Amazon.com _ samsung phones.html"

    # Excel file path to save the extracted data
    excel_file_path = "samsung_data.xlsx"

    # Read HTML content from the file
    html_content = read_html_file(html_file_path)

    # Parse HTML content and extract information
    extracted_data = parse_html(html_content)

    # Write data to Excel file
    write_to_excel(extracted_data, excel_file_path)

    print("Data extraction and Excel writing completed.")
