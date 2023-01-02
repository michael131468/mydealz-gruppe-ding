#!/usr/bin/env python3

import argparse
import requests
import sched
import sys
import time
import urllib.parse

from bs4 import BeautifulSoup

# Global toggle to use cached test html rather than fetching actual content from the internet
example_mode = False


def get_html(group: str):
    group_url_base = "https://www.mydealz.de/gruppe/"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"
    }

    if example_mode:
        with gzip.open(f"test/gruppe.{group}.html.gz", mode="rt") as test_html_file:
            html_text = test_html_file.read()
    else:
        group_url = urllib.parse.urljoin(group_url_base, group)
        html_text = requests.get(group_url, headers=headers).text

    return html_text


def parse_html_for_dealz(html_text: str):
    dealz = []

    # We use html5lib as it's very lenient. My tests with html.parser found it broke halfway through
    # parsing the html of the site.
    soup = BeautifulSoup(html_text, "html5lib")

    articles = soup.find_all("article")
    for article in articles:
        article_title_tag = article.find("strong", attrs={"class": "thread-title"})
        new_price_tag = article.find("span", attrs={"class": "thread-price"})
        orig_price_tag = article.find("span", attrs={"class": "mute--text"})
        savings_tag = article.find("span", attrs={"class": "space--ml-1"})
        merchant_tag = article.find("span", attrs={"class": "cept-merchant-name"})
        if not article_title_tag:
            continue

        deal = {
            "title": article_title_tag.text,
            "href": article_title_tag.find("a")["href"],
            "price": None,
            "original_price": None,
            "savings": None,
            "merchant": None,
        }

        if new_price_tag:
            deal["price"] = new_price_tag.text

        if orig_price_tag:
            deal["original_price"] = orig_price_tag.text

        if savings_tag:
            deal["savings"] = savings_tag.text

        if merchant_tag:
            deal["merchant"] = merchant_tag.text

        dealz.append(deal)

    return dealz


def get_dealz(group: str):
    html_text = get_html(group)
    dealz = parse_html_for_dealz(html_text)

    return dealz


def dnotify(dealz: list, ntfy_topic: str = None):
    for deal in dealz:
        print(deal)
        if ntfy_topic:
            requests.post(
                f"https://ntfy.sh/{ntfy_topic}",
                data=f"{deal['title']} | {deal['price']}".encode(encoding="utf-8"),
            )


def periodic_job(scheduler, group, previous_dealz, ntfy_topic):
    print(f"[{time.ctime()}]: checking for new dealz...")
    dealz = get_dealz(group)
    if len(previous_dealz) == 0 or dealz[0]["title"] != previous_dealz[0]["title"]:
        new_dealz = list(
            filter(
                lambda x: x["title"] not in [d["title"] for d in previous_dealz], dealz
            )
        )
        previous_dealz = dealz
        dnotify(new_dealz, ntfy_topic=ntfy_topic)
    else:
        print(f"[{time.ctime()}]: no new dealz found.")

    period = 20 * 60
    print(f"[{time.ctime()}]: sleeping {period} seconds...")
    scheduler.enter(
        period, 1, periodic_job, (scheduler, group, previous_dealz, ntfy_topic)
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--example-mode", action="store_true", default=False)
    parser.add_argument("--ntfy-topic", type=str)
    parser.add_argument("group", default="macbook-air")
    args = parser.parse_args()

    previous_dealz = []
    group = args.group

    # Toggle using cached test html rather than fetching actual content from the internet
    if args.example_mode:
        example_mode = True
        import gzip

        group = "macbook-air"

    scheduler = sched.scheduler(time.time, time.sleep)
    periodic_job(scheduler, args.group, previous_dealz, args.ntfy_topic)
    scheduler.run()


if __name__ == "__main__":
    main()
