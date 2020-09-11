import time
import requests
import codetiming


def download_site(url, session):
    with session.get(url) as response:
        # The Session object allows you to persist certain parameters across requests.
        # It also persists cookies across all requests made from the Session instance,
        # and will use urllib3‘s connection pooling.
        # So if you’re making several requests to the same host,
        # the underlying TCP connection will be reused,
        # which can result in a significant performance increase
        a = len(response.content)
        # print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = [
                "https://www.jython.org",
                "http://olympus.realpython.org/dice",
            ] * 80
    with codetiming.Timer():
        download_all_sites(sites)
    with codetiming.Timer():
        for url in sites:
            with requests.get(url) as response:
                a = len(response.content)
