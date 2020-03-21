from issue import IssueAfter338, IssueBefore339
from find_out_latest_issue import find_out_latest_issue
from article import ArticleAfter338, ArticleBefore338, Article338

latest_issue_number = find_out_latest_issue()
earliest_issue = 232  # September 1, 2016


def test_block(issue_class, article_class):
    try:
        current_issue = issue_class(number)
    except Exception as e:
        print(f"Exception while creating an object for issue {number}", e)
        print(e)
        return
    if current_issue.page_response.status_code != 200:
        print(f'response.status_code for issue number {number} is {current_issue.page_response.status_code}')
        return
    if not current_issue.page_element_with_articles:
        print(f'Expected page element with articles in issue {number} not found')
        return
    try:
        articles_in_tags = current_issue.extract_articles_from_page()
    except Exception as e:
        print(f"Exception while extracting articles from issue {number}")
        print(e)
        return
    if not articles_in_tags:
        print(f"Couldn't extract any articles for issue {number}")
        return
    for item in articles_in_tags:
        try:
            current_article = article_class(item)
        except Exception as e:
            print(f'Exception creating Article object from item {item}, issue number {number}')
            print(e)
            continue
        if not current_article.title:
            print(f'current_article.title is empty for item {item}, issue number {number}')
        if not current_article.href:
            print(f'current_article.href is empty for item {item}, issue number {number}')
        # if not current_article.summary:
        #     print(f'current_article.summary is empty for item below, issue number {number}')
        #     print(f'item: {item}')


if __name__ == '__main__':
    for number in reversed(range(339, latest_issue_number + 1)):
        test_block(IssueAfter338, ArticleAfter338)
    for number in [338]:
        test_block(IssueBefore339, Article338)
    for number in reversed(range(earliest_issue, 338)):
        test_block(IssueBefore339, ArticleBefore338)
