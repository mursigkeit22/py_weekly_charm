from abc import ABC, abstractmethod
import re
import requests
from bs4 import BeautifulSoup
import bs4
from typing import List


class Issue(ABC):

    def __init__(self, number: int):
        self.page_link: str = 'https://pycoders.com/issues/' + str(number)
        self.page_response: requests.models.Response = requests.get(self.page_link)
        self.page: bs4.BeautifulSoup = BeautifulSoup(self.page_response.content, 'html.parser')
        self.page_element_with_articles: bs4.PageElement = self.get_element()
        self.issue_articles: list = []

    @abstractmethod
    def get_element(self) -> bs4.element.Tag:
        pass

    @abstractmethod
    def extract_articles_from_page(self) -> List:
        pass

    def add_article_to_issue(self, article: List[bs4.element.Tag]) -> None:
        if len(article) >= 2 and article[-1].string != 'sponsor' and article[-1].string != 'video':
            self.issue_articles.append(article)


class IssueAfter338(Issue):

    def get_element(self) -> bs4.element.Tag:
        element = self.page.find('td', class_='mcnTextContent', style=re.compile('padding-top'), valign='top')
        return element

    def extract_articles_from_page(self) -> List:
        page_element_iterable = iter(self.page_element_with_articles)
        article: List[bs4.element.Tag] = []
        for element in page_element_iterable:
            if not element.name:
                continue
            if element.name == 'br':
                if element.next_element.name == "br":
                    self.add_article_to_issue(article)
                    article = []
                    continue
                elif not element.next_element.name:
                    if element.next_element.next_element.name == "br":
                        self.add_article_to_issue(article)
                        article = []
                        continue
                continue
            if element.name == 'h2' and element.string == "Python Jobs":
                while True:
                    element = next(page_element_iterable)
                    if element.name == 'h2' and element.string == 'Articles & Tutorials':
                        break

            if element.name == 'h2' and element.string == "Projects & Code":
                self.add_article_to_issue(article)
                break
            if element.name == 'span':
                article.append(element)
        return self.issue_articles


class IssueBefore339(Issue):

    def get_element(self) -> bs4.element.Tag:
        element = self.page.find('h2', string='Articles')
        return element

    def extract_articles_from_page(self) -> List :
        article: List[bs4.element.Tag] = []
        for element in self.page_element_with_articles.next_siblings:
            if not element.name:
                continue
            if element.name == 'br':
                if element.next_element.name == "br":
                    self.add_article_to_issue(article)
                    article = []
                    continue
                elif not element.next_element.name:
                    if element.next_element.next_element.name == "br":
                        self.add_article_to_issue(article)
                        article = []
                        continue
                continue
            if element.name == 'h2':
                self.add_article_to_issue(article)
                break
            article.append(element)
        return self.issue_articles
