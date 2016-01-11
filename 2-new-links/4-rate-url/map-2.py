#!/usr/bin/python

# 2. Is the rate of new pages arrival different for different topics?

import sys
import os

next(sys.stdin)

for line in sys.stdin:

    if line.strip() == 'crawl_domain url_domain original_url crawl_date positive negative unknown total new_links new_relevant_links links_gone relevant_links_gone':
        continue

    line = line.strip().split(' ')

    if len(line) == 1:

        print('%s' % (line[0]))

    elif len(line) == 8:

        domain, site, url, url_new_links_rate, url_new_relevant_links_rate, url_links_gone_rate, url_relevant_links_gone_rate, days_passed = line
        
        print('%s %s %s %s %s %s %s %s' % (url, domain, site, url_new_links_rate, url_new_relevant_links_rate, url_links_gone_rate, url_relevant_links_gone_rate, days_passed))
