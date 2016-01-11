#!/usr/bin/python

# 2. Is the rate of new pages arrival different for different topics?

import sys
import os

for line in sys.stdin:

    if line.strip() == 'crawl_domain crawl_date url_domain original_url outlink_url outlink_relevant':
        continue
    
    domain, date, site, url, outlink_url, outlink_relevant = line.strip().split(' ')

    print('%s %s %s %s %s %s' % (domain, site, url, date, outlink_url, outlink_relevant))
