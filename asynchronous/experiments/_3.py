import concurrent.futures
import requests
import threading
import codetiming

thread_local = threading.local()
session = requests.Session()  # that's wrong - not a session for thread.
# But I don't yet see what exactly goes wrong here


def download_site(url):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
                "https://www.jython.org",
                "http://olympus.realpython.org/dice",
            ] * 80
    with codetiming.Timer():
        download_all_sites(sites)
