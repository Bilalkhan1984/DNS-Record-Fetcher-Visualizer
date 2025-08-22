name: DNS Record Fetcher

on:
  workflow_dispatch:   # allows manual run
  push:
    branches: [ "main" ]

jobs:
  fetch-dns:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          pip install dnspython

      - name: Run DNS fetcher
        run: |
          python dns_fetcher.py

      - name: Upload report
        uses: actions/upload-artifact@v3
        with:
          name: dns-report
          path: report.html
