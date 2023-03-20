import requests
from bs4 import BeautifulSoup

# scrape the links from the website
url = input("Enter your website to be scraped: ")
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
links = [link.get("href") for link in soup.find_all("a")]

# write the links to a txt file
with open("Web Scraper/links.txt", "w") as file:
    for link in links:
        file.write(link + "\n")
