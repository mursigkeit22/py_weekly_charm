import requests
from bs4 import BeautifulSoup


def find_out_latest_issue() -> int:
    issues_link = 'https://pycoders.com/issues'
    issues_page_response = requests.get(issues_link)
    issues_page = BeautifulSoup(issues_page_response.content, 'html.parser')
    latest_number = issues_page.find('h2').a['href'].split('/')[-1]
    return int(latest_number)
