#!/usr/bin/python

# 1. Do the web pages in different topics change at different rates?

import sys
import os

for line in sys.stdin:
    
    domain, date, fetch_time, url_domain, original_url, redirected_url, classified_relevant, content_hash = line.strip().split(' ')

    if classified_relevant == "1":
        print('%s %s %s %s %s' % (domain, url_domain, original_url, date, content_hash))
