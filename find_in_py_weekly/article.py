from abc import ABC, abstractmethod
from typing import Optional


class Article(ABC):
    href: Optional[str]
    summary: Optional[str]
    title: Optional[str]

    def __init__(self, article_in_tags) -> None:
        self.article_tags = article_in_tags
        self.title = None
        self.href = None
        self.summary = None
        self.get_data_from_articles_tags()

    def display(self) -> None:
        print(f'Found: {self.title} {self.href}')
        if self.summary:
            print(self.summary)
        print()

    def search(self, words) -> None:
        words = [word.lower() for word in words]
        if all(word in str(self.title).lower() for word in words) or all(
                word in str(self.summary).lower() for word in words):
            self.display()

    @abstractmethod
    def get_data_from_articles_tags(self) -> None:
        pass


class ArticleAfter338(Article):

    def get_data_from_articles_tags(self) -> None:
        self.href = self.article_tags[0].a['href']
        if self.article_tags[0].string:
            self.title = self.article_tags[0].string
        else:
            for child in self.article_tags[0].children:
                self.title = ' '.join(list(map(str, child.contents)))
        if len(self.article_tags) > 2:
            if self.article_tags[1].string:
                self.summary = self.article_tags[1].string
            else:
                self.summary = ' '.join(list(map(str, self.article_tags[1].contents)))


class ArticleBefore338(Article):

    def get_data_from_articles_tags(self) -> None:
        self.href = self.article_tags[0]['href']
        self.title = self.article_tags[0].contents[0].string
        self.summary = self.article_tags[1].string


class Article338(Article):

    def get_data_from_articles_tags(self) -> None:
        self.href = self.article_tags[0].contents[0]['href']
        self.title = self.article_tags[0].contents[0].string
        self.summary = self.article_tags[1].string
