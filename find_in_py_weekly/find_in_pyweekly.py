from issue import IssueAfter338, IssueBefore339
from find_out_latest_issue import find_out_latest_issue
from article import ArticleAfter338, ArticleBefore338, Article338

latest_issue = find_out_latest_issue()
earliest_issue = 232  # September 1, 2016


def block(issue_class, article_class):
    try:
        current_issue = issue_class(number)
        articles_in_tags = current_issue.extract_articles_from_page()
        for item in articles_in_tags:
            current_article = article_class(item)
            current_article.search(words)
    except Exception as e:
        print(number)
        print(e)


if __name__ == '__main__':
    words = input('Enter key words for articles you want to find: ').split()
    if len(words) == 0:
        exit()

    for number in reversed(range(339, latest_issue + 1)):
        block(IssueAfter338, ArticleAfter338)
    for number in [338]:
        block(IssueBefore339, Article338)
    for number in reversed(range(earliest_issue, 338)):
        block(IssueBefore339, ArticleBefore338)

user_exit = input('Print "exit" if you want to shut window down: ')
if user_exit == "exit":
    exit()
