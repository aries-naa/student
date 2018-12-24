#!/usr/bin/env python3

import re
import time
import os
from os.path import *
from logging import *

from urllib.request import *
from urllib.parse import *
from urllib.error import *
from bs4 import BeautifulSoup


logger = getLogger('xls-downloader')
logger.setLevel(INFO)
console = StreamHandler()
formatter = Formatter('%(asctime)s %(levelname)s: %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)

write_report = None

def is_suburl(base_url, url):

    link = urljoin(base_url, url)
    if link.upper().endswith(".PDF") or \
        link.upper().endswith(".ZIP") or \
        link.upper().endswith(".DOC") or \
        link.upper().endswith(".XLSX") or \
        link.upper().endswith(".XLS"):
        return False
    if link != base_url and link.startswith(base_url):
        return True

    return False


def format_url(url):
    sp_url = urlsplit(url)
    return urlunsplit((sp_url.scheme, sp_url.netloc, sp_url.path, "", ""))


def download_url(url):
    sp_url = urlsplit(url)
    path = join(*sp_url.path.split("/"))
    dir = dirname(path)

    if not exists(dir):
        os.makedirs(dir)

    logger.info("download {}".format(url))
    try:
        urlretrieve(url, path)
        if write_report:
            write_report(url)
    except (URLError, HTTPError, ContentTooShortError, ConnectionResetError):
        logger.warn("download error {}".format(url))


visited_urls = set()
xls_regexp = re.compile(".*\\.XLSX?$")
downloads = set()


def downloader(base_url):

    if base_url not in visited_urls:

        visited_urls.add(base_url)
        base = format_url(base_url)
        links = []

        try:
            with urlopen(base_url) as response:

                http_header = response.info()
                content = "Content-Type"

                if content in http_header and \
                    "text/html" in http_header[content]:

                    logger.info("search in {}".format(base_url))

                    # лекарство от блокировки.
                    time.sleep(0.2)

                    data = response.read()
                    soup = BeautifulSoup(data, 'html.parser')
                    links.extend([urljoin(base, x.get("href"))
                                  for x in soup.find_all('a')
                                  if x.get("href")])

        except (URLError, HTTPError, ContentTooShortError,
                UnicodeEncodeError, ConnectionResetError):
            logger.warn("error in {}".format(base_url))

        for xls_link in filter(lambda x: xls_regexp.match(x.upper()), links):
            if xls_link not in downloads:
                download_url(xls_link)
            downloads.add(xls_link)

        # глубже.
        for sublink in filter(lambda x: is_suburl(base, x), links):
            downloads.add(sublink)
            downloader(sublink)


url = "http://www.cbr.ru/statistics"

with open("report.txt", "w") as report:

    def report_file(url):
        report.write("    download {}\n".format(url))
    write_report = report_file
        
    report.write("Download from: {}\n".format(url))
    downloader(url)
