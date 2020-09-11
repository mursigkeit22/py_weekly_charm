#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import logging
import re
from typing import IO
import urllib.error
import urllib.parse

import aiofiles
import aiohttp
from aiohttp import ClientSession
import pathlib
import sys

# any line within a given coroutine will block other coroutines unless that line uses yield, await, or return.

logging.basicConfig(format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
                    level=logging.DEBUG,
                    datefmt="%H:%M:%S",
                    # stream=sys.stderr,
                    filename='example.log')

logger = logging.getLogger("mylogger")
logging.getLogger("chardet.charsetprober").disabled = True  # chardet library is used in aiohttp

HREF_RE = re.compile(r'href="(.*?)"')


#  is a wrapper around a GET request to make the request and decode the resulting page HTML.
#  It makes the request, awaits the response, and raises right away in the case of a non-200 status
async def fetch_html(url: str, session: ClientSession, **kwargs) -> str:
    resp = await session.request(method="GET", url=url, timeout = 10, **kwargs)
    resp.raise_for_status()
    logger.info(f"Got response {resp.status} for URL: {url}")
    html = await resp.text()
    return html


async def parse(url: str, session: ClientSession, **kwargs):
    found = set()
    try:
        html = await fetch_html(url=url, session=session, **kwargs)
    except (aiohttp.ClientError, aiohttp.http.HttpProcessingError,) as e:
        logger.error("aiohttp exception for %s [%s]: %s",
                     url,
                     getattr(e, "status", None),
                     getattr(e, "message", None), )
        return found
    except Exception as e:
        logger.exception(f"Non-aiohttp exception {e.__class__} occured for url{url}")

        return found
    else:
        #  the second portion of parse() is blocking,
        #  but it consists of a quick regex match and ensuring that the links discovered are made into absolute paths
        for link in HREF_RE.findall(html):
            try:
                abslink = urllib.parse.urljoin(url, link)
            except (urllib.error.URLError, ValueError):
                logger.exception("Error parsing URL: %s", link)

            else:
                found.add(abslink)
        logger.info("Found %d links for %s", len(found), url)
        return found


async def write_one(file: IO, url: str, **kwargs) -> None:
    res = await parse(url=url, **kwargs)
    if not res:
        return None
    async with aiofiles.open(file, "a") as f:
        for p in res:
            await f.write(f"{url}\t{p}\n")
        logger.info("Wrote results for source URL: %s", url)


async def bulk_crawl_and_write(file: IO, urls: set, **kwargs):
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(write_one(file=file, url=url, session=session, **kwargs))
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    assert sys.version_info >= (3, 7), "Script requires Python 3.7+."
    here = pathlib.Path(__file__).parent

    # with open(here.joinpath("urls.txt")) as infile:
    #     urls = set(map(str.strip, infile))  # open возвращает набор строк
    urls = {"http://google.com", "http://yahoo.com", "http://linkedin.com", "http://apple.com", "http://microsoft.com",
            "http://facebook.com", "http://twitter.com"}

    outpath = here.joinpath("foundurls.txt")

    #this works too, at least on windows:

    # with open("urls.txt") as infile:
    #     urls = set(map(str.strip, infile))
    # outpath = "foundurls.txt"

    with open(outpath, "w") as outfile:
        outfile.write("source_url\tparsed_url\n")
    asyncio.run(bulk_crawl_and_write(file=outpath, urls=urls))
