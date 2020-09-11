import concurrent.futures
import requests
import threading
import codetiming

thread_local = threading.local()  # Threading.local() creates an object that look like a global but is specific to
# each individual thread.


# a threading.local() object only needs to be created once,
# not once per thread nor once per function call. The global or class level are ideal locations.
# Here is why: threading.local() actually creates a new instance each time it is called
# (just like any factory or class call would),
# so calling threading.local() multiple times constantly overwrites the original object,
# which in all likelihood is not what one wants.
# When any thread accesses an existing threadLocal variable (or whatever it is called),
# it gets its own private view of that variable.


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


# Because the operating system is in control of when your task gets interrupted
# and another task starts, any data that is shared between the threads needs to be protected,
# or thread-safe. # Unfortunately requests.Session() is not thread-safe.

# There are several strategies for making data accesses thread-safe
# One of them is to use thread-safe data structures like Queue from Python’s queue module.
# These objects use low-level primitives like threading.Lock to ensure that only one thread
# can access a block of code or a bit of memory at the same time.
# You are using this strategy indirectly by way of the ThreadPoolExecutor object.
# Another strategy to use here is something called thread local storage.

def download_site(url):
    session = get_session()  # each thread needs to create its own requests.Session() object
    with session.get(url) as response:
        len(response.content)
        # print(f"Read {len(response.content)} from {url}")


def download_site_without_session(url):
    with requests.get(url) as response:
        len(response.content)


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)  # This method
        # runs the passed-in function on each of the sites in the list. The great part is
        #  that it automatically runs them concurrently using the pool of threads it is managing.


if __name__ == '__main__':
    sites = [
                "https://www.jython.org",
                "http://olympus.realpython.org/dice",
            ] * 80
    with codetiming.Timer():
        download_all_sites(sites)
    with codetiming.Timer():
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(download_site_without_session, sites)
