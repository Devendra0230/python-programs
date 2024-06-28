import re
import requests
import csv

def scrape_data(url):
    response = requests.get(url)
    text = response.text
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    phone_numbers = re.findall(r'\b\d{10}\b', text)
    return emails, phone_numbers

def write_to_csv(data):
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Email', 'Phone Number'])
        writer.writerows(data)

with open('example_links.txt', 'r') as file:
    urls = file.readlines()

data = []
for url in urls:
    url = url.strip()
    emails, phone_numbers = scrape_data(url)
    data.extend(zip(emails, phone_numbers))

write_to_csv(data)

