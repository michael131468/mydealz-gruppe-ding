# mydealz-gruppe-ding

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A small program to scrape select mydealz groups and notify with [ntfy.sh][1]
when new deals are available.

Only for educational purposes! Not intended for production use! Scraping that
website may be against their terms of services!

This shows how BeautifulSoup can be used to scrape and parse websites.

## ding.py

See ding.py for the single file script. It launches a periodic scheduled job to
run every 20 minutes that scrapes a select mydealz group for the latest ten
articles. If the articles differ to the previous results (or this is the first
run), the script will send that list to [ntfy.sh][1] to notify an audience of new
deals.

Example:
```
$ python3 ding.py --ntfy-topic michael131468mydealz macbook-air
[Mon Jan  2 22:06:13 2023]: checking for new dealz...
{'title': 'Macbook Air 2022 13" 16GB RAM 256GB SSD - GRAVIS nur mit CB', 'href': 'https://www.mydealz.de/deals/macbook-air-2022-13-16gb-ram-256gb-ssd-gravis-nur-mit-cb-2065002', 'price': '1.469€', 'original_price': '1.529€', 'savings': '-4%', 'merchant': 'GRAVIS'}
{'title': 'MacBook Air M1, grau/silber, 8 GB RAM, 256 GB SSD (Shoop mit 3% Cashback + 5€ Shoop-Gutschein* zusätzlich möglich)', 'href': 'https://www.mydealz.de/deals/macbook-air-m1-grausilber-8-gb-ram-256-gb-ssd-shoop-mit-3-cashback-5eur-shoop-gutschein-zusatzlich-moglich-2098749', 'price': '999€', 'original_price': None, 'savings': '', 'merchant': 'expert'}
{'title': 'Apple MacBook Air M2, 8 GB, 512 GB SSD, verschiedene Farben zum Bestpreis', 'href': 'https://www.mydealz.de/deals/apple-macbook-air-m2-mitternachtsblau-8-gb-512-gb-ssd-mly43da-zum-bestpreis-2098662', 'price': '1.489,50€', 'original_price': '1.574,95€', 'savings': '-5%', 'merchant': 'Conrad'}
{'title': 'APPLE MacBook Air (2022), MLXW3D/A, Notebook mit 13,6 Zoll Display, Apple M2 Prozessor, 8 GB RAM, 256 GB SSD, M2', 'href': 'https://www.mydealz.de/deals/apple-macbook-air-2022-2094111', 'price': '1.249€
', 'original_price': '1.270,93€', 'savings': '-2%', 'merchant': 'Saturn'}
{'title': 'Apple MacBook Air M2 - 8 Core CPU/ 8 Core GPU, 8GB RAM, 256GB SSD, Grau (mit Shoop 1.117€ möglich)', 'href': 'https://www.mydealz.de/deals/apple-macbook-air-m2-8-core-cpu-8-core-gpu-8gb-ram-256gb-ssd-grau-mit-shoop-1117eur-moglich-2092075', 'price': '1.219€', 'original_price': '1.249€', 'savings': '-2%', 'merchant': 'Galaxus'}
{'title': '[Corporate Benefits / Gravis] Apple MacBook Air M2 - 8 Core CPU / 8 Core GPU, 8GB RAM, 256GB SSD', 'href': 'https://www.mydealz.de/deals/corporate-benefits-gravis-apple-macbook-air-m2-8-core-cpu-8-core-gpu-8gb-ram-256gb-ssd-2089224', 'price': '1.239€', 'original_price': '1.264€', 'savings': '-2%', 'merchant': 'GRAVIS'}
{'title': 'MacBook Air 13‘‘ M1, 2020, 8 GB RAM, 256 GB SSD alle Farben', 'href': 'https://www.mydealz.de/deals/macbook-air-13-m1-2020-8-gb-ram-256-gb-ssd-alle-farben-2085461', 'price': '909€', 'original_price': '939,80€', 'savings': '-3%', 'merchant': 'eBay'}
{'title': 'Apple MacBook Air M2 - 8 Core CPU / 10 Core GPU, 8 GB RAM, 512 GB SSD (Ebay - Gravis)', 'href': 'https://www.mydealz.de/deals/apple-macbook-air-m2-8-core-cpu-10-core-gpu-8gb-ram-512gb-ssd-ebay-gravis-2084095', 'price': '1.479€', 'original_price': '1.549€', 'savings': '-5%', 'merchant': 'eBay'}
{'title': 'Apple MacBook Air M2 - 8 Core CPU / 8 Core GPU, 8GB RAM, 256GB SSD (Ebay - Gravis) BESTPREIS', 'href': 'https://www.mydealz.de/deals/apple-macbook-air-m2-8-core-cpu-8-core-gpu-8gb-ram-256gb-ssd-ebay-gravis-2083992', 'price': '1.199€', 'original_price': '1.233,95€', 'savings': '-3%', 'merchant': 'eBay'}
{'title': '*ebay* Apple MacBook Air M1 Ret. 13" (2020)', 'href': 'https://www.mydealz.de/deals/ebay-apple-macbook-air-m1-ret-13-2020-2083930', 'price': '895€', 'original_price': '944€', 'savings': '-5%', 'merchant': 'eBay'}
[Mon Jan  2 22:06:17 2023]: sleeping 1200 seconds...
```

If the `--ntfy-topic` parameter is omitted when the script starts, the
notifications will only be printed to the cli interface and no ntfy.sh
interactions will occur.

If `--example-mode` is set, then the script will not scrape the actual website
but use a [cached test html file](./test/gruppe.macbook-air.html.gz) file as
input instead.

[1]: https://ntfy.sh

## LICENSE

See [LICENSE](LICENSE) file.

